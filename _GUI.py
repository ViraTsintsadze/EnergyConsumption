from tkinter import *
from tkinter import filedialog
import os
import pandas as pd
import pickle
import numpy as np 

def Label_category(SAS_Variable_Name_str):
    cat = 'NotBtu'
    if 'EL' in SAS_Variable_Name_str:
        cat = 'EL'
    if 'KWH' in SAS_Variable_Name_str:
        cat = 'EL'
    if 'NG' in SAS_Variable_Name_str:
        cat = 'NG'
    if 'LP' in SAS_Variable_Name_str:
        cat = 'LP'
    if'FO' in SAS_Variable_Name_str:
        cat = 'FO'
    if 'TOTAL' in SAS_Variable_Name_str:
        cat = 'TOTAL'
    return cat   

## COLORS ##
Color0 = 'alice blue' #Ligtest
Color4 = 'SteelBlue4' #Darkest, more grey then blue
Color5 = 'peach puff' #yellow for text

x_to_pred = 0 #initiating

#codes : from SAS var name to Description
cokebook_file = 'codebook_for_Labels.xlsx'
path = os.getcwd()
pdCodebook = pd.read_excel(os.path.join(path,cokebook_file), delimiter=',', header=0)
pdVarDescr = pd.DataFrame(pdCodebook, columns = ['SAS Variable Name', 'Variable Description', 'Final Response Set', 'Error'])
pdVarDescr['Category'] = pdVarDescr['SAS Variable Name'].apply(Label_category)


window = Tk()
window.title("EnergyCons")
window.configure(background=Color0)


def prediction(x_to_pred, Label_to_predict, Path_to_Models):
    #load model
    filename =Label_to_predict+'_MLP.pickle'
    dbfile = open(os.path.join(Path_to_Models, filename), 'rb') 
    model = pickle.load(dbfile)                      
    dbfile.close()
    print(x_to_pred.shape)
    pred = int(np.round(model.predict(x_to_pred)[0])) #rounded prediction
    return pred

    
def buttonLoad_clicked(): #loads feature presets from csv files to pandas dataframe
    #open dialogue from where to load
    global x_to_pred 
    global pdFeatures
    loadpath = filedialog.askopenfile(filetypes=[("CSV Files",".csv")])
    pdFeatures = pd.read_csv(loadpath)
    x_to_pred = pdFeatures.to_numpy()
    return x_to_pred           
 
    
def Change_ResultListbox_Text():
    text_for_ResListbox = 'Prediction is '+ pred
    ResultListbox.delete(0, END)
    #put corresponding descriptions
    ResultListbox.insert(END, text_for_ResListbox)

def RBselection(): #called whenever radiobuts changed
    Categ = PredCateg.get()
    text_for_Listbox = pdVarDescr[pdVarDescr['Category']==Categ]['Variable Description']
    #clear the field
    Lb.delete(0, END)
    #put corresponding descriptions
    for line in text_for_Listbox:
        Lb.insert(END,line)

def buttonPredict_clicked():
    global pred
    
    #what label was choosen (from left menu)?
    picked = Lb.get(Lb.curselection())
    Label_to_predict = pdVarDescr['SAS Variable Name'].where(pdVarDescr['Variable Description']==picked).dropna().values[0]
    Path_to_Models=os.path.join(os.getcwd(),'Models') # folder Models in current directory, maybe i need to initiate it in __init__
    #if x_to_pred not loaded yet
    pred = str(prediction(x_to_pred, Label_to_predict, Path_to_Models))
    #add Error
    Error = int(np.round(pdVarDescr['Error'].where(pdVarDescr['Variable Description']==picked).dropna().values[0]))
    pred = pred +'\u00B1'+str(Error)+'%'
    #put it in the ResultListbox
    Change_ResultListbox_Text()
    return pred
    
  
    
## Left Panel ##
#Ask what to predict?
WhatPredLabel = Label(window,width=50, text='What would you like to predict?', fg = Color4, bg = Color0, font=('arial', 10, 'bold')).grid(column=0, row=0, columnspan=3) 
PredCateg = StringVar(value="BTUEL")

RbTOTAL = Radiobutton(window,text="Total", padx = 20, variable=PredCateg, value='TOTAL', bg = Color0
                      , command=RBselection)
RbTOTAL.grid(sticky="W", column=0, row=1)
RbTOTAL.select()
RbEL = Radiobutton(window,text="Electricity", padx = 20, variable=PredCateg, value='EL', bg = Color0
           , command=RBselection)
RbEL.grid(sticky="W", column=0, row=2)
RbNG = Radiobutton(window,text="Natural Gas", padx = 20, variable=PredCateg, value='NG', bg = Color0 , command=RBselection)
RbNG.grid(sticky="W", column=0, row=3)
RbLP = Radiobutton(window,text="Propane", padx = 20, variable=PredCateg, value='LP',bg = Color0, command=RBselection)
RbLP.grid(sticky="W", column=0, row=4)
RbFO = Radiobutton(window,text="Oil/Kerosene", padx = 20, variable=PredCateg, value='FO', bg = Color0, command=RBselection)
RbFO.grid(sticky="W", column=0, row=5)

scrollbar = Scrollbar(window, orient=VERTICAL)
Lb=Listbox(window, width=80,yscrollcommand=scrollbar.set)
scrollbar.config(command=Lb.yview)
Lb.grid(column=1, row=1, rowspan=7)
scrollbar.grid(column=2, row=1, rowspan=7)

Label(window, text='Scroll down to see more', bg = Color0).grid(column=1, row=8) 


## Right Panel ##
PARAMETLabel = Label(window,width=14, text='PARAMETERS', bg = Color0, fg = Color4, font=('arial', 10, 'bold')).grid(column=3, row=0)
buttonLoad=Button(window, width=15, text='Load', bg = Color4, fg = 'white', command=buttonLoad_clicked).grid(column=3, row=1)

buttonCreate=Button(window, text='RUN PREDICTION', font = ('arial', 10, 'bold'), command=buttonPredict_clicked, bg = Color4, fg = 'peach puff').grid(column=3, row=5)

ResultLabel = Label(window,width=20, text='RESULT', bg = Color0, fg = Color4 ,font=('arial', 10, 'bold')).grid(column=5, row=0)
ResultListbox=Listbox(window, width=50)
ResultListbox.grid(column=4, row=1, rowspan=5, columnspan=3)

window.mainloop()