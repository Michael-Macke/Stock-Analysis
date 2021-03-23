#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 08:17:21 2021

@author: michael
"""

import os
import pandas as pd
from yahoofinancials import YahooFinancials
import datetime as dt

"""This is the function data_modernize.
      If there is no data present in the specified file then it will fill in
         the data from the standard start date until the current date. This is 
         considered an initial save
      If there is data present then it will grab the last date in the file and
         pull data from one day after that date until the current date."""
         
def data_modernize(symbol, path):
    end = dt.date.today().strftime("%Y-%m-%d")
    """The issue is with how the datetime object is stored. Need to convert the
       end date into a string for it to work with the yahoofinancials function"""
    if not(os.path.isfile(path)):
        """Standard download starting date will be 01/01/2001"""
        yahoo_financials = YahooFinancials(symbol)
        
        new_data = yahoo_financials.get_historical_price_data(start_date = '2001-01-01',
                                                              end_date = end,
                                                              time_interval = "daily")
        print("Data pulled for:", symbol)
        
        new_df = pd.DataFrame(new_data[symbol]['prices'])
        new_df = new_df.drop('date', axis=1).set_index('formatted_date')
        print("Data for", symbol, "refined and now saving.")
        new_df.to_csv(path)
    else:
        data = pd.read_csv(path)
        """Start date if there is already data in the csv is the day after the
              last date in the csv"""
        start = data['formatted_date'].iloc[-1]
        yahoo_financials = YahooFinancials(symbol)
        
        new_data = yahoo_financials.get_historical_price_data(start_date = start,
                                                              end_date = end,
                                                              time_interval = "daily")
        print("Data pulled for:", symbol)
        new_df = pd.DataFrame(new_data[symbol]['prices'])
        new_df = new_df.drop('date', axis=1)
        data = data.append(new_df)
        print("Data for", symbol, "refined and appended. Now saving.\n")
        data.to_csv(path, index = False)
        