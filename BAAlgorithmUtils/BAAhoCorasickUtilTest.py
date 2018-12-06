#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.BAAhoCorasickUtil import BAAhoCorasickUtil

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
	start(['nihao', 'hao', 'haoa'], ['unihaoabc'])
	start(['nihao', 'hao', 'ao'], ['unihaoabc'])
	start(['nihao', 'hao', 'ao', 'a'], ['unihaoabc'])
	start(['ab', 'bab', 'bca', 'caa'], ['abccab'])
	start(['aa'], ['aaaaaaaaa'])
	start(['aaa'], ['aaaaaaaaa'])