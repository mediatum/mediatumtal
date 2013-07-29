# -*- coding: utf-8 -*-
'''
Created on 26.07.2013
@author: stenzel
'''
from __future__ import division, absolute_import
from mediatumtal.talextracted import processTAL


def getTAL(page,context,macro=None,language=None):
    return processTAL(context,file=page, macro=macro, language=language)

def getTALstr(string,context,macro=None,language=None,mode=None):
    return processTAL(context,string=string, macro=macro, language=language, mode=mode)
