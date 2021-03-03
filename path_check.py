#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:01:07 2021

@author: michael
"""

import os

"""This function checks if the folder/file exsists or not and returns true/false
   accordingly"""

def path_check(to_check, file = False):
    DocRoot = os.path.expanduser("~/Documents")
    if file == False:
        path = os.path.join(DocRoot, to_check)
        if os.path.isdir(path) == True:
            return path
        else:
            os.mkdir(path)
            return path
    else:
        path = os.path.join(DocRoot, to_check)
        if os.path.isfile(path) == True:
            return path
        else:
            with open(path, "w+") as empty_csv:
                pass
            return path