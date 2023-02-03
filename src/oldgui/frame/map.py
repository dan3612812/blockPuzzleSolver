import json
from typing import Callable
import tkinter as tk
from tkinter import Frame,Label,IntVar,Canvas,Text,BooleanVar
from tkinter.ttk import Combobox,Button
from comp.twoDButton import getTwoDButtonsFrame
from functools import partial

class Size():
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

def getMapFrame():
    # set variable
    xVar=IntVar()
    yVar=IntVar()
    xVar.set(0)
    yVar.set(0)
    tempTwoDButtonExists=BooleanVar()
    tempTwoDButtonExists.set(False)
    # twoDButton=None



    # set event
    def generateMapButtonClick():
        def hook():
            data = twoDButton.get2d()
            updateText(data)
        xVar.set(xBox.get())
        yVar.set(yBox.get())
        sizeLabel.config(text="地圖大小:%dx%d"%(xVar.get(),yVar.get()))
        # generateMapButton.config(text="重設地圖")
        twoDButton = getTwoDButtonsFrame(frame,Size(xVar.get(),yVar.get()),hook)
        twoDButton.grid(column=1,row=3)
        

    def updateText(t):
        print(t)
        text.delete(1.0,'end')
        text.insert(1.0,json.dumps(t))

    # declare
    frame=Frame(width=500,height=500,highlightbackground="black", highlightthickness=2)
    xLabel=Label(frame,text="地圖x軸:")
    yLabel=Label(frame,text="地圖y軸:")
    xBox = Combobox(frame,values=[x+1 for x in range(10)])
    yBox = Combobox(frame,values=[x+1 for x in range(10)])
    generateMapButton = Button(frame,text="產生地圖",command=generateMapButtonClick)
    sizeLabel = Label(frame,text="地圖大小:%dx%d"%(xVar.get(),yVar.get()))
    text=Text(frame,)
    

    # grid layout 
    xLabel.grid(column=0,row=0)
    xBox.grid(column=1,row=0)
    yLabel.grid(column=0,row=1)
    yBox.grid(column=1,row=1)
    generateMapButton.grid(column=2,row=0)
    sizeLabel.grid(column=2,row=1)
    text.grid(column=3,row=3)


    return frame