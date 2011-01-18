#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    calcmymarks.main
    ~~~~~~~~~~~~~~~~~~~~

    The main application code. 

    :copyright: (c) 2009-2011 by Aaron Toth.
    :license: Apache 2.0, see LICENSE for more details.
"""

import os
import sys
import cgi

dirname = os.path.dirname(__file__)
sys.path.append(os.path.join(dirname, 'lib'))

from google.appengine.ext.webapp import util
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify

from markcalc import MarkCalc

DEBUG = False

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    """Main area"""
    return render_template('index.html')

@app.route('/_calculate', methods=['GET', 'POST'])
def calculate():
    """Main calculator"""
    error = False

    try:
        orig = request.args.get('orig', type=float)
    except:
        error = True

    curr = request.args.getlist('curr')
    eval = request.args.getlist('eval')
    tally = request.args.getlist('tally')
    choice = request.args.get('type')

    current = []
    for i in range(len(curr)):
        try:
            curr[i] = float(curr[i])
            eval[i] = cgi.escape(str(eval[i]))
            tally[i] = float(tally[i])
            current.append([curr[i], eval[i], tally[i]])
        except:
            error = True

    mk = MarkCalc(current)
        
    if (choice == 'course'):
        result = mk.needed(orig)
        result_str = ["You need a", "on the final exam to get a %0.1f%% in \
                the course" % orig]
    else:
        result = mk.whatif(orig)
        result_str = ["If you get a %0.1f%% on the final exam, you'll get a"
                % orig, "in the course"]
    
    tally.append(mk.exam_total())
    eval.append("Exam")
    
    return jsonify(res = round(result, 2),
                   curr = curr,
                   eval = eval,
                   tally = tally,
                   len_curr = len(curr),
                   res_str = result_str,
                   error = error)

@app.route('/error')
def error():
    """Error landing page"""
    return render_template('error.html')

def main():
    """Main runner for GAE"""
    util.run_wsgi_app(app)

if __name__ == '__main__':
    main()
