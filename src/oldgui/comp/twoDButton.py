from typing import List,Callable
from tkinter import Frame
from tkinter.ttk import Button

class Size():
    def __init__(self,x:int,y:int) -> None:
        self.x=x
        self.y=y

class MyButton(Button):
    def __init__(self,btnClickHook:Callable, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.value = True
        self.btnClickHook=btnClickHook
        self.bind("<Button-1>",self.click)
    
    def click(self,event):
        self.value = not self.value
        if self.value:
            self.config(text="")
        else:
            self.config(text="X")
        self.btnClickHook()
        

class MyFrame(Frame):
    def __init__(self,size:Size,btnHeight:int,btnHook:Callable, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.__x = size.x
        self.__y = size.y
        self.btnHeight=btnHeight
        self.twoD= [[None for i in range(self.__y)] for j in range(self.__x)] 
        for x in range(self.__x):
            for y in range(self.__y):
                self.twoD[x][y]=MyButton(btnHook,master=self,width=self.btnHeight)
                self.twoD[x][y].grid(column=x,row=y)

    def get2d(self)->List[List[bool]]:
        twoD= [[None for i in range(self.__y)] for j in range(self.__x)] 
        # twoD[self.__x][self.__y]
        for x in range(self.__x):
            for y in range(self.__y):
               twoD[x][y]= (self.twoD[x][y]).value
        return twoD

def getTwoDButtonsFrame(master,size:Size,btnClickHook:Callable,btnHeight:int=2):
    frame = MyFrame(size,btnHeight,btnClickHook,master=master)
    return frame