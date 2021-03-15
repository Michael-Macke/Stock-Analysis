#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:29:42 2021

@author: michael
"""

from read_sym import read_sym
import os
import matplotlib.pyplot as plt

"""This file wraps up the functionality to create visualizations of the data
      using date as the X axis and each of the columns individually as the
      Y axes"""
      
def data_vis():
    Corpsym = read_sym("Companies")
    Comsym  = read_sym("Commodities")
    
    