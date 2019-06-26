#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import sys

from xlsx2html import xlsx2html

if __name__ == '__main__':
    xlsx2html(sys.argv[1], sys.argv[2])


