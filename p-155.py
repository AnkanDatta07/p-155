# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:15:44 2023

@author: Ankan Datta
"""

from tkinter import * 
import random
root = Tk()

root.title("RANDOM COLOURS USING DICTIONARY")
root.geometry("600x400")

dictionary = {"color" : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan","darkorange2","darkorchid1","chartreuse2","dodgerblue2",
                         "lightgrey","royalblue2","firebrick1","turquoise","indianred2","coral1","darkgoldenrod1","seagreen"]}

def random_bg_color(): 
    random_color = random.randint(0,20)
    print(dictionary["color"][random_color])
    root.configure(background = dictionary["color"][random_color])
    
btn = Button(root, text = "Click Me To Change The Background Color", command = random_bg_color)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()

