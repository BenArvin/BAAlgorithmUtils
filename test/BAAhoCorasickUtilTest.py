#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append('../')
from BAAhoCorasickUtil import BAAhoCorasickUtil

def start(trainSamples, experimentalValues):
	print('\n********************************')
	trainsString = ''
	acUtil = BAAhoCorasickUtil()
	for sample in trainSamples:
		trainsString = trainsString + ', ' + sample
		acUtil.train(sample)
	acUtil.prepare()
	print('Sample: ' + trainsString[2 : len(trainsString)])
	print('\nACTree:')
	acUtil.fullPrint()
	print('\nResults:')
	for value in experimentalValues:
		print(value + ': ' + str(acUtil.search(value)))
	print('********************************\n')


if __name__ == '__main__':
	start(['hers', 'his', 'she'], ['ushers', 'shersushis', 'shersushishe'])
	start(['nihao', 'hao', 'hs', 'hsr'], ['sdmfhsgnshejfgnihaofhsrnihao'])
	start(['ab', 'bab', 'bca', 'caa'], ['abccab'])