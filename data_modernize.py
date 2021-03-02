#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 08:17:21 2021

@author: michael
"""


"""This is the function data_modernize.
      If there is no data present in the specified file then it will fill in
         the data from the standard start date until the current date. This is 
         considered an initial save
      If there is data present then it will grab the last date in the file and
         pull data from one day after that date until the current date."""
         
def data_modernize(symbol, path):
    