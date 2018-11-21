#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os

class BATireTreeNode(object):

	def __init__(self):
		self.content = None
		self.isEndPoint = False
		self.children = []

	def search(self, content):
		if content == None or isinstance(content, str) == False or len(content) == 0:
			return None
		result = None
		for child in self.children:
			if child.content == content:
				result = child
				break
		return result

	def adopt(self, node):
		if node == None:
			return
		if node not in self.children:
			self.children.append(node)


class BATireTree(object):

	def __init__(self):
		self.__startNode = BATireTreeNode()

	def train(self, sample):
		if sample == None or isinstance(sample, str) == False or len(sample) == 0:
			return
		currentNode = self.__startNode
		for char in sample:
			child = currentNode.search(char)
			if child == None:
				newChild = BATireTreeNode()
				newChild.content = char
				currentNode.adopt(newChild)
				currentNode = newChild
			else:
				currentNode = child

		currentNode.isEndPoint = True

	def check(self, content):
		if content == None or isinstance(content, str) == False or len(content) == 0:
			return False
		currentNode = self.__startNode
		for char in content:
			if currentNode != None:
				currentNode = currentNode.search(char)
			else:
				break
		if currentNode != None and currentNode.isEndPoint == True:
			return True
		else:
			return False

class BATireTreeUtil(object):
	def __init__(self):
		super(BATireTreeUtil, self).__init__()
		