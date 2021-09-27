#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:16:31 2021

@author: michael
"""


import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#import Test_tab.py as tt

#Testing intergration of the underlying structure and the GUI
from symbol_update import update_symbol_list


class DATA_GUI():
    def __init__(self):
        self.win = tk.Tk()
        
        self.win.title("NASDAQ Analysis Engine")
        
        self.create_widgets()
        
    """def _quit():
        self.win.quit()
        self.win.destroy()  """  
        
    #def create_tab1(self):
        
    
    def create_widgets(self):
        menu_bar = Menu(self.win)
        self.win.configure(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.win.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        help_menu=Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")
        
        tabControl = ttk.Notebook(self.win)
        
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = "Main Menu")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = "Update Symbol List")
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text = "Update Data")
        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text = "Visualizer")
        tab5 = ttk.Frame(tabControl)
        tabControl.add(tab5, text = "Open Graph")
        
        tabControl.pack(expand=1, fill="both")
        
        a_label = ttk.Label(tab1, text="A label")
        a_label.grid(column=0, row=0)

        #tt.create_ListTab(self.win)
        
        """----------------------------------------------------------------------------------"""       
        

        """Adding in radial buttons to control whether the user is updating a company
              or a commodity, and whether they are adding or subtracting symbols from
              the list"""
        radVar = tk.StringVar()
        radMod = tk.StringVar()
        
        rad1 = tk.Radiobutton(tab2, text = "Companies", variable = radVar, value = "Companies")
        rad1.grid(column = 0, row = 5, sticky=tk.W, columnspan = 3)
        
        rad2 = tk.Radiobutton(tab2, text = "Commodities", variable = radVar, value = "Commodities")
        rad2.grid(column = 3, row = 5, sticky=tk.W, columnspan = 3)
        
        rad3 = tk.Radiobutton(tab2, text = "Add", variable = radMod, value = "Add")
        rad3.grid(column = 0, row = 6, sticky=tk.W, columnspan = 3)
        
        rad4 = tk.Radiobutton(tab2, text = "Delete", variable = radMod, value = "Delete")
        rad4.grid(column = 3, row = 6, sticky=tk.W, columnspan = 3)
        
        """Add in a scrolling text box which will be used to display the company or
            commodity symbol list depending on the radial button choice above"""
        scrol_w = 50
        scrol_h = 4
        scr = scrolledtext.ScrolledText(tab2, width = scrol_w, height = scrol_h, wrap=tk.WORD)
        scr.grid(column = 0, row = 7)
        scr.insert(tk.INSERT,"Place holder text for now")
        scr.configure(state='disabled')
        
        """Adding in the label and text box for adding/deleting symbols form the
            list displayed above"""
        ttk.Label(tab2, text = "Enter symbols below with a space separating them").grid(column = 0, row = 8, sticky=tk.W)
        symbols = tk.StringVar()
        symb_enter = ttk.Entry(tab2, width = 12, textvariable=symbols)
        symb_enter.grid(column=0, row = 9, sticky=tk.W)
        
        #cpcm = radVar.get()
        #ad = radMod.get()
        ul_button = ttk.Button(tab2, text = "Update List", command = update_symbol_list(radVar, radMod))
        ul_button.grid(column = 0, row = 10, sticky=tk.W)
        
        
        """----------------------------------------------------------------------------""" 

       
        """Adding in GUI for data update tab. This includes:
             Scrolling text boxes to display company and commodity symbol lists
             Buttons to initiate each of the updates
             Progress bars to track the update process"""

        """Adding in labels and the scrolling text boxes to display company and commodity symbol
              lists"""      
        scrol_w = 30
        scrol_h = 7
        comp_label = ttk.Label(tab3, text = "Company symbols")
        comp_label.grid(column = 0, row = 0, sticky=tk.W)
        Comp_scr = scrolledtext.ScrolledText(tab3, width = scrol_w, height = scrol_h, wrap = tk.WORD)
        Comp_scr.grid(column = 0, row = 1, sticky = tk.W)
        
        comm_label = ttk.Label(tab3, text = "Commodity symbols")
        comm_label.grid(column = 0, row = 3, sticky = tk.W)
        Comm_scr = scrolledtext.ScrolledText(tab3, width = scrol_w, height = scrol_h, wrap = tk.WORD)
        Comm_scr.grid(column = 0, row = 4, sticky=tk.W)
        
        
        """Adding in the buttons to initiate the company and commodity updates"""
        comp_update = ttk.Button(tab3, text = "Update Company Data")
        comp_update.grid(column = 2, row = 1)
        
        comm_update = ttk.Button(tab3, text = "Update Commodity Data")
        comm_update.grid(column = 2, row = 4)
        
        """Adding in the progress bars for company and commodity update tracking"""
        comp_bar = ttk.Progressbar(tab3, orient = "horizontal", length = 200, mode = 'determinate')
        comp_bar.grid(column = 2, row = 2)
        
        comm_bar = ttk.Progressbar(tab3, orient='horizontal', length = 200, mode = 'determinate')
        comm_bar.grid(column = 2, row = 5)
    
        """-------------------------------------------------------------------------------"""

        """Adding in GUI for data visualization. This includes:
              Scrolling text boxes to display the company and commodity symbol lists
              Button sto initiate the visualization
              Progress bars to track the update process"""
              
        vis_w = 30
        vis_h = 7
        Cpv_label = ttk.Label(tab4, text = "Company symbols")
        Cpv_label.grid(column = 0, row = 0, sticky=tk.W)
        comps = scrolledtext.ScrolledText(tab4, width = vis_w, height = vis_h, wrap = tk.WORD)
        comps.grid(column = 0, row = 1, sticky = tk.W)
        
        cmv_label = ttk.Label(tab4, text = "Commodity symbols")
        cmv_label.grid(column = 0, row = 3, sticky = tk.W)
        cmms = scrolledtext.ScrolledText(tab4, width = vis_w, height = vis_h, wrap = tk.WORD)
        cmms.grid(column = 0, row = 4, sticky = tk.W)
        
        comp_vis = ttk.Button(tab4, text = "Visualize Company Data")
        comp_vis.grid(column = 2, row = 1)
        
        comm_vis = ttk.Button(tab4, text = "VIsualize Commodity Data")
        comm_vis.grid(column = 2, row = 4)
        
        cpv_bar = ttk.Progressbar(tab4, orient="horizontal", length = 200, mode = 'determinate')
        cpv_bar.grid(column = 2, row = 2)
        
        cmv_bar = ttk.Progressbar(tab4, orient='horizontal', length = 200, mode = 'determinate')
        cmv_bar.grid(column = 2, row = 5)
        
        """------------------------------------------------------------------------------"""
        
        """Adding in the graph visualization for the 5th tab. This includes:
              A way to select the visualizations to display
              A screen to display the visualizations
              """
        """Initial testing will use a sample dataframe. Full impletmentation will
              utilize either pulling the data and then creating the figure or
              displaying the figure from already generated figures"""
              
        """Added in radial buttons to select the column and text input to select the
              company/commodity"""
              
        """Need to put in a way to see the symbol lists
           Adjust the size of the display
           Add in a way to select/specify the company/commodity displayed"""
              
        test_frame = ttk.Label(tab5, text = "Test_frame")
        test_frame.grid(column=0, row=4, columnspan = 5)
        colSel = tk.StringVar()
        columns = ['high', 'low', 'open', 'close', 'volume', 'adjclose']
        
        col_label = ttk.Label(tab5, text = "Data Columns")
        col_label.grid(column=0, row = 0, sticky=tk.W)
        
        col0 = tk.Radiobutton(tab5, text = columns[0], variable = colSel, value = columns[0])
        col0.grid(column=0, row = 1, sticky=tk.W)
        
        col1 = tk.Radiobutton(tab5, text = columns[1], variable = colSel, value = columns[1])
        col1.grid(column=1, row = 1, sticky=tk.W)
        
        col2 = tk.Radiobutton(tab5, text = columns[2], variable = colSel, value = columns[2])
        col2.grid(column=2, row = 1, sticky=tk.W)
        
        col3 = tk.Radiobutton(tab5, text = columns[3], variable = colSel, value = columns[3])
        col3.grid(column=3, row = 1, sticky=tk.W)
        
        col4 = tk.Radiobutton(tab5, text = columns[4], variable = colSel, value = columns[4])
        col4.grid(column=4, row = 1, sticky=tk.W)
              
        data1 = {'Country': ['US','CA','GER','UK','FR'],
                 'GDP_Per_Capita': [45000,42000,52000,49000,47000]
                }
        df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])
        
        
        data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
                 'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
                }
        df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])
        
        
        data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
                 'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
                }  
        df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])
        
        figure1 = plt.Figure(figsize=(6,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, test_frame)
        bar1.get_tk_widget().pack(side=tk.RIGHT, expand=False)
        df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
        
        """Here is where the data is plotted. I can modify it to take in the dataframe
              from the existing data for the columns and company/commodity selected 
              by the user"""
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Country Vs. GDP Per Capita')

        
oop = DATA_GUI()

oop.win.mainloop()