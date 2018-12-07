#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os

class BAHorspoolUtil(object):
    def __init__(self):
        super(BAHorspoolUtil, self).__init__()
        self.__matcher = None
        self.offsetTable = {}

    def __buildOffsetTable(self, matcher):
        self.offsetTable = {}
        matcherLen = len(matcher)
        for i in range(matcherLen):
            currentChar = matcher[i]
            locations = []
            if currentChar in self.offsetTable:
                locations = self.offsetTable[currentChar]
            locations.append(i)
            self.offsetTable[currentChar] = locations

    def __getOffset(self, flagChar, stopLocation, matcherLen):
        badCharLocations = []
        if flagChar in self.offsetTable:
            badCharLocations = self.offsetTable[flagChar]
        for i in range(len(badCharLocations), 0, -1):
            locationTmp = badCharLocations[i-1]
            if locationTmp < stopLocation:
                return matcherLen - 1 - locationTmp
        return matcherLen

    def setMatcher(self, matcher):
        if matcher == None or len(matcher) == 0:
            return
        self.__matcher = matcher
        self.__buildOffsetTable(self.__matcher)
        
    def __searchLoop(self, content, duplMode, matcher, start, result):
        if start + len(matcher) > len(content):
            return
        matcherLen = len(matcher)
        flagChar = content[start + matcherLen - 1]
        finded = True
        offsetNextLoop = matcherLen
        for i in range(matcherLen - 1, 0, -1):
            currentContentChar = content[start + i]
            currentMatcherChar = matcher[i]
            if currentContentChar != currentMatcherChar:
                offsetNextLoop = self.__getOffset(flagChar, i, len(matcher))
                finded = False
                break
        if finded == True:
            if duplMode == True:
                offsetNextLoop = 1
            result.append(start)
        self.__searchLoop(content, duplMode, matcher, start + offsetNextLoop, result)

    def search(self, content, duplMode):
        result = []
        self.__searchLoop(content, duplMode, self.__matcher, 0, result)
        return result