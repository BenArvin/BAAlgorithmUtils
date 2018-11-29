#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os
from BAAlgorithmUtils.BAClassUtil import BAClassUtil

class BAACTireTreeNode(object):

	def __init__(self):
		self.children = {}
		self.parent = None
		self.bastard = None
		self.isEndPoint = False
		self.endContent = None

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


class BAACTireTree(object):

	def __init__(self):
		self.root = BAACTireTreeNode()
		self.__keyForTerminal = 'terminal'
		self.__keyForPassing = 'passing'

	def train(self, sample):
		if sample == None or isinstance(sample, str) == False or len(sample) == 0:
			return
		currentNode = self.root
		for char in sample:
			child = currentNode.search(char)
			if child == None:
				newChild = BAACTireTreeNode()
				currentNode.adopt(char, newChild)
				newChild.parent = currentNode
				currentNode = newChild
			else:
				currentNode = child

		currentNode.isEndPoint = True
		currentNode.endContent = sample

	def __automatizeLoop(self, currentKey, currentNode):
		if currentNode.bastard == None:
			if currentNode.parent == None:
				currentNode.bastard = self.root
			elif currentNode.parent == self.root:
				currentNode.bastard = self.root
			else:
				tmpBastard = self.root
				tmpParent = currentNode.parent
				while True:
					if tmpParent.bastard == None:
						break
					elif tmpParent.bastard.children == None or len(tmpParent.bastard.children) == 0:
						tmpParent = tmpParent.parent
					else:
						finded = False
						for key, child in tmpParent.bastard.children.items():
							if key == currentKey:
								finded = True
								tmpBastard = child
								break
						if finded == False:
							tmpParent = tmpParent.parent
						break
				currentNode.bastard = tmpBastard
		if len(currentNode.children) > 0:
			for key, child in currentNode.children.items():
				self.__automatizeLoop(key, child)

	def automatize(self):
		self.__automatizeLoop(None, self.root)

	def __buildBlankResult(self):
		return {self.__keyForTerminal: self.root, self.__keyForPassing: []}

	def __react(self, currentNode, key):
		result = self.__buildBlankResult()
		if currentNode == None:
			return result
		currentNodeTmp = currentNode
		resultTerminal = self.root
		resultPassing = []
		while True:
			if currentNodeTmp.children == None or len(currentNodeTmp.children) == 0:
				#jump
				currentNodeTmp = currentNodeTmp.bastard
				resultPassing.append(currentNodeTmp)
				continue
			
			rightChild = None
			for keyTmp, child in currentNodeTmp.children.items():
				if keyTmp == key:
					rightChild = child
					break
			if rightChild == None:
				if currentNodeTmp == self.root:
					#stop
					resultTerminal = currentNodeTmp
					break
				else:
					#jump
					currentNodeTmp = currentNodeTmp.bastard
					resultPassing.append(currentNodeTmp)
			else:
				#stop
				resultTerminal = rightChild
				break
		result[self.__keyForTerminal] = resultTerminal
		result[self.__keyForPassing] = resultPassing
		return result

	def react(self, currentNode, key):
		if key == None or isinstance(key, str) == False or len(key) == 0:
			return self.__buildBlankResult()
		return self.__react(currentNode, key)

	def finialCheck(self, currentNode):
		return self.__react(currentNode, None)

	def fullPrint(self, currentNode):
		if currentNode == None:
			return
		for key, child in currentNode.children.items():
			if child.isEndPoint == True:
				print(BAClassUtil.hexAddress(currentNode) + ' + ' + key + ' --> ' + BAClassUtil.hexAddress(child) + '(' + str(child.endContent) + ')')
			else:
				print(BAClassUtil.hexAddress(currentNode) + ' + ' + key + ' --> ' + BAClassUtil.hexAddress(child))
		if currentNode.bastard != None:
			print('    ' + BAClassUtil.hexAddress(currentNode) + ' __> ' + BAClassUtil.hexAddress(currentNode.bastard))
		for key, child in currentNode.children.items():
			self.fullPrint(child)

class BAAhoCorasickUtil(object):
	def __init__(self):
		super(BAAhoCorasickUtil, self).__init__()
		self.__acTree = BAACTireTree()

	def train(self, sample):
		self.__acTree.train(sample)

	def prepare(self):
		self.__acTree.automatize()

	def __saveSearchResult(self, resultDic, node, location):
		if resultDic == None:
			resultDic = {}
		if node == None:
			return resultDic
		key = node.endContent
		value = location - len(node.endContent) + 1
		listTmp = []
		if key in resultDic:
			listTmp = resultDic[key]
		listTmp.append(value)
		resultDic[key] = listTmp
		return resultDic

	def search(self, content):
		result = {}
		nodeTmp = self.__acTree.root
		contentLength = len(content)
		for i in range(0, contentLength + 1, 1):
			resultTmp = None
			if i == contentLength:
				resultTmp = self.__acTree.finialCheck(nodeTmp)
			else:
				resultTmp = self.__acTree.react(nodeTmp, content[i])
			nextNode = resultTmp['terminal']
			allNodeNeedCheck = resultTmp['passing']
			allNodeNeedCheck.append(nextNode)
			for item in allNodeNeedCheck:
				if item.isEndPoint == True:
					result = self.__saveSearchResult(result, item, i)
			nodeTmp = nextNode
		return result

	def fullPrint(self):
		self.__acTree.fullPrint(self.__acTree.root)