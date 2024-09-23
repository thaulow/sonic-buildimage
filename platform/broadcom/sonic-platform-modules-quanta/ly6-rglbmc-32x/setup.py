#!/usr/bin/env python

import os
from setuptools import setup
os.listdir

setup(
   name='ly6_32x',
   version='1.0',
   description='Module to initialize Quanta LY6-32X platforms',

   packages=['ly6_32x'],
   package_dir={'ly6_32x': 'ly6-32x/classes'},
)
