#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:01:07 2021

@author: michael
"""

import os

"""This function checks if the folder/file exsists or not and returns true/false
   accordingly"""

def path_check(to_check):
    DocRoot = os.path.expanduser("~/Documents")
    path = os.path.join(DocRoot, to_check)
    if os.path.isdir(path) == True:
        return path
    else:
        os.mkdir(path)
        return path