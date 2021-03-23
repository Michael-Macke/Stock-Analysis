#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 08:02:08 2021

@author: michael
"""
from data_vis import data_vis

"""This file is the function to wrap up the data analysis and predictive model
   functions."""
   

"""TO DO LIST:
      1:Create interface to guide the user in what actions they wish to take
      2:Create basic functionality to visualize just the base data
         i.e.: visualize each column against the date as a line graph
      3:Implement basic predictive modeling
         -Still deciding on first model
         -Needs to be simple
         -Potential starter model is a linear regression model
         -After this, other potential models are non-linear regression and
            neural network"""
            
def data_analytics():
    exit = False
    
    while exit == False:
        print("Welcome to the data analytics and prediction section.")
        print("1: Create visualizations for all available data")
        print("2: Run predictive analysis on select data")
        print("3: Exit back to main menu")
        d = int(input("Which of the above options would you like to do?"))
        if d == 1:
            data_vis()
        """elif d == 2:
            #Predictive analysis wrapper function"""
        elif d == 3:
            exit = True