#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:04:56 2021

@author: michael
"""

from symbol_update import update_symbol_list
from data_update import update_data_stores

"""This is the main file for the market analysis project
       The main aim of this project is the practice and learn more aspects of coding
       and create a tool for my own personal use"""

"""TO DO LIST:
      1:Create the functions to create, store and modify the symbol list - COMPLETE
      2:Create the functions to download, store and update the data from the symbol list
      3:Create the functions to run data analytics for the data stored"""

exit = False

while exit == False:
    print("Which option would you like to use?")
    print("1: Modify list of companies or commodities")
    print("2: Update data for all companies and commodities on your list")
    print("3: Run data analytics on company or commodity data")
    print("4: Exit program")
    choice = int(input("Which option number would you like to use?\n"))
    if choice == 1:
        """update_symbol_list is a function to wrap up the modification of company
              and commodity symbol lists.
           If a symbol is added to the list, an initial store of the symbols data
              will be made from the base date (1/1/2010) to the current date as of the
              adding of the symbol."""
        update_symbol_list()
    elif choice == 2:
        """update_data_stores is a function to wrap up the updating of data currently
              stored for the symbol lists."""
        update_data_stores()
    elif choice == 3:
        """data_analytics is a function to wrap up the data analysis process.
           It wraps up functions for visualizing the data, running machine learning
              algorithms on the data, and utilizing the results of the machine learning
              to create predictions about future data."""
        #data_analytics()
    elif choice == 4:
        """This is used to control exiting the menu loop.
           Exiting this menu loop will quit the current run of the program"""
        exit = True