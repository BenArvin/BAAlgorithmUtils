#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os
from BAAlgorithmUtils.BAClassUtil import BAClassUtil

class BABSTTreeNode(object):
    def __init__(self):
        super(BABSTTreeNode, self).__init__()
        self.key = None
        self.content = None
        self.parent = None
        self.left = None
        self.right = None

class BABSTTree(object):
    def __init__(self):
        super(BABSTTree, self).__init__()
        self.root = None

    def set(self, key, content):
        if content == None:
            self.delete(key)
            return
        if self.root == None:
            self.root = BABSTTreeNode()
            self.root.key = key
            self.root.content = content
            return
        newNode = BABSTTreeNode()
        newNode.key = key
        newNode.content = content
        endNode = self.root
        while(1):
            if newNode.key < endNode.key:
                if endNode.left != None:
                    endNode = endNode.left
                else:
                    endNode.left = newNode
                    newNode.parent = endNode
                    break
            elif newNode.key > endNode.key:
                if endNode.right != None:
                    endNode = endNode.right
                else:
                    endNode.right = newNode
                    newNode.parent = endNode
                    break
            else:
                endNode.content = newNode.content
                break
    
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
    
    def delete(self, key):
        targetNode = self.__get(key)
        if targetNode == None:
            return

        if targetNode == self.root:
            if targetNode.right != None and targetNode.left != None:
                self.root = targetNode.right
                smallestRightSide = self.__findSmallest(targetNode.right)
                smallestRightSide.left = targetNode.left
                targetNode.left.parent = smallestRightSide
            elif targetNode.right == None and targetNode.left == None:
                self.root == None
            else:
                self.root = targetNode.left if targetNode.left != None else targetNode.right
            return

        parentNode = targetNode.parent
        if targetNode.left != None and targetNode.right != None:
            parentNode.left = targetNode.right
            targetNode.right.parent = parentNode
            smallestRightSide = self.__findSmallest(targetNode.right)
            smallestRightSide.left = targetNode.left
            targetNode.left.parent = smallestRightSide
        else:
            nextNode = None
            if targetNode.left == None and targetNode.right != None:
                nextNode = targetNode.right
            elif targetNode.left != None and targetNode.right == None:
                nextNode = targetNode.left
            if parentNode.left == targetNode:
                parentNode.left = nextNode
            else:
                parentNode.right = nextNode
            if nextNode != None:
                nextNode.parent = parentNode

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
    
    def fullPrint(self, currentNode):
        if currentNode == None:
            return
        print(BAClassUtil.hexAddress(currentNode))
        print('    key: ' + str(currentNode.key))
        print('    content: ' + str(currentNode.content))
        if currentNode.left == None and currentNode.right == None:
            return
        if currentNode.left != None:
            print('    left: ' + str(BAClassUtil.hexAddress(currentNode.left)))
        if currentNode.right != None:
            print('    right: ' + str(BAClassUtil.hexAddress(currentNode.right)))
        if currentNode.left != None:
            self.fullPrint(currentNode.left)
        if currentNode.right != None:
            self.fullPrint(currentNode.right)

class BABSTUtil(object):
    def __init__(self):
        super(BABSTUtil, self).__init__()
        self.tree = BABSTTree()

    def set(self, key, content):
        self.tree.set(key, content)

    def get(self, key):
        self.tree.get(key)
    
    def delete(self, key):
        self.tree.delete(key)

    def fullPrint(self):
        self.tree.fullPrint(self.tree.root)