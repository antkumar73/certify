# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:51:42 2020

@author: Anant Kumar
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:34:29 2020

@author: Anant Kumar
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:05:55 2020

@author: Anant Kumar
"""
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import pytesseract
from pytesseract import Output
import cv2
import os


root = tk.Tk()
root.title("Quix")
root.iconbitmap("Assets\Quix.ico")

li1= []
li2= []

W,H=(2000,1414)
HEIGHT=500
WIDTH=800


def selectFile():
    global datafile
    for widget in frame.winfo_children():
        widget.destroy()
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
                                         filetypes=(("executables","*.csv"),("all files", "*.*")))
    print(filename)
    li1.append(filename)
    for file in li1:
        label = tk.Label(frame, text= file, bg="grey")
        label.pack()
    datafile = os.path.basename(filename)
    print(datafile)
    return datafile
    
def selectTheme():
    global theme

    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
                                         filetypes=(("executables","*.png"),("all files", "*.*")))
    print(filename)
    li2.append(filename)
    for file in li2:
        label = tk.Label(frame, text= file, bg="grey")
        label.pack()
    theme = os.path.basename(filename)
    print(theme)
    return theme




def position():
    global c
    img = cv2.imread(theme)
    
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
   
     
    a= d["text"].index('presented') +1
    
    c=1414-d["left"][a]
    return c

def position1():
    global c
    img = cv2.imread(theme)
    
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    
     
    a= d["text"].index('securing') +1
   
    e=1414-d["left"][a]
    return e

def position2():
    global c
    img = cv2.imread(theme)
    
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    
     
    a= d["text"].index('securing') +1
   
    f=1414-d["left"][a]
    return f

def position3():
    global c
    img = cv2.imread(theme)
    
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    
     
    a= d["text"].index('securing') +1
   
    g=1414-d["left"][a]
    return g

W=2000
def createCertificate():
    df = pd.read_csv(datafile)
    
    n=0
    font1 = ImageFont.truetype('arial.ttf',75)
    font2 = ImageFont.truetype('arial.ttf',47)
    for index,j in df.iterrows():
        img = Image.open(theme)
        draw = ImageDraw.Draw(img)
        name='{}'.format(df['name'][n])
        pos='{}'.format(df['position'][n])
        event='{}'.format(df['event'][n])
        org='{}'.format(df['organizer'][n])
        x = (len(name)/2)*33
        y = (len(pos)/2)*75
        z = (len(event)/2)*50
        w = (len(org)/2)*20
        
        n=n+1
        draw.text(xy=((W/2-position()-x/2),721),text='{}'.format(j['name']),fill=(0,0,0),font=font1)
        draw.text(xy=((W/2-position1()+1.1*y),847.25),text='{}'.format(j['position']),fill=(0,0,0),font=font2)
        draw.text(xy=((W/2-position2()+(2*z)/3),919),text='{}'.format(j['event']),fill=(0,0,0),font=font2)
        draw.text(xy=((W/2-position3()+1.5*w),991),text='{}'.format(j['organizer']),fill=(0,0,0),font=font2)
        img.save('pictures/{}.png'.format(j['name']))
        

    
        
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#006064")
canvas.pack()

background_image= tk.PhotoImage(file='Assets\main.png')
background_label = tk.Label(root, image=background_image)
background_label.place( relwidth=1, relheight=1)

frame= tk.Frame(root, bg="#FFFDE7")
frame.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.25)

text=tk.Label(frame, text="Welcome to Quix\nYOU CAN CREATE THOUSANDS OF CERTIFICATES WITHIN SECONDS!")
text.pack()

openFile= tk.Button(root, text="open file", padx=10, pady=5, 
                    fg="white", bg="#C2185B", command=selectFile)
openFile.pack()

addTheme= tk.Button(root, text="Choose Theme", padx=10, pady=5, 
                    fg="white", bg="#E91E63", command=selectTheme)
addTheme.pack()

createCertficate= tk.Button(root, text="Create Certificate", padx=10, pady=5, 
                    fg="white", bg="#E91E10", command=createCertificate)
createCertficate.pack()



root.mainloop()