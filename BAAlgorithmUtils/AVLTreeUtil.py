#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os
from BAAlgorithmUtils.ClassUtil import ClassUtil

class AVLTreeNode(object):
    def __init__(self):
        super(AVLTreeNode, self).__init__()
        self.key = None
        self.content = None
        self.left = None
        self.right = None
        self.height = 0

class AVLTree(object):
    def __init__(self):
        super(AVLTree, self).__init__()
        self.root = None

    def __rebalance(self, tmpRoot):
        if tmpRoot == None:
            return None

        newTmpRoot = tmpRoot

        leftHeight = 0
        rightHeight = 0
        if newTmpRoot.left != None:
            leftHeight = newTmpRoot.left.height + 1
        if newTmpRoot.right != None:
            rightHeight = newTmpRoot.right.height + 1

        if leftHeight - rightHeight == 2:
            #deeper left
            leftNodeLeftHeight = 0
            leftNodeRightHeight = 0
            if newTmpRoot.left.left != None:
                leftNodeLeftHeight = newTmpRoot.left.left.height + 1
            if newTmpRoot.left.right != None:
                leftNodeRightHeight = newTmpRoot.left.right.height + 1
            if leftNodeLeftHeight < leftNodeRightHeight:
                #if child tree is inverted, reverted first
                leftTmp = newTmpRoot.left
                leftRightTmp = leftTmp.right
                leftTmp.right = leftRightTmp.left
                leftRightTmp.left = leftTmp
                newTmpRoot.left = leftRightTmp
            oldLeft = newTmpRoot.left
            oldTmpRoot = newTmpRoot
            oldTmpRoot.left = oldLeft.right
            newTmpRoot = oldLeft
            newTmpRoot.right = oldTmpRoot
        elif rightHeight - leftHeight == 2:
            #deeper right
            rightNodeLeftHeight = 0
            rightNodeRightHeight = 0
            if newTmpRoot.right.left != None:
                rightNodeLeftHeight = newTmpRoot.right.left.height + 1
            if newTmpRoot.right.right != None:
                rightNodeRightHeight = newTmpRoot.right.right.height + 1
            if rightNodeRightHeight < rightNodeLeftHeight:
                #if child tree is inverted, reverted first
                rightTmp = newTmpRoot.right
                rightLeftTmp = rightTmp.left
                rightTmp.left = rightLeftTmp.right
                rightLeftTmp.right = rightTmp
                newTmpRoot.right = rightLeftTmp
            oldRight = newTmpRoot.right
            oldTmpRoot = newTmpRoot
            oldTmpRoot.right = oldRight.left
            newTmpRoot = oldRight
            newTmpRoot.left = oldTmpRoot
        
        return newTmpRoot
    
    def __recalculateHeight(self, currentNode):
        #TODO: this method is heavy and high frequency used, should be optimized
        if currentNode == None:
            return 0
        leftHeight = 0
        if currentNode.left != None:
            leftHeight = self.__recalculateHeight(currentNode.left) + 1
        rightHeight = 0
        if currentNode.right != None:
            rightHeight = self.__recalculateHeight(currentNode.right) + 1
        currentNode.height = max(leftHeight, rightHeight)
        return currentNode.height

    def __set(self, tmpRoot, newNode):
        if tmpRoot == None:
            return newNode

        newTmpRoot = tmpRoot
        if newNode.key == newTmpRoot.key:
            newTmpRoot.content = newNode.content
        else:
            if newNode.key < newTmpRoot.key:
                newTree = self.__set(newTmpRoot.left, newNode)
                newTmpRoot.left = newTree
            elif newNode.key > newTmpRoot.key:
                newTree = self.__set(newTmpRoot.right, newNode)
                newTmpRoot.right = newTree
            
            newTmpRoot = self.__rebalance(newTmpRoot)

        self.__recalculateHeight(newTmpRoot)
        return newTmpRoot

    def set(self, key, content):
        if content == None:
            self.delete(key)
            return
        newNode = AVLTreeNode()
        newNode.key = key
        newNode.content = content
        self.root = self.__set(self.root, newNode)
    
    def __findBiggest(self, startNode):
        currentNode = startNode
        while(1):
            if currentNode.right == None:
                return currentNode
            else:
                currentNode = currentNode.right
    
    def __findSmallest(self, startNode):
        currentNode = startNode
        while(1):
            if currentNode.left == None:
                return currentNode
            else:
                currentNode = currentNode.left
    
    def __delete(self, currentNode, key):
        if currentNode == None:
            return None
        
        result = None
        if currentNode.key == key:
            if currentNode.left != None and currentNode.right != None:
                if currentNode.left.height > currentNode.right.height:
                    #use key and content of biggest node in left side, reset current node
                    biggestLeftSide = self.__findBiggest(currentNode.left)
                    currentNode.key = biggestLeftSide.key
                    currentNode.content = biggestLeftSide.content
                    #delete that biggest node in left side
                    currentNode.left = self.__delete(currentNode.left, biggestLeftSide.key)
                else:
                    #use key and content of smallest node in right side, reset current node
                    smallestRightSide = self.__findSmallest(currentNode.right)
                    currentNode.key = smallestRightSide.key
                    currentNode.content = smallestRightSide.content
                    #delete that smallest node in right side
                    currentNode.right = self.__delete(currentNode.right, smallestRightSide.key)
                result = currentNode
            elif currentNode.left != None:
                result = currentNode.left
            elif currentNode.right != None:
                result = currentNode.right
        else:
            if currentNode.key > key:
                currentNode.left = self.__delete(currentNode.left, key)
            else:
                currentNode.right = self.__delete(currentNode.right, key)
            currentNode = self.__rebalance(currentNode)
            result = currentNode
        self.__recalculateHeight(result)
        return result

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __get(self, key):
        currentNode = self.root
        while(1):
            if currentNode == None:
                return None
            if currentNode.key == key:
                return currentNode
            if key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

    def get(self, key):
        result = self.__get(key)
        if result == None:
            return None
        else:
            return result.content
    
    def __fullPrint(self, currentNode):
        if currentNode == None:
            return
        print(ClassUtil.hexAddress(currentNode))
        print('    key: ' + str(currentNode.key))
        print('    content: ' + str(currentNode.content))
        print('    height: ' + str(currentNode.height))
        if currentNode.left == None and currentNode.right == None:
            return
        if currentNode.left != None:
            print('    left: ' + str(ClassUtil.hexAddress(currentNode.left)))
        if currentNode.right != None:
            print('    right: ' + str(ClassUtil.hexAddress(currentNode.right)))
        if currentNode.left != None:
            self.__fullPrint(currentNode.left)
        if currentNode.right != None:
            self.__fullPrint(currentNode.right)
    
    def fullPrint(self):
        self.__fullPrint(self.root)