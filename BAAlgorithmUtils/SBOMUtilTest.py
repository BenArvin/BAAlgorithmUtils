#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os
sys.path.append('../')

from BAAlgorithmUtils.SBOMUtil import SBOMUtil

def start(trainSamples, experimentalValues):
    print('\n********************************')
    trainsString = ''
    sbomUtil = SBOMUtil()
    for sample in trainSamples:
        trainsString = trainsString + ', ' + sample
        sbomUtil.train(sample)
    sbomUtil.prepare()
    print('Sample: ' + trainsString[2 : len(trainsString)])
    print('\nTree:')
    sbomUtil.fullPrint()
    print('\nResults:')
    for value in experimentalValues:
        print(value + ': ' + str(sbomUtil.search(value)))
    print('********************************\n')

if __name__ == '__main__':
    start(['announce'], ['announce', 'announ', 'announce123', '123announce', 'announceannounce', 'announce123announc456nnounce789announce123announce'])
    start(['barbarian', 'bomb'], ['arbarbarianbara'])
    start(['announce', 'annual', 'annually'], ['CPM_annual_conference_announce'])
    start(['hers', 'his', 'she'], ['ushers', 'shersushis', 'shersushishe'])
    start(['nihao', 'hao', 'hs', 'hsr'], ['sdmfhsgnshejfgnihaofhsrnihao'])
    start(['nihao', 'hao', 'haoa'], ['unihaoabc'])
    start(['nihao', 'hao', 'ao'], ['unihaoabc'])
    start(['nihao', 'hao', 'ao', 'a'], ['unihaoabc'])
    start(['ab', 'bab', 'bca', 'caa'], ['abccab'])
    start(['aa'], ['aaaaaaaaa'])
    start(['aaa'], ['aaaaaaaaa'])
    start(['With', 'Vie'], ['/With'])