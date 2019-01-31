#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os
from BAAlgorithmUtils.ClassUtil import ClassUtil

class SBOMTreeNode(object):
    def __init__(self):
        super(SBOMTreeNode, self).__init__()
        self.children = {}
        self.bastards = {}
        self.parent = None
        self.isEndPoint = False
        self.endContent = None
        self.suffixTree = None
        self.isTheta = False
    
    def search(self, content):
        if content == None or isinstance(content, str) == False or len(content) == 0:
            return None
        result = None
        for key, value in self.children.items():
            if key == content:
                result = value
                break
        return result

    def adopt(self, key, node):
        if key == None or len(key) == 0 or node == None:
            return
        self.children[key] = node

class SBOMSuffixTree(object):
    def __init__(self):
        super(SBOMSuffixTree, self).__init__()
        self.root = SBOMTreeNode()
        self.length = 0
    
    def train(self, suffix, endContent):
        currentNode = self.root
        for char in suffix:
            child = currentNode.search(char)
            if child == None:
                newChild = SBOMTreeNode()
                currentNode.adopt(char, newChild)
                newChild.parent = currentNode
                currentNode = newChild
            else:
                currentNode = child
        currentNode.isEndPoint = True
        currentNode.endContent = endContent
        
        if len(suffix) > self.length:
            self.length = len(suffix)
    
    def react(self, currentNode, key):
        if currentNode.children != None and key in currentNode.children:
            return currentNode.children[key]
        return None
    
    def fullPrint(self, currentNode):
        if currentNode == None:
            return
        if currentNode.children == None or len(currentNode.children) == 0:
            if currentNode == self.root:
                print('        ' + ClassUtil.hexAddress(currentNode) + '(' + str(currentNode.endContent) + ')')
            return
        for key, child in currentNode.children.items():
            if child.isEndPoint == True:
                print('        ' + ClassUtil.hexAddress(currentNode) + ' + ' + key + ' >>> ' + ClassUtil.hexAddress(child) + '(' + str(child.endContent) + ')')
            else:
                print('        ' + ClassUtil.hexAddress(currentNode) + ' + ' + key + ' >>> ' + ClassUtil.hexAddress(child))
        for key, child in currentNode.children.items():
            self.fullPrint(child)

class SBOMPrefixTree(object):
    def __init__(self):
        super(SBOMPrefixTree, self).__init__()
        self.sNodeTable = {}
        self.root = SBOMTreeNode()
        self.thetaNode = SBOMTreeNode()
        self.thetaNode.isTheta = True
        self.sNodeTable[self.root] = self.thetaNode

    def __getSNode(self, currentNode):
        if currentNode in self.sNodeTable:
            return self.sNodeTable[currentNode]
        else:
            return self.thetaNode
    
    def __setSNode(self, currentNode, sNode):
        self.sNodeTable[currentNode] = sNode
    
    def train(self, sample, endInfo):
        if sample == None or isinstance(sample, str) == False or len(sample) == 0:
            return
        currentNode = self.root
        for i in range(len(sample) - 1, -1, -1):
            char = sample[i]
            child = currentNode.search(char)
            if child == None:
                newChild = SBOMTreeNode()
                currentNode.adopt(char, newChild)
                newChild.parent = currentNode
                currentNode = newChild
            else:
                currentNode = child
        currentNode.isEndPoint = True
        currentNode.suffixTree = SBOMSuffixTree()
        for endItem in endInfo:
            currentNode.suffixTree.train(endItem['suffix'], endItem['content'])
    
    def __automatizeSeeker(self, currentNode, kNode, jumpKey):
        if kNode.isTheta == True:
            self.__setSNode(currentNode, self.root)
        else:
            if jumpKey in kNode.children or jumpKey in kNode.bastards:
                jNode = None
                if jumpKey in kNode.children:
                    jNode = kNode.children[jumpKey]
                else:
                    jNode = kNode.bastards[jumpKey]
                self.__setSNode(currentNode, jNode)
            else:
                kNode.bastards[jumpKey] = currentNode
                self.__automatizeSeeker(currentNode, self.__getSNode(kNode), jumpKey)
    
    def __automatizeLoop(self, currentLayerNodes):
        if currentLayerNodes == None or len(currentLayerNodes) == 0:
            return
        nextLayerNodes = []
        for currentLayerNodeItem in currentLayerNodes:
            currentLayerNode = currentLayerNodeItem['node']
            self.__automatizeSeeker(currentLayerNode, self.__getSNode(currentLayerNode.parent), currentLayerNodeItem['key'])
            if currentLayerNode.children != None and len(currentLayerNode.children) > 0:
                for childKey, childNode in currentLayerNode.children.items():
                    nextLayerNodeItem = {'key': childKey, 'node':childNode}
                    nextLayerNodes.append(nextLayerNodeItem)
        self.__automatizeLoop(nextLayerNodes)

    def automatize(self):
        nextLayerNodes = []
        for childKey, childNode in self.root.children.items():
            nodeItemTmp = {'key': childKey, 'node':childNode}
            nextLayerNodes.append(nodeItemTmp)
        self.__automatizeLoop(nextLayerNodes)

    def react(self, currentNode, key):
        if currentNode.children != None and key in currentNode.children:
            return currentNode.children[key]
        if currentNode.bastards != None and key in currentNode.bastards:
            return currentNode.bastards[key]
        return None

    def fullPrint(self, currentNode):
        if currentNode == None:
            return
        for key, child in currentNode.children.items():
            if child.isEndPoint == True:
                print(ClassUtil.hexAddress(currentNode) + ' + ' + key + ' --> ' + ClassUtil.hexAddress(child) + '(end)')
            else:
                print(ClassUtil.hexAddress(currentNode) + ' + ' + key + ' --> ' + ClassUtil.hexAddress(child))
        for key, child in currentNode.bastards.items():
            print('    ' + ClassUtil.hexAddress(currentNode) + ' + ' + key + ' __> ' + ClassUtil.hexAddress(child))
        if currentNode.suffixTree != None:
            print('    ' + ClassUtil.hexAddress(currentNode) + ' ~~> ' + ClassUtil.hexAddress(currentNode.suffixTree.root))
            currentNode.suffixTree.fullPrint(currentNode.suffixTree.root)
        for key, child in currentNode.children.items():
            self.fullPrint(child)

class SBOMUtil(object):
    def __init__(self):
        super(SBOMUtil, self).__init__()
        self.samples = []
        self.searchWindowLen = 0
        self.samplePrefixDic = {}
        self.prefixTree = SBOMPrefixTree()

    def train(self, sample):
        if sample == None or isinstance(sample, str) == False or len(sample) == 0:
            return
        self.samples.append(sample)
        sampleLen = len(sample)
        if len(self.samples) == 1:
            self.searchWindowLen = sampleLen
        elif sampleLen < self.searchWindowLen:
            self.searchWindowLen = sampleLen

    def prepare(self):
        #cut samples
        self.samplePrefixDic = {}
        for sampleItem in self.samples:
            prefix = sampleItem[0 : self.searchWindowLen]
            suffix = sampleItem[self.searchWindowLen : len(sampleItem)]
            dicItemTmp = {'content': sampleItem, 'suffix': suffix}
            prefixDics = []
            if prefix in self.samplePrefixDic:
                prefixDics = self.samplePrefixDic[prefix]
            prefixDics.append(dicItemTmp)
            self.samplePrefixDic[prefix] = prefixDics

        #build prefix tree
        self.prefixTree = SBOMPrefixTree()
        for prefix, prefixDics in self.samplePrefixDic.items():
            self.prefixTree.train(prefix, prefixDics)

        #automatize
        self.prefixTree.automatize()

    def __saveSearchResult(self, resultDic, sample, location):
        listTmp = []
        if sample in resultDic:
            listTmp = resultDic[sample]
        listTmp.append(location)
        resultDic[sample] = listTmp
        return resultDic

    def search(self, content):
        result = {}
        if content == None or isinstance(content, str) == False or len(content) < self.searchWindowLen:
            return result

        contentLen = len(content)
        offset = 0
        while True:
            if self.searchWindowLen + offset > contentLen:
                break
            currentNode = self.prefixTree.root
            finded = True
            stopIndex = offset + 1
            for i in range(offset + self.searchWindowLen - 1, offset - 1, -1):
                contentChar = content[i]
                nextNodeTmp = self.prefixTree.react(currentNode, contentChar)
                if nextNodeTmp == None:
                    stopIndex = i + 1
                    finded = False
                    break
                else:
                    currentNode = nextNodeTmp
            if finded == True:
                if currentNode.isEndPoint and currentNode.suffixTree != None:
                    currentSuffixNode = currentNode.suffixTree.root
                    j = 1
                    while True:
                        if currentSuffixNode.isEndPoint == True:
                            self.__saveSearchResult(result, currentSuffixNode.endContent, offset)
                        indexTmp = self.searchWindowLen + offset + j - 1
                        if indexTmp >= contentLen:
                            break
                        currentSuffixNodeTmp = currentNode.suffixTree.react(currentSuffixNode, content[indexTmp])
                        if currentSuffixNodeTmp == None:
                            break
                        else:
                            currentSuffixNode = currentSuffixNodeTmp
                        j = j + 1
                offset = offset + 1
            else:
                offset = stopIndex
        return result

    def fullPrint(self):
        self.prefixTree.fullPrint(self.prefixTree.root)