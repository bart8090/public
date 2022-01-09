import tkinter as tk
import math
import calendar
from tkinter.ttk import Label
#from tkinter.ttk import Spinbox
from tkinter import ttk
import datetime
from datetime import date

# if console must be closed, start this python by: pythonw D:/bart/python/juldate22/tkintersamp_v0.2.pyw

root = tk.Tk()
#print (root.configure().keys())
tdate = date.today()
root.title(tdate.strftime("%d %B %Y"))

def monthfil(yy,mm,weekday):
    mr = calendar.monthrange(yy,mm)
    si = (7 - weekday + mr[0]) % 7
    #print(mr[0],si,weekday,mr[1])
    daylist = ['ma','di','wo','do','vr','za','zo']
    result = []
    ic = 0
    for i in range(weekday,7):
        result.append(daylist[i])
        ic = ic+1
    for i in range(0,weekday):
        result.append(daylist[i])
        ic = ic+1
    for i in range(si):
        result.append(' ')
        ic = ic+1
    for i in range(1,mr[1]+1):
        result.append(str(i))
        ic = ic+1
    for i in range(ic,7*7):
        result.append(' ')
        ic = ic+1
    return result

def myfunction(event):
    print ("buttons[event.widget]",buttons[event.widget])
    print (event)
    #b.config(text=str(0))
    #event.widget.config(text=str(0))
    #b = butlist[buttons[event.widget]+5]
    #b.config(text=str(0))
    if buttons[event.widget] < 7:
        print(buttons[event.widget] , xwd)
        xwd[0] = (7 + buttons[event.widget] + xwd[0]) % 7
    vals = monthfil(xyy,xmm,xwd[0])
    i = 0
    for b in butlist:
        b.config(text=vals[i])
        i = i + 1
    dt = xwd[1]
    tt = dt.timetuple()
    #label.config(text=str(tt.tm_year)+ '  '+str(tt.tm_yday),font=("Helvetica", 34))
    label.config(text=str(tt.tm_yday),font=("Helvetica", 54))
    #label.config(text=str(buttons[event.widget]),font=("Helvetica", 24))

def year_up_clicked():
    print("year_up", xwd[2], xwd[2]+1)
    xwd[2] = xwd[2] +1

def year_down_clicked():
    print("year_down", xwd[2], xwd[2]-1)
    xwd[2] = xwd[2] -1

root.geometry('300x300')
buttons = {}
butlist = []
xyy = tdate.year
xmm = tdate.month
dt = datetime.datetime(xyy,xmm,1,0,0)
xwd = [0,dt,xyy,xmm]
vals = monthfil(xyy,xmm,xwd[0])
for i in range(7*7):
    b = tk.Button(root, text=vals[i])
    buttons[b] = i # save button, index as key-value pair
    b.bind("<Button-1>", myfunction)
    c1 = 40 + ((i % 7) * 30)
    c2 = 120 + ((math.trunc(i / 7)) * 30)
    #b.place(x=10,y=(10+(25*i)))
    b.place(x=c1,y=c2)
    b.config(height=1, width=2, borderwidth=0)
    #b.config(text=str(i))
    #print("loop : ",i,"buttons : ",buttons)
    butlist.append(b)

label = Label(root, text='This is a label')
label.place(x=40,y=10)

year_up_icon = tk.PhotoImage(file='D:/bart/python/juldate22/assets/up.png')
year_up_button = ttk.Button(
    root,
    image=year_up_icon,
    command=year_up_clicked
)
year_up_button.place(x=270,y=10)

year_down_icon = tk.PhotoImage(file='D:/bart/python/juldate22/assets/down.png')
year_down_button = ttk.Button(
    root,
    image=year_down_icon,
    command=year_down_clicked
)
year_down_button.place(x=270,y=40)

root.mainloop()
