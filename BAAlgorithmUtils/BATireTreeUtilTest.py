#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.BATireTreeUtil import BATireTree

if __name__ == '__main__':
	treeInstance = BATireTree()
	treeInstance.train('aababbaba')
	treeInstance.train('aababba')
	treeInstance.train('aababbabab')
	treeInstance.train('abaabbba')
	treeInstance.train('b')

	print('aababbaba: ' + str(treeInstance.check('aababbaba')))
	print('aababba: ' + str(treeInstance.check('aababba')))
	print('aababbabab: ' + str(treeInstance.check('aababbabab')))
	print('abaabbba: ' + str(treeInstance.check('abaabbba')))
	print('b: ' + str(treeInstance.check('b')))
	print('abbb: ' + str(treeInstance.check('abbb')))
	print('abaa: ' + str(treeInstance.check('abaa')))
	print('ba: ' + str(treeInstance.check('ba')))
