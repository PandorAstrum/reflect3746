#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__version__ = "0.0.1"
__email__ = "dreadlordn@gmail.com"
__status__ = "Production"
__license__ = "GPL-3"
__copyright__ = "Copyright 2020, PandorAstrum"
__date__ = 8/26/2020
__desc__ = "Flask server runner"
"""

from App import create_app

if __name__ == "__main__":

    app = create_app()

    app.run()
