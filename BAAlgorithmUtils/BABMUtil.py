#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python3 required!

import sys, os

class BABMUtil(object):
    def __init__(self):
        super(BABMUtil, self).__init__()
        self.__matcher = None
        self.badCharTable = {}
        self.goodSuffixTable = {}

    def __buildBadCharDic(self, matcher):
        self.badCharTable = {}
        matcherLen = len(matcher)
        for i in range(matcherLen):
            currentChar = matcher[i]
            locations = []
            if currentChar in self.badCharTable:
                locations = self.badCharTable[currentChar]
            locations.append(i)
            self.badCharTable[currentChar] = locations

    def __getOffsetByBadCharRule(self, char, stopLocation):
        badCharLocations = []
        if char in self.badCharTable:
            badCharLocations = self.badCharTable[char]
        for i in range(len(badCharLocations), 0, -1):
            locationTmp = badCharLocations[i - 1]
            if locationTmp < stopLocation:
                return stopLocation - locationTmp - 1
        return stopLocation

    def __buildGoodSuffixDic(self, matcher):
        self.goodSuffixTable = {}
        matcherLen = len(matcher)
        for i in range(matcherLen, 1, -1):
            tmpSuffix = matcher[i - 1 : matcherLen]
            tmpSuffixLen = len(tmpSuffix)
            finded = False
            locationTmp = matcherLen - tmpSuffixLen - 1
            while True:
                if locationTmp <= 0 - tmpSuffixLen:
                    break
                matchedThisTime = True
                for j in range(0, tmpSuffixLen, 1):
                    if locationTmp + j < 0:
                        continue
                    if tmpSuffix[j] != matcher[locationTmp + j]:
                        matchedThisTime = False
                if matchedThisTime == True:
                    finded = True
                    break
                locationTmp = locationTmp - 1
            
            if finded == True:
                self.goodSuffixTable[tmpSuffix] = i - 1 - locationTmp
            else:
                self.goodSuffixTable[tmpSuffix] = matcherLen
    
    def __getOffsetByGoodSuffixRule(self, matchedPart):
        if matchedPart == None or len(matchedPart) == 0:
            return 0
        return self.goodSuffixTable[matchedPart]

    def setMatcher(self, matcher):
        if matcher == None or len(matcher) == 0:
            return
        self.__matcher = matcher
        self.__buildBadCharDic(self.__matcher)
        self.__buildGoodSuffixDic(self.__matcher)
        
    def __searchLoop(self, content, duplMode, matcher, start, result):
        if start + len(matcher) > len(content):
            return
        finded = True
        offsetNextLoop = len(matcher)
        matchedPart = ""
        for i in range(len(matcher), 0, -1):
            currentContentChar = content[start + i - 1]
            currentMatcherChar = matcher[i - 1]
            if currentContentChar != currentMatcherChar:
                offsetOfBadChar = self.__getOffsetByBadCharRule(currentContentChar, i)
                offsetOfGoodSuffix = self.__getOffsetByGoodSuffixRule(matchedPart)
                offsetNextLoop = max(offsetOfBadChar, offsetOfGoodSuffix)
                finded = False
                break
            else:
                matchedPart = currentContentChar + matchedPart
        if finded == True:
            if duplMode == True:
                offsetNextLoop = 1
            result.append(start)
        self.__searchLoop(content, duplMode, matcher, start + offsetNextLoop, result)

    def search(self, content, duplMode):
        result = []
        self.__searchLoop(content, duplMode, self.__matcher, 0, result)
        return result