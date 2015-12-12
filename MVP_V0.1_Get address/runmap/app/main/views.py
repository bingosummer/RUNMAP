# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import request, render_template, session, redirect, url_for, current_app
import json
import logging
from ..logger import handler
from . import main


logger = logging.getLogger(__file__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', api_key=current_app.config['API_KEY'])
