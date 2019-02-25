#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os

class RBTreeNode(object):
    def __init__(self):
        super(RBTreeNode, self).__init__()
        self.key = None
        self.content = None
        self.parent = None
        self.left = None
        self.right = None
        self.isBlack = False

class RBTree(object):
    def __init__(self):
        super(RBTree, self).__init__()
        self.root = None

    def __rotateLeft(self, currentNode):
        # A.left=B, A.right=C => C.left=A, A.left=B
        rightNode = currentNode.right
        parentNode = currentNode.parent
        rightLeftNode = rightNode.left if rightNode != None else None

        if currentNode == self.root:
            self.root = rightNode
            rightNode.parent = None
        else:
            if parentNode.right == currentNode:
                parentNode.right = rightNode
            else:
                parentNode.left = rightNode
            rightNode.parent = parentNode

        currentNode.right = rightLeftNode
        if rightLeftNode != None:
            rightLeftNode.parent = currentNode

        rightNode.left = currentNode
        currentNode.parent = rightNode
    
    def __rotateRight(self, currentNode):
        # A.left=B, A.right=C => B.right=A, A.right=C
        leftNode = currentNode.left
        parentNode = currentNode.parent
        leftRightNode = leftNode.right if leftNode != None else None

        if currentNode == self.root:
            self.root = leftNode
            leftNode.parent = None
        else:
            if parentNode.right == currentNode:
                parentNode.right = leftNode
            else:
                parentNode.left = leftNode
            leftNode.parent = parentNode

        currentNode.left = leftRightNode
        if leftRightNode != None:
            leftRightNode.parent = currentNode

        leftNode.right = currentNode
        currentNode.parent = leftNode

    def __rebalance(self, currentNode):
        if currentNode == self.root:
            currentNode.isBlack = True
            return

        parentNode = currentNode.parent
        if parentNode.isBlack == True:
            #parent is black or root
            currentNode.isBlack = False
            return

        grandParentNode = parentNode.parent
        uncleNode = grandParentNode.left if grandParentNode.right == parentNode else grandParentNode.right
        if uncleNode != None and uncleNode.isBlack == False:
            parentNode.isBlack = True
            uncleNode.isBlack = True
            grandParentNode.isBlack = False
            self.__rebalance(grandParentNode)
            return
        
        currentLeftNode = currentNode.left
        currentRightNode = currentNode.right

        if parentNode.left == currentNode and grandParentNode.right == parentNode:
            #if parent and grandparent is inverted, reverted first
            grandParentNode.right = currentNode
            currentNode.parent = grandParentNode

            currentNode.right = parentNode
            parentNode.parent = currentNode

            parentNode.left = currentRightNode
            if currentRightNode != None:
                currentRightNode.parent = parentNode

            self.__rebalance(parentNode)
            return

        if parentNode.right == currentNode and grandParentNode.left == parentNode:
            #if parent and grandparent is inverted, reverted first
            grandParentNode.left = currentNode
            currentNode.parent = grandParentNode

            currentNode.left = parentNode
            parentNode.parent = currentNode

            parentNode.right = currentLeftNode
            if currentLeftNode != None:
                currentLeftNode.parent = parentNode

            self.__rebalance(parentNode)
            return

        grandGrandParentNode = grandParentNode.parent
        if parentNode.left == currentNode:
            #rotate right
            self.__rotateRight(grandParentNode)
            grandParentNode.isBlack = False
            parentNode.isBlack = True
            return

        if parentNode.right == currentNode:
            #rotate left
            self.__rotateLeft(grandParentNode)
            grandParentNode.isBlack = False
            parentNode.isBlack = True
            return

    def __set(self, newNode):
        if self.root == None:
            self.root = newNode
            self.root.isBlack = True
            return

        newNodeSetted = False
        currentNode = self.root
        while(1):
            if currentNode.key == newNode.key:
                currentNode.content = newNode.content
                break
            else:
                if newNode.key < currentNode.key:
                    if currentNode.left == None:
                        currentNode.left = newNode
                        newNode.parent = currentNode
                        newNodeSetted = True
                        break
                    else:
                        currentNode = currentNode.left
                elif newNode.key > currentNode.key:
                    if currentNode.right == None:
                        currentNode.right = newNode
                        newNode.parent = currentNode
                        newNodeSetted = True
                        break
                    else:
                        currentNode = currentNode.right

        if newNodeSetted == True and newNode.parent.isBlack == False:
            self.__rebalance(newNode)

    def set(self, key, content):
        if content == None:
            self.delete(key)
            return
        newNode = RBTreeNode()
        newNode.key = key
        newNode.content = content
        self.__set(newNode)
    
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

    def __swapColor(self, nodeA, nodeB):
        colorTmp = nodeA.isBlack
        nodeA.isBlack = nodeB.isBlack
        nodeB.isBlack = colorTmp

    def __deleteCase(self, parentNode, targetNode):
        targetNodeKey = targetNode.key if targetNode != None else None
        parentNodeKey = parentNode.key if parentNode != None else None
        #case 1, if target node is root 
        if targetNode == self.root:
            return

        cousinNode = parentNode.left if parentNode.right == targetNode else parentNode.right

        #case 2, if cousin node is red, then parent node must be black
        if cousinNode != None and cousinNode.isBlack == False:
            #rotate and change color
            if parentNode.left == targetNode:
                self.__rotateLeft(parentNode)
            else:
                self.__rotateRight(parentNode)
            self.__swapColor(parentNode, cousinNode)
            #then goto case 3

        #case 3, if parent node & cousin node & cousin's left node & cousin's right node is black
        cousinNode = parentNode.left if parentNode.right == targetNode else parentNode.right
        cousinLeftNode = cousinNode.left if cousinNode != None else None
        cousinRightNode = cousinNode.right if cousinNode != None else None
        if (parentNode.isBlack == True 
         and cousinNode != None and cousinNode.isBlack == True 
         and (cousinLeftNode == None or cousinLeftNode.isBlack == True)
         and (cousinRightNode == None or cousinRightNode.isBlack == True)):
            #set cousin red, then goto case 1
            cousinNode.isBlack = False
            self.__deleteCase(parentNode.parent, parentNode)
            return
        
        #case 4, if parent node is red, and cousin node & cousin's left node & cousin's right node is black
        if (parentNode.isBlack == False
         and cousinNode != None and cousinNode.isBlack == True 
         and (cousinLeftNode == None or cousinLeftNode.isBlack == True)
         and (cousinRightNode == None or cousinRightNode.isBlack == True)):
            #change color and finished
            self.__swapColor(cousinNode, parentNode)
            return
        
        targetLeftNode = targetNode.left if targetNode != None else None
        targetRightNode = targetNode.right if targetNode != None else None

        #case 5
        if (cousinNode != None and cousinNode.isBlack == True
         and cousinLeftNode != None and cousinLeftNode.isBlack == True
         and cousinRightNode != None and cousinRightNode.isBlack == False
         and parentNode.left == cousinNode):
         #if cousin & cousin's left node is black, and cousin's right node is red, and cousin is parent's left node
         #then rotate left and change color
            self.__rotateLeft(cousinNode)
            self.__swapColor(cousinNode, parentNode)
        elif (cousinNode != None and cousinNode.isBlack == True
         and cousinLeftNode != None and cousinLeftNode.isBlack == False
         and cousinRightNode != None and cousinRightNode.isBlack == True
         and parentNode.right == cousinNode):
         #if cousin & cousin's right node is black, and cousin's left node is red, and cousin is parent's right node
         #then rotate right and change color
            self.__rotateRight(cousinNode)
            self.__swapColor(cousinNode, parentNode)
        #then goto case 6

        #case 6
        cousinNode = parentNode.left if parentNode.right == targetNode else parentNode.right
        cousinLeftNode = cousinNode.left if cousinNode != None else None
        cousinRightNode = cousinNode.right if cousinNode != None else None
        if (cousinNode != None and cousinNode.isBlack == True
         and cousinRightNode != None and cousinRightNode.isBlack == False
         and parentNode.right == cousinNode):
            self.__rotateLeft(parentNode)
            self.__swapColor(cousinNode, parentNode)
            cousinRightNode.isBlack = True
        elif (cousinNode != None and cousinNode.isBlack == True
         and cousinLeftNode != None and cousinLeftNode.isBlack == False
         and parentNode.left == cousinNode):
            self.__rotateRight(parentNode)
            self.__swapColor(cousinNode, parentNode)
            cousinLeftNode.isBlack = True
        #finished

    def __deleteOneChild(self, targetNode):
        if targetNode == None:
            return
        parentNode = targetNode.parent
        targetLeftNode = targetNode.left
        targetRightNode = targetNode.right
        targetChildNode = targetLeftNode if targetLeftNode != None else targetRightNode
        if targetNode.isBlack == False:
            #target node is red, so target node can't be root, and parent node cant't be None
            if parentNode.left == targetNode:
                parentNode.left = targetChildNode
            else:
                parentNode.right = targetChildNode
            targetChildNode.parent = parentNode
            targetNode = None
        else:
            #target node is black
            if targetChildNode == None or targetChildNode.isBlack == True:
                #child node is black or None, so target node can't be root, and parent node cant't be None
                if parentNode.left == targetNode:
                    parentNode.left = targetChildNode
                else:
                    parentNode.right = targetChildNode
                if targetChildNode != None:
                    targetChildNode.parent = parentNode
                self.__deleteCase(parentNode, targetChildNode)
                targetNode = None
            else:
                #child node is red
                if parentNode == None:
                    #target node is root
                    self.root = targetChildNode
                else:
                    if parentNode.left == targetNode:
                        parentNode.left = targetChildNode
                    else:
                        parentNode.right = targetChildNode
                    if targetChildNode != None:
                        targetChildNode.parent = parentNode
                if targetChildNode != None:
                    targetChildNode.isBlack = True
                targetNode = None

    def delete(self, key):
        targetNode = self.__get(key)
        if targetNode == None:
            return

        if targetNode.left != None and targetNode.right != None:
            biggestLeftSide = self.__findBiggest(targetNode.left)
            targetNode.key = biggestLeftSide.key
            targetNode.content = biggestLeftSide.content
            self.__deleteOneChild(biggestLeftSide)
        else:
            self.__deleteOneChild(targetNode)

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
        print('Node ' + str(currentNode.key))
        print('    content: ' + str(currentNode.content))
        print('    color: ' + ('Black' if currentNode.isBlack == True else 'Red'))
        if currentNode.left == None and currentNode.right == None:
            return
        if currentNode.left != None and currentNode.left.key != None:
            print('    left: ' + str(currentNode.left.key))
        if currentNode.right != None and currentNode.right.key != None:
            print('    right: ' + str(currentNode.right.key))
        if currentNode.left != None:
            self.__fullPrint(currentNode.left)
        if currentNode.right != None:
            self.__fullPrint(currentNode.right)
    
    def fullPrint(self):
        self.__fullPrint(self.root)