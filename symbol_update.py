#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:09:54 2021

@author: michael
"""


"""This will be the file to wrap the updating of the symbol lists
      Symbol lists will differ between companies and commodities
      The symbol lists for companies and commodities will be stored in their
         respective folders"""
         
def update_symbol_list():
    """First we need to find out which of the types are being modified"""
    print("Which type of symbol are you wishing to modify?")
    print("1: Company symbol list")
    print("2: Commodity symbol list")
    symt = int(input("Do you wish to modify the first or second list? \n"))
    if symt == 1:
        csym = read_sym("Companies")
    elif symt == 2:
        csym = read_sym("Commodities")
    print("Here is your current list of symbols: \n")
    print(csym)
    modifier = input("Do you wish to add or delete symbols?").lower()
    if modifier == "add":
        new_sym = input("Please enter the list of symbols you wish to add separated by spaces")
        new_sym = new_sym.split()
        write_sym(new_sym)
    elif modifier == "delete":
        del_sym = input("Please enter the list of symbols you wish to delete separated by spaces")
        del_sym = del_sym.split()
        write_sym(del_sym)
    