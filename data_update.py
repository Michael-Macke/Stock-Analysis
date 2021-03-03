#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 07:23:40 2021

@author: michael
"""

from read_sym import read_sym
from path_check import path_check
from data_modernize import data_modernize

"""This will be the function to wrap the updating of the market data for 
      companies and commodities
   Company and commodity data are stored in their repective folder divided by 
      the company or symbol"""
      
def update_data_stores():
    """Since this set of functions aims to just update the data based on the 
          list of symbols there is no need to ask the user what they want to 
          do."""
          
    """First is retrieving the lists of company and commodity symbols"""
    Corpsym = read_sym("Companies")
    Comsym  = read_sym("Commodities")
    
    """Now that we have the symbol lists, we need to go through both lists 
          and update the data"""
    """Update_data function will check if the data file is empty or not.
          If empty, it will pull data from the start data to current and fill 
             in the file with it
          If not empty, the last date in the data will be retrieved and used 
             as the starting point"""
    for symbol in Corpsym:
        Corp = "Companies/" + symbol + "_data/" + symbol + ".csv"
        CorpPath = path_check(Corp, True)
        #data_modernize updates the data to the current dates data
        data_modernize(symbol, CorpPath)
    for symbol in Comsym:
        Comm = "Commodities/" + symbol + "_data/" + symbol + ".csv"
        CommPath = path_check(Comm, True)
        #data_modernize updates the data to the current dates data
        data_modernize(symbol, CommPath)