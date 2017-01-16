#!/usr/bin/env python
# -*- coding: utf-8 -*-
# owh (c) Thomas C Hicks

from owh.wsgi import app
app.run(port=app.config['PORT'])
