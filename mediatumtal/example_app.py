# -*- coding: utf-8 -*-
'''
Created on 26.07.2013
@author: stenzel
'''
from __future__ import division, absolute_import
import logging
import os.path
import sys

from flask import Flask, render_template
# some debugging and profiling stuff
try:
    from dozer import Dozer, Profiler
except:
    Dozer = None
try:
    from flask_debugtoolbar import DebugToolbarExtension
except:
    DebugToolbarExtension = None

sys.path.append(".")    

from mediatumtal.tal import getTAL


logging.basicConfig(level=logging.DEBUG)
logg = logging.getLogger(__name__)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'TODU9H7xmFHiLRpOforS/gREA+suKW+TEDxNnJ/0C'

# if DebugToolbarExtension:
#     toolbar = DebugToolbarExtension(app)

if Dozer:
    wsgi_app = Profiler(app, profile_path="/tmp")
else: 
    wsgi_app = app


class Pizza():
    def get_toppings(self):
        return ["tomatoes", "mushrooms"]
    
    def get_size(self):
        return 13
    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/talpizza")
def talpizza():
    piz = Pizza()
    return getTAL("templates/pizza_tal.html", dict(pizza=piz))


@app.route("/jinjapizza")
def jinjapizza():
    piz = Pizza()
    return render_template("pizza_jinja.html", pizza=piz)


if __name__ == "__main__":
    ### some debugging helpers
    import signal
    # pdb debug hook
    # ipdb hook
    try:
        import ipdb
    except:
        ipdb = None
    if ipdb:
        def start_ipdb(signal, trace):
            ipdb.set_trace()
        logg.info("setting up ipdb debugging hook...")
        signal.signal(signal.SIGQUIT, start_ipdb)
    else:
        import pdb
        def start_pdb(signal, trace):
            pdb.set_trace()
        logg.info("setting up pdb debugging hook...")
        signal.signal(signal.SIGQUIT, start_pdb)
     
    # adapted from flask.app.App.run()
    from werkzeug.serving import run_simple
    try:
        run_simple("localhost", 5000, wsgi_app, use_reloader=True, use_debugger=True)
    finally:
        app._got_first_request = False