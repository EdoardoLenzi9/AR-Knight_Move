#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


# load .env configs
from knights_tour.utils.env import Env
Env.load()


# load tests/
import unittest

from tests import CliTest


'''Run all tests in tests/'''

unittest.main()