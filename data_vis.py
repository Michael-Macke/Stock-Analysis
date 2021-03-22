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
import seaborn as sns

"""This file wraps up the functionality to create visualizations of the data
      using date as the X axis and each of the columns individually as the
      Y axes
   For visualization we utilize pythons seaborn library to create the lineplots
   CURRENT TASK:
       Find how to expand the size of the figure created so that it is screen wide"""
      
      
#def data_vis():
list_list = ["Companies", "Commodities"]
Corpsym = read_sym("Companies")
Comsym  = read_sym("Commodities")

BA_data = pd.read_csv('/home/michael/Documents/Companies/BA_data/BA.csv', index_col = 'formatted_date')
BA_data.index = pd.to_datetime(BA_data.index, format = '%Y-%m-%d')
sns.lineplot(data = BA_data["high"])

for sect in list_list:
    Symlist = read_sym(sect)
    for symbol in Symlist:
        DocRoot = os.path.expanduser("~/Documents")
        Corp = sect + "/" + symbol + "_data/" + symbol + ".csv"
        CorpPath = os.path.join(DocRoot, Corp)
        #data_modernize updates the data to the current dates data
        print("Updating data for:", symbol)
        data = pd.read_csv(CorpPath, index_col = 'formatted_date')
        data.index = pd.to_datetime(data.index, format = "")
        col_list = list(data.columns.values.tolist())
        for column in col_list:
            col_path = sect + "/" + symbol + "_data/" + symbol + "_"+ column + ".jpg"
            png_path = os.path.join(DocRoot, col_path)
            sns.lineplot(data = data[column])
            #plt.show()
            plt.savefig(png_path)
            plt.clf()
            
    
    #BA_data = pd.read_csv('/home/michael/Documents/Companies/BA_data/BA.csv')
    #AAPL_data = pd.read_csv('/home/michael/Documents/Companies/AAPL_data/AAPL.csv')
        
    #fig = plt.figure(figsize=(10,6))
    
    #ax1 = fig.add_axes([0,0,1,1])
    #ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])
    
    #ax1.set_title("AAPL adjclose")
    
    #ax1.plot(AAPL_data['formatted_date'], AAPL_data['adjclose'], color = 'green')
    #ax2.plot(BA_data['formatted_date'], BA_data['adjclose'], color = 'blue')
    
    #plt.show()