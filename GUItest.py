import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import seaborn as sns

#import Test_tab.py as tt

from read_sym import read_sym
from write_sym import write_sym
from data_modernize import data_modernize
import os

#Testing intergration of the underlying structure and the GUI
#from symbol_update import update_symbol_list

"""For this classes are not the way to go as this version loops indefinitely
      and can be dynamically updated"""

"""Create the initial window instance"""
win = tk.Tk()

win.title("NASDAQ Analysis Engine")

"""Define any of the commands that the GUI will need to manage the symbol lists,
      manage data updates or manage data visualizations"""

def _quit():
    win.quit()
    win.destroy()


def show_rad():
    scr.delete('1.0', 'end')
    scr.insert(tk.INSERT, radVar.get())
    
def display_list():
    symt = radVar.get()
    
    csym = read_sym(symt)
    scr.delete('1.0', 'end')
    scr.insert(tk.INSERT, csym)
    
def update_symbol_list():
    """Get the company/commodity decision and the add/delete modifier"""
    symt = radVar.get()
    modifier = radMod.get()
    
    """Get the current list of NASDAQ symbols and split it by spaces"""
    csym = read_sym(symt)
    sym = symbols.get()
    sym = sym.split()
    
    """Modify the existing symbol list either adding or deleting the entered
          symbols"""
    write_sym(symt, sym, modifier)
    
    """Pull the new list of symbols and display it to the scrolling text box"""
    csym = read_sym(symt)
    scr.delete('1.0', 'end')
    scr.insert(tk.INSERT, csym)
    if symt == "Companies":
        Comp_scr.delete('1.0', 'end')
        Comp_scr.insert(tk.INSERT, csym)
    elif symt == "Commodities":
        Comm_scr.delete('1.0', 'end')
        Comm_scr.insert(tk.INSERT, csym)
        
        
"""---------------------------------------------------------------------------"""
    
def update_comp_data():
    """Since this set of functions aims to just update the data based on the 
          list of symbols there is no need to ask the user what they want to 
          do."""
    """First is retrieving the lists of company and commodity symbols"""
    Corpsym = read_sym("Companies")
    comp_bar["maximum"] = len(Corpsym)
    comp_status.configure(text = 'Update in progress')
    
    """Now that we have the symbol lists, we need to go through both lists 
          and update the data"""
    """Update_data function will check if the data file is empty or not.
          If empty, it will pull data from the start data to current and fill 
             in the file with it
          If not empty, the last date in the data will be retrieved and used 
             as the starting point"""
    for symbol in Corpsym:
        DocRoot = os.path.expanduser("~/Documents")
        Corp = "Companies/" + symbol + "_data/" + symbol + ".csv"
        CorpPath = os.path.join(DocRoot, Corp)
        data_modernize(symbol, CorpPath)
        comp_bar["value"] = Corpsym.index(symbol)+1
        comp_bar.update()
    comp_status.configure(text = "Update complete")
    

def update_comm_data():
    """Since this set of functions aims to just update the data based on the 
          list of symbols there is no need to ask the user what they want to 
          do."""
    """First is retrieving the lists of company and commodity symbols"""
    comm_status.configure(text = 'Update in progress')
    Comsym  = read_sym("Commodities")
    comm_bar["maximum"] = len(Comsym)
    """Now that we have the symbol lists, we need to go through both lists 
          and update the data"""
    """Update_data function will check if the data file is empty or not.
          If empty, it will pull data from the start data to current and fill 
             in the file with it
          If not empty, the last date in the data will be retrieved and used 
             as the starting point"""
    for symbol in Comsym:
        DocRoot = os.path.expanduser("~/Documents")
        Comm = "Commodities/" + symbol + "_data/" + symbol + ".csv"
        CommPath = os.path.join(DocRoot, Comm)
        data_modernize(symbol, CommPath)
        comm_bar["value"] = Comsym.index(symbol)+1
        comm_bar.update()
    comm_status.configure(text = "Update complete")
    
    
"""---------------------------------------------------------------------------"""    

def comp_vis():
    Symlist = read_sym("Companies")
    cpv_bar["maximum"] = len(Symlist)
    for symbol in Symlist:
        DocRoot = os.path.expanduser("~/Documents")
        Corp = "Companies/" + symbol + "_data/" + symbol + ".csv"
        CorpPath = os.path.join(DocRoot, Corp)
        data = pd.read_csv(CorpPath, index_col = 'formatted_date')
        data.index = pd.to_datetime(data.index, format = "")
        col_list = list(data.columns.values.tolist())
        for column in col_list:
            col_path = "Companies/" + symbol + "_data/" + symbol + "_"+ column + ".jpg"
            png_path = os.path.join(DocRoot, col_path)
            fig = plt.gcf()
            fig.set_size_inches((15, 11), forward = False)
            plt.grid()
            sns.lineplot(data = data[column])
            #plt.show()
            fig.savefig(png_path, dpi=1000)
            plt.clf()
        cpv_bar["value"] = Symlist.index(symbol)+1
        cpv_bar.update()


def comm_vis():
    Symlist = read_sym("Commodities")
    cmv_bar["maximum"] = len(Symlist)
    for symbol in Symlist:
        DocRoot = os.path.expanduser("~/Documents")
        Corp = "Commodities/" + symbol + "_data/" + symbol + ".csv"
        CorpPath = os.path.join(DocRoot, Corp)
        data = pd.read_csv(CorpPath, index_col = 'formatted_date')
        data.index = pd.to_datetime(data.index, format = "")
        col_list = list(data.columns.values.tolist())
        for column in col_list:
            col_path = "Commodities/" + symbol + "_data/" + symbol + "_"+ column + ".jpg"
            png_path = os.path.join(DocRoot, col_path)
            fig = plt.gcf()
            fig.set_size_inches((15, 11), forward = False)
            plt.grid()
            sns.lineplot(data = data[column])
            #plt.show()
            fig.savefig(png_path, dpi=1000)
            plt.clf()
        cmv_bar["value"] = Symlist.index(symbol)+1
        cmv_bar.update()

"""---------------------------------------------------------------------------"""


menu_bar = Menu(win)
win.configure(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

tabControl = ttk.Notebook(win)

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

rad3 = tk.Radiobutton(tab2, text = "Add", variable = radMod, value = "add")
rad3.grid(column = 0, row = 6, sticky=tk.W, columnspan = 3)

rad4 = tk.Radiobutton(tab2, text = "delete", variable = radMod, value = "delete")
rad4.grid(column = 3, row = 6, sticky=tk.W, columnspan = 3)

"""Add in a scrolling text box which will be used to display the company or
    commodity symbol list depending on the radial button choice above"""
scrol_w = 50
scrol_h = 4
scr = scrolledtext.ScrolledText(tab2, width = scrol_w, height = scrol_h, wrap=tk.WORD)
scr.grid(column = 0, row = 7, columnspan = 3)
#scr.set(radVar.get())
init_list = read_sym("Companies")
scr.insert(tk.INSERT,init_list)
#scr.configure(state='disabled')

"""Adding in the label and text box for adding/deleting symbols form the
    list displayed above"""
ttk.Label(tab2, text = "Enter symbols below with a space separating them").grid(column = 0, row = 8, sticky=tk.W, columnspan = 3)
symbols = tk.StringVar()
symb_enter = ttk.Entry(tab2, width = 12, textvariable=symbols)
symb_enter.grid(column=0, row = 9, sticky=tk.W)

disp_button = ttk.Button(tab2, text = "Display List", command = display_list)
disp_button.grid(column = 0, row = 10, sticky=tk.W)

cpcm = radVar.get()
ad = radMod.get()
ul_button = ttk.Button(tab2, text = "Update List", command = update_symbol_list)
ul_button.grid(column = 1, row = 10, sticky=tk.W)


 
"""----------------------------------------------------------------------------""" 

   
"""Adding in GUI for data update tab. This includes:
     Scrolling text boxes to display company and commodity symbol lists
     Buttons to initiate each of the updates
     Progress bars to track the update process"""

"""Adding in labels and the scrolling text boxes to display company and commodity symbol
      lists"""      
scrol_w = 30
scrol_h = 7
init_comp_list = read_sym("Companies")
comp_label = ttk.Label(tab3, text = "Company symbols")
comp_label.grid(column = 0, row = 0, sticky=tk.W)
Comp_scr = scrolledtext.ScrolledText(tab3, width = scrol_w, height = scrol_h, wrap = tk.WORD)
Comp_scr.grid(column = 0, row = 1, sticky = tk.W, rowspan = 3)
Comp_scr.insert(tk.INSERT, init_comp_list)

init_comm_list = read_sym("Commodities")
comm_label = ttk.Label(tab3, text = "Commodity symbols")
comm_label.grid(column = 0, row = 4, sticky = tk.W)
Comm_scr = scrolledtext.ScrolledText(tab3, width = scrol_w, height = scrol_h, wrap = tk.WORD)
Comm_scr.grid(column = 0, row = 5, sticky=tk.W, rowspan = 3)
Comm_scr.insert(tk.INSERT, init_comm_list)


"""Adding in the buttons to initiate the company and commodity updates"""
comp_update = ttk.Button(tab3, text = "Update Company Data", command = update_comp_data)
comp_update.grid(column = 2, row = 1)
comp_status = ttk.Label(tab3, text = "No update in progress")
comp_status.grid(column = 2, row = 2)

comm_update = ttk.Button(tab3, text = "Update Commodity Data", command = update_comm_data)
comm_update.grid(column = 2, row = 5)
comm_status = ttk.Label(tab3, text = "No update in progress")
comm_status.grid(column = 2, row = 6)

"""Adding in the progress bars for company and commodity update tracking"""
comp_bar = ttk.Progressbar(tab3, orient = "horizontal", length = 200, mode = 'determinate')
comp_bar.grid(column = 2, row = 3)

comm_bar = ttk.Progressbar(tab3, orient='horizontal', length = 200, mode = 'determinate')
comm_bar.grid(column = 2, row = 7)

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

comp_vis = ttk.Button(tab4, text = "Visualize Company Data", command = comp_vis)
comp_vis.grid(column = 2, row = 1)

comm_vis = ttk.Button(tab4, text = "VIsualize Commodity Data", command = comm_vis)
comm_vis.grid(column = 2, row = 4)

cpv_bar = ttk.Progressbar(tab4, orient="horizontal", length = 200, mode = 'determinate')
cpv_bar.grid(column = 2, row = 2)

cmv_bar = ttk.Progressbar(tab4, orient='horizontal', length = 200, mode = 'determinate')
cmv_bar.grid(column = 2, row = 5)

"""------------------------------------------------------------------------------"""
win.mainloop()
