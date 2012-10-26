#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Copyright (c) 2012 Yummy Bian <yummy.bian#gmail.com>. 
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'threadpool',
    version='1.0',
    author="Yummy Bian",
    author_email="yummy.bian#gmail.com",
    url="https://github.com/yummybian",
    packages=['threadpool'],
    platforms=["Any"],
    license="BSD",
    keywords='thread pool',
    description="Implements thread pool with queue module of python.",
)




