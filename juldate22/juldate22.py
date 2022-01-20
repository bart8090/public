import tkinter as tk
import math
import calendar
from tkinter.ttk import Label
#from tkinter.ttk import Spinbox
from tkinter import ttk
import datetime
from datetime import date

# if console must be closed, start this python by: pythonw D:/bart/python/juldate22/juldate22.py

def set_sdx():
    if sdx['tdate'] == date.today():
        sdx['jul_fg'] = 'black'
    else:
        sdx['jul_fg'] = 'green'
    sdx['pdatelist'].append(sdx['tdate'])
    sdx['yy'] = sdx['tdate'].year
    sdx['mm'] = sdx['tdate'].month
    sdx['dd'] = sdx['tdate'].day
    mr = calendar.monthrange(sdx['yy'],sdx['mm'])
    sdx['month_startday'] = mr[0]
    sdx['month_nrdays'] = mr[1]
    if (sdx['mcecnt'] > sdx['pmcecnt']) and (sdx['mcecnt'] < 0):
        sdx['mcecnt'] = 0
    if (sdx['mcecnt'] < sdx['pmcecnt']) and (sdx['mcecnt'] > 0):
        sdx['mcecnt'] = 0
    sdx['pmcecnt'] = sdx['mcecnt']
    if sdx['mcecnt'] < 3:    
        sdx['monthupdate'] = sdx['tdate'] + datetime.timedelta(days=sdx['month_nrdays'])
    elif sdx['mcecnt'] < 6:
        sdx['monthupdate'] = sdx['tdate'] + datetime.timedelta(days=30*abs(sdx['mcecnt']))
    else:
        sdx['monthupdate'] = sdx['tdate'] + datetime.timedelta(days=90*abs(sdx['mcecnt']))
    pmonth = sdx['tdate'] - datetime.timedelta(days=(sdx['dd']))
    if sdx['mcecnt'] > -3:
        sdx['monthdowndate'] = sdx['tdate'] - datetime.timedelta(calendar.monthrange(pmonth.year,pmonth.month)[1])
    elif sdx['mcecnt'] >= -6:
        sdx['monthdowndate'] = sdx['tdate'] - datetime.timedelta(days=30*abs(sdx['mcecnt']))
    else:
        sdx['monthdowndate'] = sdx['tdate'] - datetime.timedelta(days=90*abs(sdx['mcecnt']))
    sdx['si'] = (7 - sdx['weekday'] + mr[0]) % 7
    sdx['tdateoffset'] = 6 + sdx['si'] + sdx['dd']
    sdx['butval'] = []
    sdx['datelist'] = []
    sdx['juldate'] = datetime.datetime(sdx['yy'],sdx['mm'],sdx['dd'],0,0).timetuple().tm_yday
    id = date(sdx['yy'],sdx['mm'],1)-datetime.timedelta(7+sdx['si'])
    ic = 0
    for i in range(sdx['weekday'],7):
        sdx['butval'].append(sdx['daylist'][i])
        sdx['datelist'].append(id+datetime.timedelta(days=ic))
        ic = ic+1
    for i in range(0,sdx['weekday']):
        sdx['butval'].append(sdx['daylist'][i])
        sdx['datelist'].append(id+datetime.timedelta(days=ic))
        ic = ic+1
    for i in range(sdx['si']):
        sdx['butval'].append(' ')
        sdx['datelist'].append(id+datetime.timedelta(days=ic))
        ic = ic+1
    for i in range(1,sdx['month_nrdays']+1):
        sdx['butval'].append(str(i))
        sdx['datelist'].append(id+datetime.timedelta(days=ic))
        ic = ic+1
    for i in range(ic,7*7):
        sdx['butval'].append(' ')
        sdx['datelist'].append(id+datetime.timedelta(days=ic))
        ic = ic+1

def butfiller():
    butlist[sdx['tdateoffset']].config(bg='skyblue') 
    i = 0
    for b in butlist:
        b.config(text=sdx['butval'][i])
        i = i + 1
    root.title(sdx['tdate'].strftime("%b %Y"))
    label.config(text=str(sdx['juldate']),font=("Helvetica", 74),foreground=sdx['jul_fg'])
    
def butfunction(event):
    sdx['mcecnt'] = 0
    butlist[sdx['tdateoffset']].config(bg='white') 
    if buttons[event.widget] < 7:
        sdx['weekday'] = (7 + buttons[event.widget] + sdx['weekday']) % 7
    else:
        sdx['tdate'] = sdx['datelist'][buttons[event.widget]]
    set_sdx()
    butfiller()

def month_up_clicked():
    sdx['tdate'] = sdx['monthupdate']
    sdx['mcecnt'] = sdx['mcecnt'] + 1
    butlist[sdx['tdateoffset']].config(bg='white')
    set_sdx()
    butfiller()

def month_down_clicked():
    sdx['tdate'] = sdx['monthdowndate']
    sdx['mcecnt'] = sdx['mcecnt'] - 1
    butlist[sdx['tdateoffset']].config(bg='white')
    set_sdx()
    butfiller()

def current_date_clicked():
    sdx['tdate'] = date.today()
    sdx['mcecnt'] = 0
    butlist[sdx['tdateoffset']].config(bg='white')
    set_sdx()
    butfiller()

def prev_date_clicked():
    if len(sdx['pdatelist']) > 1:
        trash = sdx['pdatelist'].pop()
        sdx['tdate'] = sdx['pdatelist'].pop()
    sdx['mcecnt'] = 0
    butlist[sdx['tdateoffset']].config(bg='white')
    set_sdx()
    butfiller()

tdate = date.today()
sdx = {'tdate' : tdate, 'weekday' : 0, 'pdatelist' : [tdate], 'daylist' : ['ma','di','wo','do','vr','za','zo'], 'mcecnt' : 0, 'pmcecnt' : 0}
set_sdx()

root = tk.Tk()
root.title(tdate.strftime("%b %Y"))
root.geometry('225x225')
root.configure(background='white')
buttons = {}
butlist = []
for i in range(7*7):
    b = tk.Button(root, text=sdx['butval'][i])
    buttons[b] = i 
    b.bind("<Button-1>", butfunction)
    c1 = 21 + ((i % 7) * 27)
    c2 = 113 + ((math.trunc(i / 7)) * 16)
    b.place(x=c1,y=c2)
    b.config(height=1, width=2, borderwidth=0, bg='white', font=("Helvetica", 7))
    butlist.append(b)
butlist[sdx['tdateoffset']].config(bg='skyblue') 

label = Label(root, background='white')
label.place(relx=0.5,rely=0.005,anchor='n')
label.config(text=str(sdx['juldate']),font=("Helvetica", 74))

month_up_icon = tk.PhotoImage(file='./juldate22/assets/bluedot15.png') 
month_up_button = ttk.Button(
    root,
    image=month_up_icon,
    command=month_up_clicked
)
month_up_button.place(x=190,y=0) 

month_down_icon = tk.PhotoImage(file='./juldate22/assets/bluedot15.png') 
month_down_button = ttk.Button(
    root,
    image=month_down_icon,
    command=month_down_clicked
)
month_down_button.place(x=5,y=0)

current_date_icon = tk.PhotoImage(file='./juldate22/assets/bluedot15.png') 
current_date_button = ttk.Button(
    root,
    image=current_date_icon,
    command=current_date_clicked
)
current_date_button.place(x=190,y=85)

prev_date_icon = tk.PhotoImage(file='./juldate22/assets/bluedot15.png') 
prev_date_button = ttk.Button(
    root,
    image=prev_date_icon,
    command=prev_date_clicked
)
prev_date_button.place(x=5,y=85)

root.mainloop()
