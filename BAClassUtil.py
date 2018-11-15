#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")

class BAClassUtil(object):

	@classmethod
	def hexAddress(cls, object):
		if object == None:
			return '_None_'
		return '0x' + ("%x"%id(object))
		