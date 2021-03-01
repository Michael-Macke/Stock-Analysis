#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:17:25 2021

@author: michael
"""
import os
from path_check import path_check

"""This is the function to read the symbol list from the provided symbol type"""

def read_sym(symt):
    base_path = path_check(symt)
    symbol_path = os.path.join(base_path, "symbollist.txt")
    if not(os.path.isfile(symbol_path)):
        with open("symbollist.txt", "w") as new:
            pass
        return {}
    elif os.path.isfile(symbol_path):
        with open(symbol_path, "r") as reader:
            symbols = reader.readlines()
        return set(symbols)