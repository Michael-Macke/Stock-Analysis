#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:40:00 2021

@author: michael
"""
import os
from path_check import path_check
from read_sym import read_sym

"""This is the function to modify symbol lists"""

def write_sym(symt, symlist, modifier):
    base_path = path_check(symt)
    symbol_path = os.path.join(base_path, "symbollist.txt")
    if not(os.path.isfile(symbol_path)):
        print("File does not exist. Creating one now.")
    else:
        print("File exists. Checking if there is content in file.")
        content = read_sym(symt)
        if not content and modifier == "delete":
            print("There is no content to be deleted. \n Returning you to the menu")
            return
        elif content:
            if modifier == "add":
                content.add(symlist)
            elif modifier == "delete":
                content.discard(symlist)
    with open(symbol_path, "w") as writer:
        writer.writelines("%s\n" % symbol for symbol in symlist)
    
    return
            