# -*- coding: utf-8 -*-
'''
Created on 26.07.2013
@author: stenzel
'''
from __future__ import division, absolute_import
from mediatumtal import talextracted
from mediatumtal.talextracted import runTAL, processTAL, u_processTAL


def getTAL(page, context, macro=None, language=None, request=None):
    return processTAL(context, file=page, macro=macro, language=language, request=request)

def u_getTAL(page, context, macro=None, language=None, request=None):
    return u_processTAL(context, file=page, macro=macro, language=language, request=request)

def getTALstr(string, context, macro=None, language=None, mode=None):
    return processTAL(context, string=string, macro=macro, language=language, mode=mode)


def set_base(basedir):
    talextracted.setBase(basedir)


def add_translator(translator):
    talextracted.addTranslator(translator)


def add_macro_resolver(macroresolver):
    talextracted.addMacroResolver(macroresolver)
