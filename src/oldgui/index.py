import tkinter as tk
from tkinter import ttk
from frame.map import getMapFrame

def main():
    root=tk.Tk()
    root.title('GUI')
    root.geometry('640x640')
    # root.resizable(False, False)
    # window.iconbitmap('icon.ico')
    # test = tk.Button(text="測試")
    # test.pack(side="top")
    mapFrame=getMapFrame()
    mapFrame.grid(column=1,row=1)
    # test=tk.Button(root,text="測試")
    # test.grid(column=2,row=1)

    root.mainloop()

if __name__=="__main__":
        main()