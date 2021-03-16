#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:29:42 2021

@author: michael
"""

from read_sym import read_sym
import pandas as pd
import os
import matplotlib.pyplot as plt

"""This file wraps up the functionality to create visualizations of the data
      using date as the X axis and each of the columns individually as the
      Y axes"""
      
#def data_vis():
list_list = ["Companies", "Commodities"]
Corpsym = read_sym("Companies")
Comsym  = read_sym("Commodities")

for sect in list_list:
    Symlist = read_sym(sect)
    for symbol in Symlist:
        DocRoot = os.path.expanduser("~/Documents")
        Corp = sect + "/" + symbol + "_data/" + symbol + ".csv"
        CorpPath = os.path.join(DocRoot, Corp)
        #data_modernize updates the data to the current dates data
        print("Updating data for:", symbol)
        data = pd.read_csv(CorpPath)
        col_list = list(data.columns.values.tolist())
        col_list.remove('formatted_date')
        for column in col_list:
            fig = plt.figure(figsize=(10,6))
            
            ax1 = fig.add_axes([0,0, 1, 1])
            
            title = symbol + "_" + column
            
            ax1.set_title(title)
            
            ax1.plot(data['formatted_date'], data[column], color = "blue")
            
            png_path = sect + "/" + symbol + "_data/" + title + ".png"
            
            pngfinal = os.path.join(DocRoot, png_path)
            
            plt.show()
            
            plt.savefig(pngfinal, bbox_inches = "tight", pad_inches = 1.1)
            
    
    #BA_data = pd.read_csv('/home/michael/Documents/Companies/BA_data/BA.csv')
    #AAPL_data = pd.read_csv('/home/michael/Documents/Companies/AAPL_data/AAPL.csv')
        
    #fig = plt.figure(figsize=(10,6))
    
    #ax1 = fig.add_axes([0,0,1,1])
    #ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])
    
    #ax1.set_title("AAPL adjclose")
    
    #ax1.plot(AAPL_data['formatted_date'], AAPL_data['adjclose'], color = 'green')
    #ax2.plot(BA_data['formatted_date'], BA_data['adjclose'], color = 'blue')
    
    #plt.show()