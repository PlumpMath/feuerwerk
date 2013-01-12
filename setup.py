#!/usr/bin/env python
# -*- coding: utf-8 -*-

# feuerwerk
# Copyright (C) 2013  Luca Wehrstedt <luca.wehrstedt@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
feuerwerk
=========

"""

from distutils.core import setup

setup(
    name='feuerwerk',
    version='0.1-dev',
    author='Luca Wehrstedt',
    author_email='luca.wehrstedt@gmail.com',
    license='GNU Affero General Public License v3',
    url='https://github.com/lerks/feuerwerk',

    provides=['feuerwerk (0.1)'],
    requires=[],

    description='A fast asynchronous coroutine-based HTTP server',
    long_description=__doc__,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    packages=['feuerwerk'],
)
