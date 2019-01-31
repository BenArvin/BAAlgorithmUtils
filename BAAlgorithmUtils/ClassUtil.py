#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os

class ClassUtil(object):

	@classmethod
	def hexAddress(cls, object):
		if object == None:
			return '_None_'
		return '0x' + ("%x"%id(object))
		