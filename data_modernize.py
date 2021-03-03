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
    end = dt.date.today()
    print(os.path.isfile(path))
    if not(os.path.isfile(path)):
        print("HERE")
        """Standard download starting date will be 01/01/2001"""
        start = dt.date("2001-01-01")
        yahoo_financials = YahooFinancials(symbol)
        
        new_data = yahoo_financials.get_historical_price_data(start_date = start,
                                                              end_date = end)
        
        new_df = pd.DataFrame(new_data[symbol]['prices'])
        new_df = new_df.drop('date', axis=1).set_index('formatted_date')
        new_df.to_csv(path)
    else:
        print("HERE2")
        data = pd.read_csv(path)
        """Start date if there is already data in the csv is the day after the
              last date in the csv"""
        start = data['date'].iloc[-1]
        yahoo_financials = YahooFinancials(symbol)
        
        new_data = yahoo_financials.get_historical_price_data(start_date = start,
                                                              end_date = end)
        
        new_df = pd.DataFrame(new_data[symbol]['prices'])
        new_df = new_df.drop('date', axis=1).set_index('formatted_date')
        
        data.append(new_df)
        data.to_csv(path)
        