# -*- coding: utf-8 -*-
"""
Created on 12/03/2022

@author: userDCPS
"""


import tkinter as tk    
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
import pandas as pd
import numpy as np
from scipy import signal,stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

DEFAULT_BG_COLOR='#f1f0f1'

#_____________________________________________________________________________#
#_________________________________GLOBAL DEFS_________________________________#


# Fade Out Effect 
def fade_out(root):
    alpha = root.attributes("-alpha")
    if alpha > 0:
        alpha -= .1
        root.attributes("-alpha", alpha)
        root.after(100, lambda: fade_out(root))
    else:
        root.destroy()
        
# Defining style for all main boxes
def call_style():
    style = ttk.Style()
    style.theme_create('style', parent='alt', 
        settings = { 'TLabelframe': {
            'configure': {
                'background': DEFAULT_BG_COLOR,
                'relief': 'solid',
                'bordercolor': '#1c4366',
                # 'highlightcolor': 'black',
                # 'highlightbackground': 'black',
                'borderwidth': 2
            }
        },
        'TLabelframe.Label': {
            'configure': {
                'foreground': '#1c4366',
                'background': DEFAULT_BG_COLOR,
                'font': ('raleway', 11,'bold italic')
            }
        }
    })
    style.theme_use('style')
   
    
    return style

# Defining base layer for each menu option 
def base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width):
    # Criando Frame base
    frame = tk.Frame(master,bg='#1c4366')
    frame.place(relwidth=0.99,relheight=0.99,relx=0.005,rely=0.005)
    l_title = tk.Label(frame,text=title,bg='#1c4366',fg='white',
                        font = ('raleway', 20, 'italic bold'))
    l_title.place(relx=.5, rely=.04,anchor='center')
    
    frame = tk.Frame(frame, bg=DEFAULT_BG_COLOR)
    frame.place(relwidth=0.99,  # EAST
                relheight=0.91, # SOUTH
                relx=0.005,     # WEST
                rely=0.08)      # NORTH
    
    # Creating responsive frame 
    frame_responsive = tk.Frame(frame, bg=DEFAULT_BG_COLOR,
                                width=frame_responsive_width,
                                height=600)
    frame_responsive.pack()
    # canvas = tk.Canvas(frame, bg="blue", height=250, width=300)
    # canvas.pack()
    
    return frame_responsive

# Function for Welcome!>Info and when program starts.
def the_welcome(root):
    frame = tk.Frame(root,bg='#1c4366')
    frame.place(relwidth=0.99,relheight=0.99,relx=0.005,rely=0.005)
    l_title = tk.Label(frame,text='uniTIDE',bg='#1c4366',fg='white',
                        font=('raleway',60,'italic bold'))                   
    l_title.place(relx=.5, rely=.5,anchor='center')
    l_subtitle = tk.Label(frame,text='Designed for field and office needs.',
                          bg='#1c4366',fg='white',font=('raleway','9','italic'))
    l_subtitle.place(relx=.57, rely=.57,anchor='center')
    
    l_author = tk.Label(frame,text='@author: Diogo Silva <dceddiaps@protonmail.com>',
                        bg='#1c4366',fg='white')
    l_author.place(relx=.5, rely=.9,anchor='s')
    return None

# Help button of input box
def help_input_popup():
    
    # Layout
    root = tk.Toplevel()
    root.title('HINT - Input')
    root.geometry("400x500")
    root.lift()
    root.config(bg='#1c4366')
    frame = tk.Frame(root, bg='white')
    frame.place(relwidth=0.96,relheight=0.96,relx=0.02,rely=0.02)
    l_title = tk.Label(frame,text='How to Input Properly',
                       font=('raleway', 18, 'italic bold'),bg='white')
    l_title.pack(pady=10)
    
    # Info labels
    l_0 = tk.Label(frame,text='The software only needs date and heights measurements,\nnothing more!\n',
                   bg='white',font=('raleway', 10, 'italic'))
    l_0.pack()    
    
    l_1 = tk.Label(frame,text='Standard Date Format:',
                   bg='white',font=('raleway', 10, 'bold'))
    l_1.pack(anchor=tk.W)

    l_2 = tk.Label(frame,text='\tyyyy-mm-dd HH:MM:SS',
                   bg='white',font=('raleway', 10))
    l_2.pack(anchor=tk.W)    
       
    l_3 = tk.Label(frame,text='Skip Header Rows:',
                   font=('raleway', 10, 'bold'),bg='white')
    l_3.pack(anchor=tk.W)
    
    l_4 = tk.Label(frame,text='\tNumber of header rows to skip, from top to bottom.',
                   font=('raleway', 10,),bg='white')
    l_4.pack(anchor=tk.W)   

    l_5 = tk.Label(frame,text='Skip Footer Rows:',
                   font=('raleway', 10, 'bold'),bg='white')
    l_5.pack(anchor=tk.W)                
    
    l_6 = tk.Label(frame,text='\tNumber of footer rows to skip, from bottom to top.',
                   font=('raleway', 10,),bg='white')
    l_6.pack(anchor=tk.W)                      

    l_7 = tk.Label(frame,text='Date Column:',
                   font=('raleway', 10, 'bold'),bg='white')
    l_7.pack(anchor=tk.W)                
    
    l_8 = tk.Label(frame,text='\tIndex of the column with tide dates.',
                   font=('raleway', 10,),bg='white')
    l_8.pack(anchor=tk.W) 
    
    l_8a = tk.Label(frame,text='\tAll indexes start in 0.',
                   font=('raleway', 10,),bg='white')
    l_8a.pack(anchor=tk.W)     
    
    l_8b = tk.Label(frame,text='\tUsually, it is the first column of the data (index=0).',
                   font=('raleway', 10,),bg='white')
    l_8b.pack(anchor=tk.W)  

    l_9 = tk.Label(frame,text='Height Column:',
                   font=('raleway', 10, 'bold'),bg='white')
    l_9.pack(anchor=tk.W)                
    
    l_10 = tk.Label(frame,text='\tIndex of the column with tide heights.',
                   font=('raleway', 10,),bg='white')
    l_10.pack(anchor=tk.W)   

    l_10a = tk.Label(frame,text='\tAll indexes start in 0.',
                   font=('raleway', 10,),bg='white')
    l_10a.pack(anchor=tk.W)  

    l_10b = tk.Label(frame,text='\tUsually, it is the second column of the data (index=1).',
                   font=('raleway', 10,),bg='white')
    l_10b.pack(anchor=tk.W)  

    l_11 = tk.Label(frame,text='Delimiter:',
                   bg='white',font=('raleway', 10, 'bold'))
    l_11.pack(anchor=tk.W)

    l_12 = tk.Label(frame,text='\tDelimiter or separator, is the symbol between two',
                   bg='white',font=('raleway', 10))
    l_12.pack(anchor=tk.W)  
    
    l_12a = tk.Label(frame,text='\tdistinct and consecutive columns.',
                   bg='white',font=('raleway', 10))
    l_12a.pack(anchor=tk.W)     
    
# Help button of statistics box
def help_stat_popup():
        
    # Layout
    root = tk.Toplevel()
    root.title('Help - Statistics Box')
    root.geometry("400x500")
    root.lift()
    root.config(bg='#1c4366')
    frame = tk.Frame(root, bg='white')
    frame.place(relwidth=0.96,relheight=0.96,relx=0.02,rely=0.02)
    l_title = tk.Label(frame,text='Understanding the Statistics Box',
                        font=('raleway', 18, 'italic bold'),bg='white')
    l_title.pack(pady=10)
    
    # Info labels
    l_0 = tk.Label(frame,text='All statistics provided are relative to all data inputed.\n',
                    bg='white',font=('raleway', 10, 'italic'))
    l_0.pack()    

    l_1 = tk.Label(frame,text='Hmax or HAT (Highest Astronomical Tide):',
                   bg='white',font=('raleway', 10, 'bold'))
    l_1.pack(anchor=tk.W)

    l_2 = tk.Label(frame,text='\tMaximum tide height in all data.',
                   bg='white',font=('raleway', 10))
    l_2.pack(anchor=tk.W)    
    
    l_3 = tk.Label(frame,text='Hmin or LAT (Lowest Astronomical Tide):',
                   bg='white',font=('raleway', 10, 'bold'))
    l_3.pack(anchor=tk.W)

    l_4 = tk.Label(frame,text='\tMinimum tide height in all data.',
                   bg='white',font=('raleway', 10))
    l_4.pack(anchor=tk.W)    

    l_5 = tk.Label(frame,text='Hmean:',
                   bg='white',font=('raleway', 10, 'bold'))
    l_5.pack(anchor=tk.W)

    l_6 = tk.Label(frame,text='\tMean tide height of the data.',
                   bg='white',font=('raleway', 10))
    l_6.pack(anchor=tk.W) 

    l_6a = tk.Label(frame,text='\tIt is also know as MLS (Mean Sea Level) of all data.',
                   bg='white',font=('raleway', 10))
    l_6a.pack(anchor=tk.W) 

    l_8 = tk.Label(frame,text='Start:',
                   bg='white',font=('raleway', 10, 'bold'))
    l_8.pack(anchor=tk.W)

    l_9 = tk.Label(frame,text='\tThe moment in time when tide measurements started.',
                   bg='white',font=('raleway', 10))
    l_9.pack(anchor=tk.W) 

    l_9a = tk.Label(frame,text='\tOutputed: detetime vector: yyyy-mm-dd HH:MM:SS.',
                   bg='white',font=('raleway', 10))
    l_9a.pack(anchor=tk.W) 

    l_10 = tk.Label(frame,text='End:',
                   bg='white',font=('raleway', 10, 'bold'))
    l_10.pack(anchor=tk.W)

    l_11 = tk.Label(frame,text='\tThe moment in time when tide measurements ended.',
                   bg='white',font=('raleway', 10))
    l_11.pack(anchor=tk.W) 
   
    l_11a = tk.Label(frame,text='\tOutputed: detetime vector: yyyy-mm-dd HH:MM:SS.',
                   bg='white',font=('raleway', 10))
    l_11a.pack(anchor=tk.W) 
     
    l_12 = tk.Label(frame,text='Interval:',
                   bg='white',font=('raleway', 10, 'bold'))
    l_12.pack(anchor=tk.W)

    l_13 = tk.Label(frame,text='\tDifference in time between END and START.',
                   bg='white',font=('raleway', 10))
    l_13.pack(anchor=tk.W) 

    l_14 = tk.Label(frame,text='Sample Rate:',
                   bg='white',font=('raleway', 10, 'bold'))
    l_14.pack(anchor=tk.W)

    l_15 = tk.Label(frame,text='\tTime interval between tide measurements.',
                   bg='white',font=('raleway', 10))
    l_15.pack(anchor=tk.W) 
    
    
    return None    

# Help button for plots
def help_plot_popup():
    return None

# Help button for SAVE
def help_save_popup():
    return None

# Help button FFT
def help_fft_popup():
    return None

# Resample and save
def save_file(b_save,save_status,df,r_res,e_res_other):
    
    import scipy.interpolate
    
    try:
        cs = scipy.interpolate.CubicSpline(df.date,df.h, axis=0)
        
        if r_res.get() in [1,2,3,4]:
            # x = np.arange(np.datetime64(df.date.iloc[0]),np.datetime64(df.date.iloc[-1]), dt.timedelta(minutes=1))
            x = np.arange(df.date.iloc[0],df.date.iloc[-1], dt.timedelta(minutes=r_res.get()))
            x = pd.to_datetime(x)
            df_for_saving = pd.concat([pd.DataFrame(x),pd.DataFrame(cs(x))],axis=1)
        elif len(e_res_other.get()) == 0:
            tk.messagebox.showinfo('WARNING','You need to define the sample interval!')
    
        # Saving
        
        # Exiting try in a rude way xD
        print(df_for_saving)
        
        with filedialog.asksaveasfile(mode='w', filetypes = [('Text Document', '*.txt')],
                                      defaultextension=[".txt"]) as file:
            df_for_saving.to_csv(file.name, header=None, index=None, sep=',', mode='a')
            b_save.config(bg='Light green')
        save_status.config(text=f"File is saved in:\n{file.name}")
    except AttributeError:
        print("The user cancelled save")
        b_save.config(bg=DEFAULT_BG_COLOR)
 
# Layout of input/browse box.
def inpux_box(frame,box_name,x,y):
    
    lframe = ttk.LabelFrame(frame,text=box_name,labelanchor='n')
    # lframe = tk.LabelFrame(frame,text='Data Input',font=('raleway', 11,'bold italic'),fg='black')
    lframe.place(x=x,y=y,height=560,width=267)
    
    # Frame input parameters
    lframe_format = tk.LabelFrame(lframe,text='Input Parameters',labelanchor='n',
                                  font=('raleway', 10,'bold'),fg='#1c4366')
    lframe_format.place(x=3,y=5,width=257,height=115)
    
    # Skip header rows
    l_skip_hrows = tk.Label(lframe_format,text='Skip Header Rows: ')
    l_skip_hrows.place(x=0,y=8)
    e_skip_hrows = tk.Entry(lframe_format,width=3)
    e_skip_hrows.insert(0,"0")
    e_skip_hrows.place(x=110,y=10)

    # Skip footer rows
    l_skip_frows = tk.Label(lframe_format,text='Skip Footer Rows: ')
    l_skip_frows.place(x=0,y=28)
    e_skip_frows = tk.Entry(lframe_format,width=3)
    e_skip_frows.insert(0,"0")
    e_skip_frows.place(x=110,y=30)
    
    # Date column
    l_date_col = tk.Label(lframe_format,text='Date Column: ')
    l_date_col.place(x=0,y=48)
    e_date_col = tk.Entry(lframe_format,width=3)
    e_date_col.insert(0,"0")
    e_date_col.place(x=110,y=50) 
    
    # Height column
    l_h_col = tk.Label(lframe_format,text='Height Column: ')
    l_h_col.place(x=0,y=70)
    e_h_col = tk.Entry(lframe_format,width=3)
    e_h_col.insert(0,"1")
    e_h_col.place(x=110,y=70)
    
    # Frame Delimiter
    lframe_delimiter = tk.LabelFrame(lframe,text='Delimiter',labelanchor='n',fg='#1c4366',
                                  font=('raleway', 9,'bold'), padx=10,pady=10)    
    lframe_delimiter.place(x=150,y=25,width=105,height=75)
    
    # DEMILIMITER OPTIONS
    
    r = tk.IntVar()
    r.set('1')
    
    # Auto detect delimiter
    r_autodelim = tk.Radiobutton(lframe_delimiter,text='Auto Detect',variable=r,value=1,state='normal')
    r_autodelim.place(x=-6,y=-6)  

    # Delimiter OTHER
    r_other = tk.Radiobutton(lframe_delimiter,text='Other',variable=r,value=2)
    r_other.place(x=-6,y=15)  
    e_other = tk.Entry(lframe_delimiter,width=3)
    e_other.place(x=55,y=19)
    
    # Help input button
    b_help_input = tk.Button(lframe,text='?',font=('Rayleway','16','bold'),
                             fg='white',bg='#1c4366',
                             command = help_input_popup)
    b_help_input.place(x=239,y=-7,width=20,height=20)

    # Status do upload
    upload_status = tk.Label(lframe, text='<No file selected>',wraplength=254,width=36)
    upload_status.place(relx=0, y=165,x=3)

    # Statistics of inputted data
    #filling labels:
    lframe_stat = tk.LabelFrame(lframe,text='Statistics',labelanchor='n',
                                font=('raleway', 10,'bold'),fg='#1c4366')
    lframe_stat.place(x=3,y=390,height=145,width=257)
    l_stat_hmax = tk.Label(lframe_stat,text='Hmax:')
    l_stat_hmax.place(x=0,y=0)
    l_stat_hmin = tk.Label(lframe_stat,text='Hmin:')
    l_stat_hmin.place(x=0,y=17)
    l_stat_hmean = tk.Label(lframe_stat,text='Hmean:')
    l_stat_hmean.place(x=0,y=34)
    l_stat_startdate = tk.Label(lframe_stat,text='Start:')
    l_stat_startdate.place(x=0,y=51)
    l_stat_enddate = tk.Label(lframe_stat,text='End:')
    l_stat_enddate.place(x=0,y=68)
    l_stat_dateinterv = tk.Label(lframe_stat,text='Interval:')
    l_stat_dateinterv.place(x=0,y=85)
    l_stat_sf = tk.Label(lframe_stat,text='Sample Rate:')
    l_stat_sf.place(x=0,y=102)
    # Filling vals:
    l_stat_hmax_val = tk.Label(lframe_stat,text=' ')
    l_stat_hmax_val.place(x=85,y=0)
    l_stat_hmin_val = tk.Label(lframe_stat,text=' ')
    l_stat_hmin_val.place(x=85,y=17)
    l_stat_hmean_val = tk.Label(lframe_stat,text=' ')
    l_stat_hmean_val.place(x=85,y=34)
    l_stat_startdate_val = tk.Label(lframe_stat,text=' ')
    l_stat_startdate_val.place(x=85,y=51)
    l_stat_enddate_val = tk.Label(lframe_stat,text=' ')
    l_stat_enddate_val.place(x=85,y=68)
    l_stat_dateinterv_val = tk.Label(lframe_stat,text=' ')
    l_stat_dateinterv_val.place(x=85,y=85)
    l_stat_sf_val = tk.Label(lframe_stat,text=' ')
    l_stat_sf_val.place(x=85,y=102)
    
    # Help statistics button
    b_help_stat = tk.Button(lframe_stat,text='?',font=('Rayleway','16','bold'),
                            fg='white',bg='#1c4366',command = help_stat_popup)
    b_help_stat.place(x=232,y=-8,width=20,height=20)

    # Sumário do dado carregado
    _sum=tk.Text(lframe,font=('raleway', 9,), relief="sunken")
    _sum.insert(tk.INSERT,'<Your data will appear here!>')
    _sum.place(x=3,y=220,width=238,height=160)
    # Barra de rolagem do sumário
    vscroll = tk.Scrollbar(lframe, orient=tk.VERTICAL, command=_sum.yview)
    vscroll.place(in_=_sum, relx=1.015, relheight=1.0, bordermode="inside")
    _sum['yscroll'] = vscroll.set
    
    return lframe,e_skip_hrows,e_skip_frows,e_date_col,e_h_col,lframe_delimiter,r,e_other,upload_status,l_stat_hmax_val,l_stat_hmin_val,l_stat_hmean_val,l_stat_startdate_val,l_stat_enddate_val,l_stat_dateinterv_val,l_stat_sf_val,_sum                      

# Layout of plot box.
def plot_box(frame,x,y):
    
    plot_frame = ttk.LabelFrame(frame,text='Plot Options',labelanchor='n')
    plot_frame.place(x=x,y=y,height=238,width=267)

    # X-axis Units
    xunits_frame = tk.LabelFrame(plot_frame,text='Date Units',labelanchor='n',
                                 font=('raleway', 10,'bold'),fg='#1c4366')
    xunits_frame.place(x=3,y=5,height=88,width=127)
    # Radio buttons for X-axis Units
    r_xunits = tk.IntVar()
    r_xunits.set('2')
    # Julian days 
    r_julian = tk.Radiobutton(xunits_frame,text='Julian days',variable=r_xunits,value=1,state='disabled')
    r_julian.place(x=10,y=12)  
    # Datetime 
    r_dt = tk.Radiobutton(xunits_frame,text='Datetime',variable=r_xunits,value=2,state='disabled')
    r_dt.place(x=10,y=32)      
 
    # Y-axis Units
    yunits_frame = tk.LabelFrame(plot_frame,text='Height Units',labelanchor='n',
                                 font=('raleway', 10,'bold'),fg='#1c4366')
    yunits_frame.place(x=133,y=5,height=88,width=127)   
    # Radio buttons for Y-axis Units
    r_yunits = tk.IntVar()
    r_yunits.set('1')
    # Meters
    r_m = tk.Radiobutton(yunits_frame,text='Meters',variable=r_yunits,value=1,state='disabled')
    r_m.place(x=10,y=2)  
    # Feets 
    r_f = tk.Radiobutton(yunits_frame,text='Feets',variable=r_yunits,value=2,state='disabled')
    r_f.place(x=10,y=22)   
    # Other height unit
    r_o = tk.Radiobutton(yunits_frame,text='Other',variable=r_yunits,value=3,state='disabled')
    r_o.place(x=10,y=42)     
    # Other Entry
    e_o = tk.Entry(yunits_frame,width=7,state='disabled')
    e_o.place(x=70,y=44)

    # Mean sea level options
    msl_frame = tk.LabelFrame(plot_frame,text='Mean Sea Level',labelanchor='n',
                              font=('raleway', 10,'bold'),fg='#1c4366')
    msl_frame.place(x=3,y=100,height=70,width=257)
    # Checkboxes for MSL plottong options
    msl_y = tk.IntVar()
    msl_m = tk.IntVar()
    msl_d = tk.IntVar()
    msl_o = tk.IntVar()
    msl_all = tk.IntVar()
    cb_msl_y = tk.Checkbutton(msl_frame, text='Year',variable=msl_y, onvalue=1, offvalue=0,state='disabled')
    cb_msl_y.place(x=5,y=1)
    cb_msl_m = tk.Checkbutton(msl_frame, text='Month',variable=msl_m, onvalue=1, offvalue=0,state='disabled')
    cb_msl_m.place(x=90,y=1)
    cb_msl_d = tk.Checkbutton(msl_frame, text='Day',variable=msl_d, onvalue=1, offvalue=0,state='disabled')
    cb_msl_d.place(x=175,y=1)
    cb_msl_o = tk.Checkbutton(msl_frame, text='Other interval:',variable=msl_o, onvalue=1, offvalue=0,state='disabled')
    cb_msl_o.place(x=90,y=25)
    e_msl_o = tk.Entry(msl_frame,width=3,state='disabled')
    e_msl_o.place(x=194,y=27)
    l_msl_o = tk.Label(msl_frame,text='days')
    l_msl_o.place(x=216,y=27)
    cb_msl_all = tk.Checkbutton(msl_frame, text='All data',variable=msl_all, onvalue=1, offvalue=0,state='disabled')
    cb_msl_all.place(x=5,y=25) 
    msl_all.set(1)

    # Help PLOT OPTIONS button
    b_help_plot = tk.Button(plot_frame,text='?',font=('Rayleway','16','bold'),
                            fg='white',bg='#1c4366',command = help_plot_popup)
    b_help_plot.place(x=239,y=-7,width=20,height=20)  

    return plot_frame,xunits_frame,r_xunits,yunits_frame,r_yunits,msl_y,msl_m,msl_d,msl_o,msl_all,e_msl_o,r_julian,r_dt,r_m,r_f,r_o,e_o,cb_msl_y,cb_msl_m,cb_msl_d,cb_msl_o,cb_msl_all

# Layout of save box.
def save_box(frame,x,y):
    # Frame save
    frame_save = ttk.LabelFrame(frame,text='Save Options',labelanchor='n')
    frame_save.place(x=x,y=y,width=267,height=167)
    
    # Frame resample options
    frame_resamp = tk.LabelFrame(frame_save,text='Resample',labelanchor='n',
                                 font=('raleway', 10,'bold'),fg='#1c4366')
    frame_resamp.place(x=3,y=5,width=257,height=43)

    # Resample options
    r_res = tk.IntVar()
    r_res.set('1')
    # None
    r_res_none = tk.Radiobutton(frame_resamp,text='None',variable=r_res,value=1,state='disabled')
    r_res_none.place(x=3,y=-2)  
    # 1min
    r_res_1m = tk.Radiobutton(frame_resamp,text='1 min',variable=r_res,value=2,state='disabled')
    r_res_1m.place(x=63,y=-2)
    # 5min
    r_res_5m = tk.Radiobutton(frame_resamp,text='5 min',variable=r_res,value=3,state='disabled')
    r_res_5m.place(x=123,y=-2)    
    # Other
    r_res_other = tk.Radiobutton(frame_resamp,text=' ',variable=r_res,value=4,state='disabled')
    r_res_other.place(x=183,y=-2)
    e_res_other = tk.Entry(frame_resamp,width=3,state='disabled')
    e_res_other.place(x=203,y=0)
    l_res_other = tk.Label(frame_resamp,text='min')
    l_res_other.place(x=220,y=-2)

    # Status do save
    save_status = tk.Label(frame_save, text=' ',wraplength=260,width=36,
                           font=('Rayleway','9',))
    save_status.configure(anchor="center",bg=DEFAULT_BG_COLOR)
    save_status.place(x=2,y=89) 
    
    # Help button
    b_help_save = tk.Button(frame_save,text='?',font=('Rayleway','16','bold'),
                            fg='white',bg='#1c4366',command = help_save_popup)
    b_help_save.place(x=239,y=-7,width=20,height=20)     
    
    return frame_save,r_res,r_res_none,r_res_1m,r_res_5m,r_res_other,e_res_other,save_status

# Plot all
def plot_plot(file,
              df,
              r_xunits,
              r_yunits,
              e_o,
              msl_y,
              msl_m,
              msl_d,
              msl_o,
              e_msl_o,
              msl_all,
              bw=False):
    
    # Defining Y-axis units
    if r_yunits.get() == 1:
        units = 'm'
    elif r_yunits.get() == 2:
        units = 'ft'
    elif r_yunits.get() == 3:
        units = e_o.get()

    # Plot
    # for i in plt.style.available:
    # for i in ['seaborn','seaborn-white']:          
    plt.style.use('seaborn')
    # plt.style.available
    plt.figure("uniTIDE - Plot",figsize=(12,6))
    plt.title(file,fontweight="bold")
    plt.plot(df.date,df.h,label='Tide',color='black')

    # Sample rate
    rate = int(np.round(((df.date.max()-df.date.min())/len(df)).total_seconds()/60)) 

    # Plot custom interval MSL
    if msl_o.get()==1:
        ma_o = df.h.rolling(window=int(float(e_msl_o.get())*24*60/rate)).mean().dropna()
        plt.plot(df.date[:len(ma_o)],ma_o,label=f'MSL - {e_msl_o.get()} days')   
    
    # Plot dayly MSL           
    if msl_d.get()==1:
        ma_d = df.h.rolling(window=int(1*24*60/rate)).mean().dropna()
        plt.plot(df.date[:len(ma_d)],ma_d,label='MSL - day')

    # Plot monthly MSL
    if msl_m.get()==1:
        ma_m = df.h.rolling(window=int(30*24*60/rate)).mean().dropna()
        plt.plot(df.date[:len(ma_m)],ma_m,label='MSL - month')     
        
    # Plot yearly MSL
    if msl_y.get()==1:
        ma_y = df.h.rolling(window=int(365*24*60/rate)).mean().dropna()
        plt.plot(df.date[:len(ma_y)],ma_y,label='MSL - year')  

    # MSL - all data
    if msl_all.get()==1:
        plt.axhline(y=df.h.mean(),color='orange',
                    label=f'MSL - all data - {np.round(df.h.mean(),3)} {units}')
    
    
    # Adjusting X-axis depending on units.
    if r_xunits.get() == 1:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%j'))
        date_unit = 'Julian Days'
        plt.xlabel(date_unit + f' (year(s) = {np.unique(df.date.dt.year)})',fontweight="bold")
    if r_xunits.get() == 2:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d\n%H:%M'))
        date_unit = 'Datetime'
        plt.xlabel(date_unit,fontweight="bold")
        
    if bw==True:
        plt.plot(filtered_bw.date,filtered_bw[0],label='BW Filtered')
    
    plt.ylabel(f'Tide height ({units})',fontweight="bold")
    plt.legend(facecolor='white',framealpha=0.6,frameon=True,borderpad=1, edgecolor="black")
    plt.tight_layout()
    plt.grid('black')
    plt.show()
    
    # # Plotting KDE's
    # if msl_d.get()==1:
    #     plt.figure()
    #     plt.title(file + f' {i}')
    #     plt.xlabel(f'Mean Sea Level ({units})')
    #     if msl_m.get()==1:
    #         ma_m.plot.kde(color='orange',label='Monthly MSL')            
    #     ma_d.plot.kde(color='black',label='Dayly MSL')
    #     plt.legend()
    #     plt.grid('black')
    #     plt.show()
     
    return

# Export ASCII
def export_ascii(df_to_be_exported,button_export,save_status):
    try:
        with filedialog.asksaveasfile(mode='w', filetypes = [('Text Document', '*.txt')],
                                      defaultextension=[".txt"]) as file:
            df_to_be_exported.to_csv(file.name, header=None, index=None, sep=',', mode='a')
            button_export.config(bg='Light green')
        save_status.config(text=f"File is saved in:\n{file.name}")
    except AttributeError:
        print("The user cancelled save")
        button_export.config(bg=DEFAULT_BG_COLOR)

# Run Fast Fourier Transform
def run_fft(df,r_scale,b_export_fft,save_status,b_run_fft):
    
    global df_fft
    
    b_export_fft['state']='disabled'
    b_export_fft.config(bg=DEFAULT_BG_COLOR)
    save_status.config(text=' ')
    
    sample_freq = (df.date[1] - df.date[0]).total_seconds() # in seconds
    n_samples = len(df)
    
    # Applying FFT
    X = np.fft.fft(df.h)
    X[0] = 0
    freq = np.fft.fftfreq(len(X),d=sample_freq)
    X_mag = np.abs(X)
    X_mag = X_mag/(X_mag.max())
    if n_samples%2 != 0:
        freq = freq[0:int(n_samples/2+1)]
        X_mag = X_mag[0:int(n_samples/2+1)]
    else:
        freq = freq[0:int(n_samples/2)]
        X_mag = X_mag[0:int(n_samples/2)]

    # Plot
    plt.style.use('seaborn')
    plt.figure("uniTIDE - FFT",figsize=(12,6))
    plt.title(file,fontweight="bold")
    
    
    # Adjusting X-axis Scale
    t = (1/freq[1:])
    if r_scale.get()==1:
        scale='Hours'
        plt.xscale('log')
        # X_mag = X_mag[::-1]
        df_fft = pd.concat([pd.DataFrame(t/3600),pd.DataFrame(X_mag[1:])],axis=1)
        plt.plot(t/3600,X_mag[1:],color='black') #Avoid division by zero at frequency = 0 Hz
        # plt.xlim(480,0)
    if r_scale.get()==2:
        scale='Days'
        plt.xscale('log')
        # X_mag = X_mag[::-1]
        df_fft = pd.concat([pd.DataFrame(t/(3600*24)),pd.DataFrame(X_mag[1:])],axis=1)
        plt.plot(t/(3600*24),X_mag[1:],color='black') #Avoid division by zero at frequency = 0 Hz
        # plt.xlim(20,0)
    if r_scale.get()==3:
        scale='Hz'
        df_fft = pd.concat([pd.DataFrame(freq[1:]),pd.DataFrame(X_mag[1:])],axis=1)
        plt.plot(freq[1:],X_mag[1:],color='black')

    plt.xlabel(scale)
    # plt.axis(xmin=0)
    plt.ylabel('Magnitude')
    plt.tight_layout()
    plt.show()
    
    b_export_fft['state']='normal'
    b_run_fft.config(bg='light green')
    
    return



#_____________________________________________________________________________#
#________________________________PLOT TIDE DEFS_______________________________#


def upload_file_plot(label_sumario,
                     upload_status,
                     date_col,
                     h_col,
                     skipr,
                     skipf,
                     sep,
                     other_sep,
                     b_upload_plot,
                     l_stat_hmax_val,
                     l_stat_hmin_val,
                     l_stat_hmean_val,
                     l_stat_startdate_val,
                     l_stat_enddate_val,
                     l_stat_dateinterv_val,
                     l_stat_sf_val,
                     b_plot_plot,
                     r_julian,
                     r_dt,
                     r_m,
                     r_f,
                     r_o,
                     e_o,
                     cb_msl_y,
                     cb_msl_m,
                     cb_msl_d,
                     cb_msl_o,
                     e_msl_o,
                     cb_msl_all,
                     msl_y,
                     msl_m,
                     msl_d,
                     msl_o
):

    global df,file
    
    # Open dialog and display path in label
    file = filedialog.askopenfilename(filetypes=[('All',"*.*")])
    upload_status.config(text=file)
    
    # Unfill statistics 
    l_stat_hmax_val['text']= ' '
    l_stat_hmin_val['text']=' '
    l_stat_hmean_val['text']=' '
    l_stat_startdate_val['text']=' '
    l_stat_enddate_val['text']=' '
    l_stat_dateinterv_val['text']=' '
    l_stat_sf_val['text']=' '
    
    # Making all plot options disabled, since no file is inputed.
    b_plot_plot['state']='disabled'
    r_julian['state']='disabled'
    r_dt['state']='disabled'
    r_m['state']='disabled'
    r_f['state']='disabled'
    r_o['state']='disabled'
    e_o['state']='disabled'
    cb_msl_y['state']='disabled'
    cb_msl_m['state']='disabled'
    cb_msl_d['state']='disabled'
    cb_msl_o['state']='disabled'
    e_msl_o['state']='disabled'  
    cb_msl_all['state']='disabled'  
    msl_y.set(0)
    msl_m.set(0)
    msl_d.set(0)
    msl_o.set(0)
    e_msl_o.delete(0,tk.END)

    # Set browse button color to default
    b_upload_plot.config(bg=DEFAULT_BG_COLOR)
    
    # Delete any data preview information
    label_sumario.delete('0.0',tk.END)
    
    # Deleting old dataframe, if it exists.
    if 'df' in globals():
        del df
    
    # Tring to load data.
    try:
        # Defining separators/delimiters of *.txt
        if sep==1:
            sep=None
        else:
            sep=other_sep.get()
            
        # Load data
        cols_to_use = [int(date_col.get()),int(h_col.get())]
        df=pd.read_csv(file,engine='python',names=['date','h'],
                        skiprows= int(skipr.get()),
                        skipfooter= int(skipf.get()),
                        sep=sep,
                        usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]
    
        # Succed when delimiter is '\s{2,}' (two or more whitespaces).
        # This problem is expressed as heighs being times (00:00:00).
        if ':' in str(df.h[0]):
            df=pd.read_csv(file,engine='python',names=['date','h'],
                            skiprows= int(skipr.get()),
                            skipfooter= int(skipf.get()),
                            sep='\s{2,}',
                            usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]              
        else:
            pass
        
        # Converting dates to datetime vector and heights to floats.
        df.date = pd.to_datetime(df.date)
        df.h = df.h.astype("float")
        df.h = np.round(df.h,3)     # Don't need more than 3 decimals. It's tide.
        
        # Break try if there is any NaN
        if df['date'].isnull().sum() != 0:
            print(1/0)
        if df['h'].isnull().sum() != 0:
            print(1/0)
        
        # Upload successful!
        b_upload_plot.config(bg="Light green")
        b_plot_plot['state']='normal'
        r_julian['state']='normal'
        r_dt['state']='normal'
        r_m['state']='normal'
        r_f['state']='normal'
        r_o['state']='normal'
        e_o['state']='normal'
        
        # Enabling MSL buttons only when its possible to compute.
        if ((df.date.max()-df.date.min())>=dt.timedelta(days=364,hours=23,minutes=58)):
            cb_msl_y['state']='normal'
        if ((df.date.max()-df.date.min())>=dt.timedelta(days=30)):
            cb_msl_m['state']='normal'
        if ((df.date.max()-df.date.min())>=dt.timedelta(days=1)):
            cb_msl_d['state']='normal'
        cb_msl_o['state']='normal'
        e_msl_o['state']='normal'    
        cb_msl_all['state']='normal' 

        # Fill data preview
        label_sumario.delete('0.0',tk.END)
        label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------               
    {df}''')

        # Fill statistics 
        l_stat_hmax_val['text']=df.h.max()
        l_stat_hmin_val['text']=df.h.min()
        l_stat_hmean_val['text']=np.round(df.h.mean(),3)
        l_stat_startdate_val['text']=df.date.min()
        l_stat_enddate_val['text']=df.date.max()
        l_stat_dateinterv_val['text']=df.date.max()-df.date.min()
        l_stat_sf_val['text']=f'{np.round(((df.date.max()-df.date.min())/len(df)).total_seconds()/60,1)} minute(s)'

    except:
               
        # Clear data preview
        label_sumario.delete('0.0',tk.END)
        
        # If used closes browser window without selecting any file, it will return to first condition: '<No file selected>'
        if len(file)==0:
            label_sumario.insert(tk.INSERT,'<Your data will appear here!>')
            upload_status['text']='<No file selected>'
        # If data was loaded, but not as expected, raise error.
        else:
            tk.messagebox.showinfo('Input error','''Invalid input.\n\nCheck list:
> Is my file correct?
> Are there headers on my file?
> Are there footers on my file?
> Is the date column index correct?
> Is the height column index correct?
> Is the deliminter correct?''')
            label_sumario.insert(tk.INSERT,'Invalid input.\n')  
            if 'df' in globals():
                
                label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------

{df}''')    

    return None


#_____________________________________________________________________________#
#______________________________COMPARE TIDES DEFS_____________________________#




#_____________________________________________________________________________#
#_____________________________QUALITY CONTROL DEFS____________________________#

def upload_file_qc(label_sumario,
                     upload_status,
                     date_col,
                     h_col,
                     skipr,
                     skipf,
                     sep,
                     other_sep,
                     b_upload_qc,
                     l_stat_hmax_val,
                     l_stat_hmin_val,
                     l_stat_hmean_val,
                     l_stat_startdate_val,
                     l_stat_enddate_val,
                     l_stat_dateinterv_val,
                     l_stat_sf_val,
                     ):

    global df,file
    
    # Open dialog and display path in label
    file = filedialog.askopenfilename(filetypes=[('All',"*.*")])
    upload_status.config(text=file)
    
    # Unfill statistics 
    l_stat_hmax_val['text']= ' '
    l_stat_hmin_val['text']=' '
    l_stat_hmean_val['text']=' '
    l_stat_startdate_val['text']=' '
    l_stat_enddate_val['text']=' '
    l_stat_dateinterv_val['text']=' '
    l_stat_sf_val['text']=' '

    # Set browse button color to default
    b_upload_qc.config(bg=DEFAULT_BG_COLOR)

    
    # Delete any data preview information
    label_sumario.delete('0.0',tk.END)
    
    # Deleting old dataframe, if it exists.
    if 'df' in globals():
        del df
    
    # Tring to load data.
    try:
        # Defining separators/delimiters of *.txt
        if sep==1:
            sep=None
        else:
            sep=other_sep.get()
            
        # Load data
        cols_to_use = [int(date_col.get()),int(h_col.get())]
        df=pd.read_csv(file,engine='python',names=['date','h'],
                        skiprows= int(skipr.get()),
                        skipfooter= int(skipf.get()),
                        sep=sep,
                        usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]
    
        # Succed when delimiter is '\s{2,}' (two or more whitespaces).
        # This problem is expressed as heighs being times (00:00:00).
        if ':' in str(df.h[0]):
            df=pd.read_csv(file,engine='python',names=['date','h'],
                            skiprows= int(skipr.get()),
                            skipfooter= int(skipf.get()),
                            sep='\s{2,}',
                            usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]              
        else:
            pass
            
        # Converting dates to datetime vector and heights to floats.
        df.date = pd.to_datetime(df.date)
        df.h = df.h.astype("float")
        df.h = np.round(df.h,3)     # Don't need more than 3 decimals. It's tide.
        
        # Break try if there is any NaN
        if df['date'].isnull().sum() != 0:
            print(1/0)
        if df['h'].isnull().sum() != 0:
            print(1/0)
        
        # Upload successful!
        b_upload_qc.config(bg="Light green")

        # Fill data preview
        label_sumario.delete('0.0',tk.END)
        label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------               
    {df}''')

        # Fill statistics 
        l_stat_hmax_val['text']=df.h.max()
        l_stat_hmin_val['text']=df.h.min()
        l_stat_hmean_val['text']=np.round(df.h.mean(),3)
        l_stat_startdate_val['text']=df.date.max()
        l_stat_enddate_val['text']=df.date.min()
        l_stat_dateinterv_val['text']=df.date.max()-df.date.min()
        l_stat_sf_val['text']=f'{np.round(((df.date.max()-df.date.min())/len(df)).total_seconds()/60,1)} minute(s)'

    except:
               
        # Clear data preview
        label_sumario.delete('0.0',tk.END)
        
        # If used closes browser window without selecting any file, it will return to first condition: '<No file selected>'
        if len(file)==0:
            label_sumario.insert(tk.INSERT,'<Your data will appear here!>')
            upload_status['text']='<No file selected>'
        # If data was loaded, but not as expected, raise error.
        else:
            tk.messagebox.showinfo('Input error','''Invalid input.\n\nCheck list:
> Is my file correct?
> Are there headers on my file?
> Are there footers on my file?
> Is the date column index correct?
> Is the height column index correct?
> Is the deliminter correct?''')
            label_sumario.insert(tk.INSERT,'Invalid input.\n')  
            if 'df' in globals():
                label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------

{df}''')    

    return None


#_____________________________________________________________________________#
#___________________________BUTTLERWORTH FILTER DEFS__________________________#


def help_bw_popup():
    return None


def upload_file_bw(e_fs,
                   label_sumario,
                   upload_status, 
                   date_col, 
                   h_col, 
                   skipr, 
                   skipf, 
                   sep,
                   other_sep,
                   b_upload_bw,
                   b_run_bw,
                   b_plot_bw,
                   b_save,
                   e_cutoff,
                   e_order,
                   save_status,
                   l_stat_hmax_val,
                   l_stat_hmin_val,
                   l_stat_hmean_val,
                   l_stat_startdate_val,
                   l_stat_enddate_val,
                   l_stat_dateinterv_val,
                   l_stat_sf_val,
                   e_msl_o,
                   r_julian,
                   r_dt,
                   r_m,
                   r_f,
                   r_o,
                   e_o,
                   cb_msl_y,
                   cb_msl_m,
                   cb_msl_d,
                   cb_msl_o,
                   cb_msl_all,
                   r_res_none,
                   r_res_1m,
                   r_res_5m,
                   r_res_other,
                   e_res_other,
                   msl_y,
                   msl_m,
                   msl_d,
                   msl_o
                   ):
    
    """
    e_fs:           Sample Frequency Entry
    label_sumario:  Summary Label - data preview
    upload_status:  Label above Browse button that indicates Upload Status. At first it is <No file selected>.
    date_col:       Index of date 
    h_col:          Index of tide height
    skipr:          Header rows to skip (top to bottom)
    skipf:          Footer rows to skip (bottom to top)
    sep:            Separator or delimiter of *.txt
    other_sep:      Specify symbol of separator, when it is unusual 
    b_upload_bw:    Button that browse data
    b_run_bw:       Button that runs buttlerworth filter
    b_plot_bw:      Button that plots raw/filtered data.
    b_save:         Button that saves the new created file (in this case, bw filtered)
    e_cutoff:       Entry of the cut-off frequency for the bw filter. 
    e_order:        Entry that specifies the order of the bw filter.
    cb_btype:       Entry that specifies the bandpass type of the filter.
    save_status:    Print path of last file saved.
    
    """
    
    global df,file
    
    # Open dialog and display path in label
    file = filedialog.askopenfilename(filetypes=[('All',"*.*")])
    upload_status.config(text=file)

    # Unfill statistics 
    l_stat_hmax_val['text']= ' '
    l_stat_hmin_val['text']=' '
    l_stat_hmean_val['text']=' '
    l_stat_startdate_val['text']=' '
    l_stat_enddate_val['text']=' '
    l_stat_dateinterv_val['text']=' '
    l_stat_sf_val['text']=' '
    
    # Reseting bw filter buttons, entries and labels.
    b_run_bw['state'] = 'disabled'
    b_run_bw.config(bg=DEFAULT_BG_COLOR)
    b_plot_bw['state']='disabled'
    b_save['state']='disabled'
    b_save.config(bg=DEFAULT_BG_COLOR)
    save_status['text'] = ""
    e_fs.delete(0,tk.END)
    e_fs['state'] = 'disabled'
    e_cutoff.delete(0,tk.END)
    e_cutoff['state'] = 'disabled'
    e_order.delete(0,tk.END)
    e_order['state'] = 'disabled'
    e_msl_o['state'] = 'disabled'
    r_julian['state'] = 'disabled'
    r_dt['state'] = 'disabled'
    r_m['state'] = 'disabled'
    r_f['state'] = 'disabled'
    r_o['state'] = 'disabled'
    e_o['state'] = 'disabled'
    cb_msl_y['state'] = 'disabled'
    e_msl_o['text'] = " "
    cb_msl_m['state'] = 'disabled'
    cb_msl_d['state'] = 'disabled'
    cb_msl_o['state'] = 'disabled'
    cb_msl_all['state'] = 'disabled' 
    r_res_none['state'] = 'disabled'
    r_res_1m['state'] = 'disabled'
    r_res_5m['state'] = 'disabled'
    r_res_other['state'] = 'disabled'
    e_res_other['state'] = 'disabled'
    msl_y.set(0)
    msl_m.set(0)
    msl_d.set(0)
    msl_o.set(0)
    e_msl_o.delete(0,tk.END)

    # Delete any data preview information
    label_sumario.delete('0.0',tk.END)
    
    # Deleting old dataframe, if it exists.
    if 'df' in globals():
        del df
    
    # Tring to load data.
    try:
        # Defining separators/delimiters of *.txt
        if sep==1:
            sep=None
        else:
            sep=other_sep.get()
            
        # Load data
        cols_to_use = [int(date_col.get()),int(h_col.get())]
        df=pd.read_csv(file,engine='python',names=['date','h'],
                        skiprows= int(skipr.get()),
                        skipfooter= int(skipf.get()),
                        sep=sep,
                        usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]
    
        # Succed when delimiter is '\s{2,}' (two or more whitespaces).
        # This problem is expressed as heighs being times (00:00:00).
        if ':' in str(df.h[0]):
            df=pd.read_csv(file,engine='python',names=['date','h'],
                            skiprows= int(skipr.get()),
                            skipfooter= int(skipf.get()),
                            sep='\s{2,}',
                            usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]              
        else:
            pass
            
        # Converting dates to datetime vector and heights to floats.
        df.date = pd.to_datetime(df.date)
        df.h = df.h.astype("float")
        df.h = np.round(df.h,3)     # Don't need more than 3 decimals. It's tide.

        # Enabling filter parameters buttons. Everything is ok!
        b_run_bw['state'] = 'normal'
        e_fs['state'] = 'normal'
        e_cutoff['state'] = 'normal'
        e_order['state'] = 'normal'

        # Break try if there is any NaN
        if df['date'].isnull().sum() != 0:
            print(1/0)
        if df['h'].isnull().sum() != 0:
            print(1/0)

        # Upload successful!
        b_upload_bw.config(bg="Light green")
        
        # Fill sample frequency entry of bw filter
        e_fs.insert(0,np.round(((df.date.max()-df.date.min())/len(df)).total_seconds(),3))
        # Fill cut-off frequency suggestion
        e_cutoff.insert(0,np.round(((df.date.max()-df.date.min())/len(df)).total_seconds()/60))
        # Fill filter order suggestion
        e_order.insert(0,5)

        # Fill data preview
        label_sumario.delete('0.0',tk.END)
        label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------               
    {df}''')

        # Fill statistics 
        l_stat_hmax_val['text']=df.h.max()
        l_stat_hmin_val['text']=df.h.min()
        l_stat_hmean_val['text']=np.round(df.h.mean(),3)
        l_stat_startdate_val['text']=df.date.min()
        l_stat_enddate_val['text']=df.date.max()
        l_stat_dateinterv_val['text']=df.date.max()-df.date.min()
        l_stat_sf_val['text']=f'{np.round(((df.date.max()-df.date.min())/len(df)).total_seconds()/60,1)} minute(s)'


    except:
               
        # Clear data preview
        label_sumario.delete('0.0',tk.END)
        
        # If used closes browser window without selecting any file, it will return to first condition: '<No file selected>'
        if len(file)==0:
            label_sumario.insert(tk.INSERT,'<Your data will appear here!>')
            upload_status['text']='<No file selected>'
        # If data was loaded, but not as expected, raise error.
        else:
            tk.messagebox.showinfo('Input error','''Invalid input.\n\nCheck list:
> Is my file correct?
> Are there headers on my file?
> Are there footers on my file?
> Is the date column index correct?
> Is the height column index correct?
> Is the deliminter correct?''')
            label_sumario.insert(tk.INSERT,'Invalid input.\n')  
            if 'df' in globals():
                label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------

{df}''')    


def run_bw(df,
           fc,
           order,
           e_fs,
           b_run_bw,
           b_plot_bw,
           b_save,
           save_status,
           e_msl_o,
           r_julian,
           r_dt,
           r_m,
           r_f,
           r_o,
           e_o,
           cb_msl_y,
           cb_msl_m,
           cb_msl_d,
           cb_msl_o,
           cb_msl_all,
           r_res_none,
           r_res_1m,
           r_res_5m,
           r_res_other,
           e_res_other,
           ):
  
    global filtered_bw  
    
    # Disable every plot/save button, since filter is not applied yet.
    e_msl_o['state'] = 'disabled'
    r_julian['state'] = 'disabled'
    r_dt['state'] = 'disabled'
    r_m['state'] = 'disabled'
    r_f['state'] = 'disabled'
    r_o['state'] = 'disabled'
    e_o['state'] = 'disabled'
    cb_msl_y['state'] = 'disabled'
    cb_msl_m['state'] = 'disabled'
    cb_msl_d['state'] = 'disabled'
    cb_msl_o['state'] = 'disabled'
    cb_msl_all['state'] = 'disabled' 
    r_res_none['state'] = 'disabled'
    r_res_1m['state'] = 'disabled'
    r_res_5m['state'] = 'disabled'
    r_res_other['state'] = 'disabled'
    e_res_other['state'] = 'disabled'
    
    # Warning for users that forgot to fill any bw filter parameters.
    if len(e_fs)==0 or len(fc)==0 or len(order)==0:
        tk.messagebox.showinfo('WARNING','Please, set a value for all parameters!')
    
    elif int(float(fc))*2 >= int(float(e_fs)):
        tk.messagebox.showinfo('WARNING','The cut-off frequency should be < then half of sample frequency!')        
    
    else:
        # str to int
        e_fs = int(float(e_fs))
        fc = int(float(fc))
        order = int(float(order))
        
        # Appling bw filter when all parameters are set
        try:
            w = fc / (e_fs / 2) # Normalize the frequency
            b, a = signal.butter(int(order), w, 'lowpass')
            filtered_bw = np.round(signal.filtfilt(b, a, df.h),3)
            b_run_bw.config(bg='Light green')
            b_plot_bw['state']='normal'
            b_save['state']='normal'
            b_save.config(bg=DEFAULT_BG_COLOR)
            save_status['text'] = ""
            filtered_bw=pd.concat((df.date,pd.DataFrame(filtered_bw)),axis=1)
            
            # Filter applied! enable all plot/save options!
            e_msl_o['state'] = 'normal'
            r_julian['state'] = 'normal'
            r_dt['state'] = 'normal'
            r_m['state'] = 'normal'
            r_f['state'] = 'normal'
            r_o['state'] = 'normal'
            e_o['state'] = 'normal'
            cb_msl_o['state'] = 'normal'
            cb_msl_all['state'] = 'normal'
            r_res_none['state'] = 'normal'
            r_res_1m['state'] = 'normal'
            r_res_5m['state'] = 'normal'
            r_res_other['state'] = 'normal'
            e_res_other['state'] = 'normal'   
            # Enabling MSL buttons only when its possible to compute.
            if ((df.date.max()-df.date.min())>=dt.timedelta(days=364,hours=23,minutes=58)):
                cb_msl_y['state']='normal'
            if ((df.date.max()-df.date.min())>=dt.timedelta(days=30)):
                cb_msl_m['state']='normal'
            if ((df.date.max()-df.date.min())>=dt.timedelta(days=1)):
                cb_msl_d['state']='normal'
    
        except: 
            b_run_bw.config(bg=DEFAULT_BG_COLOR)
            b_plot_bw['state']='disabled'
            b_save['state']='disabled'
            b_save.config(bg=DEFAULT_BG_COLOR)
            save_status['text'] = ""
            

#_____________________________________________________________________________#
#________________________________RESAMPLE DEFS________________________________#


def upload_file_resample(label_sumario,
                     upload_status,
                     date_col,
                     h_col,
                     skipr,
                     skipf,
                     sep,
                     other_sep,
                     b_upload_resample,
                     l_stat_hmax_val,
                     l_stat_hmin_val,
                     l_stat_hmean_val,
                     l_stat_startdate_val,
                     l_stat_enddate_val,
                     l_stat_dateinterv_val,
                     l_stat_sf_val,
                     r_res_none,
                     r_res_1m,
                     r_res_5m,
                     r_res_other,
                     e_res_other,
                     b_save
                     ):

    global df,file
    
    # Open dialog and display path in label
    file = filedialog.askopenfilename(filetypes=[('All',"*.*")])
    upload_status.config(text=file)
    
    # Unfill statistics 
    l_stat_hmax_val['text']= ' '
    l_stat_hmin_val['text']=' '
    l_stat_hmean_val['text']=' '
    l_stat_startdate_val['text']=' '
    l_stat_enddate_val['text']=' '
    l_stat_dateinterv_val['text']=' '
    l_stat_sf_val['text']=' '

    # Reseting buttons
    r_res_none['state'] = 'disabled'
    r_res_1m['state'] = 'disabled'
    r_res_5m['state'] = 'disabled'
    r_res_other['state'] = 'disabled'
    e_res_other['state'] = 'disabled'
    b_save['state'] = 'disabled'

    # Set browse button color to default
    b_upload_resample.config(bg=DEFAULT_BG_COLOR)
    
    # Delete any data preview information
    label_sumario.delete('0.0',tk.END)
    
    # Deleting old dataframe, if it exists.
    if 'df' in globals():
        del df
    
    # Tring to load data.
    try:
        # Defining separators/delimiters of *.txt
        if sep==1:
            sep=None
        else:
            sep=other_sep.get()
            
        # Load data
        cols_to_use = [int(date_col.get()),int(h_col.get())]
        df=pd.read_csv(file,engine='python',names=['date','h'],
                        skiprows= int(skipr.get()),
                        skipfooter= int(skipf.get()),
                        sep=sep,
                        usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]
    
        # Succed when delimiter is '\s{2,}' (two or more whitespaces).
        # This problem is expressed as heighs being times (00:00:00).
        if ':' in str(df.h[0]):
            df=pd.read_csv(file,engine='python',names=['date','h'],
                            skiprows= int(skipr.get()),
                            skipfooter= int(skipf.get()),
                            sep='\s{2,}',
                            usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]              
        else:
            pass
            
        # Converting dates to datetime vector and heights to floats.
        df.date = pd.to_datetime(df.date)
        df.h = df.h.astype("float")
        df.h = np.round(df.h,3)     # Don't need more than 3 decimals. It's tide.

        # Break try if there is any NaN
        if df['date'].isnull().sum() != 0:
            print(1/0)
        if df['h'].isnull().sum() != 0:
            print(1/0)

        # Upload successful!
        b_upload_resample.config(bg="Light green")

        # Fill data preview
        label_sumario.delete('0.0',tk.END)
        label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------               
    {df}''')

        # Fill statistics 
        l_stat_hmax_val['text']=df.h.max()
        l_stat_hmin_val['text']=df.h.min()
        l_stat_hmean_val['text']=np.round(df.h.mean(),3)
        l_stat_startdate_val['text']=df.date.min()
        l_stat_enddate_val['text']=df.date.max()
        l_stat_dateinterv_val['text']=df.date.max()-df.date.min()
        l_stat_sf_val['text']=f'{np.round(((df.date.max()-df.date.min())/len(df)).total_seconds()/60,1)} minute(s)'
        
        # Enabling save buttons!
        r_res_none['state'] = 'normal'
        r_res_1m['state'] = 'normal'
        r_res_5m['state'] = 'normal'
        r_res_other['state'] = 'normal'
        e_res_other['state'] = 'normal'
        b_save['state'] = 'normal'

    except:
               
        # Clear data preview
        label_sumario.delete('0.0',tk.END)
        
        # If used closes browser window without selecting any file, it will return to first condition: '<No file selected>'
        if len(file)==0:
            label_sumario.insert(tk.INSERT,'<Your data will appear here!>')
            upload_status['text']='<No file selected>'
        # If data was loaded, but not as expected, raise error.
        else:
            tk.messagebox.showinfo('Input error','''Invalid input.\n\nCheck list:
> Is my file correct?
> Are there headers on my file?
> Are there footers on my file?
> Is the date column index correct?
> Is the height column index correct?
> Is the deliminter correct?''')
            label_sumario.insert(tk.INSERT,'Invalid input.\n')  
            if 'df' in globals():
                label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------

{df}''')    

    return None



#_____________________________________________________________________________#
#________________________________RESIDUALS DEFS_______________________________#


def upload_file_residuals(label_sumario,
                     upload_status,
                     date_col,
                     h_col,
                     skipr,
                     skipf,
                     sep,
                     other_sep,
                     b_upload_residuals,
                     l_stat_hmax_val,
                     l_stat_hmin_val,
                     l_stat_hmean_val,
                     l_stat_startdate_val,
                     l_stat_enddate_val,
                     l_stat_dateinterv_val,
                     l_stat_sf_val,
                     b_run_residuals,
                     b_export_residuals,
                     r_julian,
                     r_dt,
                     r_m,
                     r_f,
                     r_o,
                     e_o,
                     r_hours,
                     r_days,
                     r_hz,
                     b_export_residuals_fft,
                     b_run_residuals_fft,
                     save_status,
                     save_status_fft,
                     obs=False,
                     pre=False
                     ):

    # Doing global 
    if (obs==True) & (pre==False):
        global df_obs, file_obs
    if (obs==False) & (pre==True):
        global df_pre, file_pre
    
    global file
    
    # Open dialog and display path in label
    file = filedialog.askopenfilename(filetypes=[('All',"*.*")])
    upload_status.config(text=file)
    
    # Unfill statistics 
    l_stat_hmax_val['text']= ' '
    l_stat_hmin_val['text']=' '
    l_stat_hmean_val['text']=' '
    l_stat_startdate_val['text']=' '
    l_stat_enddate_val['text']=' '
    l_stat_dateinterv_val['text']=' '
    l_stat_sf_val['text']=' '

    # Disable all buttons
    b_run_residuals['state']='disabled'
    b_export_residuals['state']='disabled'
    r_julian['state']='disabled'
    r_dt['state']='disabled'
    r_m['state']='disabled'
    r_f['state']='disabled'
    r_o['state']='disabled'
    e_o['state']='disabled'
    r_hours['state']='disabled'
    r_days['state']='disabled'
    r_hz['state']='disabled'
    b_export_residuals_fft['state']='disabled'
    b_run_residuals_fft['state']='disabled'
    save_status['text']=' '
    save_status_fft['text']=' '
    b_export_residuals.config(bg=DEFAULT_BG_COLOR)
    b_export_residuals_fft.config(bg=DEFAULT_BG_COLOR)
    b_run_residuals.config(bg=DEFAULT_BG_COLOR)
    b_upload_residuals.config(bg=DEFAULT_BG_COLOR)
    b_run_residuals_fft.config(bg=DEFAULT_BG_COLOR)
    
    # Delete any data preview information
    label_sumario.delete('0.0',tk.END)

    # Deleting old dataframe, if it exists.
    # if ('df' in locals()) or ('df' in globals()):
    #     del df
    try:
        del df
    except:
        pass
    
    # Tring to load data.
    try:
        # Defining separators/delimiters of *.txt
        if sep==1:
            sep=None
        else:
            sep=other_sep.get()
            
        # Load data
        cols_to_use = [int(date_col.get()),int(h_col.get())]
        df=pd.read_csv(file,engine='python',names=['date','h'],
                        skiprows= int(skipr.get()),
                        skipfooter= int(skipf.get()),
                        sep=sep,
                        usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]
    
        # Succed when delimiter is '\s{2,}' (two or more whitespaces).
        # This problem is expressed as heighs being times (00:00:00).
        if ':' in str(df.h[0]):
            df=pd.read_csv(file,engine='python',names=['date','h'],
                            skiprows= int(skipr.get()),
                            skipfooter= int(skipf.get()),
                            sep='\s{2,}',
                            usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]              
        else:
            pass
            
        # Converting dates to datetime vector and heights to floats.
        df.date = pd.to_datetime(df.date)
        df.h = df.h.astype("float")
        df.h = np.round(df.h,3)     # Don't need more than 3 decimals. It's tide.

        # Break try if there is any NaN
        if df['date'].isnull().sum() != 0:
            print(1/0)
        if df['h'].isnull().sum() != 0:
            print(1/0)

        # Upload successful!
        b_upload_residuals.config(bg="Light green")

        # Fill data preview
        label_sumario.delete('0.0',tk.END)
        label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------               
    {df}''')

        # Fill statistics 
        l_stat_hmax_val['text']=df.h.max()
        l_stat_hmin_val['text']=df.h.min()
        l_stat_hmean_val['text']=np.round(df.h.mean(),3)
        l_stat_startdate_val['text']=df.date.min()
        l_stat_enddate_val['text']=df.date.max()
        l_stat_dateinterv_val['text']=df.date.max()-df.date.min()
        l_stat_sf_val['text']=f'{np.round(((df.date.max()-df.date.min())/len(df)).total_seconds()/60,1)} minute(s)'
        
        # Separating observed and predicted df's.
        if (obs==True) & (pre==False):
            df_obs = df
            file_obs = file
        if (obs==False) & (pre==True):
            df_pre = df
            file_pre = file    
        
        # Enable plot/export button if the observed and predicted data are uploaded.
        if (('df_obs' in locals()) or ('df_obs' in globals())) & (('df_pre' in locals()) or ('df_pre' in globals())):
            b_run_residuals['state']='normal'
            r_julian['state']='normal'
            r_dt['state']='normal'
            r_m['state']='normal'
            r_f['state']='normal'
            r_o['state']='normal'
            e_o['state']='normal'
        
        
    except:
               
        # Clear data preview
        label_sumario.delete('0.0',tk.END)
        
        # If used closes browser window without selecting any file, it will return to first condition: '<No file selected>'
        if len(file)==0:
            label_sumario.insert(tk.INSERT,'<Your data will appear here!>')
            upload_status['text']='<No file selected>'
        # If data was loaded, but not as expected, raise error.
        else:
            tk.messagebox.showinfo('Input error','''Invalid input.\n\nCheck list:
> Is my file correct?
> Are there headers on my file?
> Are there footers on my file?
> Is the date column index correct?
> Is the height column index correct?
> Is the deliminter correct?''')
            label_sumario.insert(tk.INSERT,'Invalid input.\n')  
            if 'df' in globals():
                label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------

{df}''')    

    return None


def run_residuals(df_obs,
                  df_pre,
                  r_yunits,
                  r_xunits,
                  e_o,
                  b_export_residuals,
                  b_export_residuals_fft,
                  b_run_residuals_fft,
                  r_hours,
                  r_days,
                  r_hz,
                  b_run_residuals,
                  save_status,
                  save_status_fft,):
    
    global df_to_export
    
    b_run_residuals_fft.config(bg=DEFAULT_BG_COLOR)
    save_status['text']=' '
    save_status_fft['text']=' '
    b_export_residuals.config(bg=DEFAULT_BG_COLOR)
    b_export_residuals_fft.config(bg=DEFAULT_BG_COLOR)
    b_export_residuals_fft['state']='disabled'
    
    resample_obs = df_obs.set_index('date').resample('1T').ffill().reset_index().dropna()
    resample_pre = df_pre.set_index('date').resample('1T').ffill().reset_index().dropna()
    df_residuals = (resample_obs-resample_pre).dropna()
    df_residuals.h = np.round(df_residuals.h,3)
    
    # Defining Y-axis units
    if r_yunits.get() == 1:
        units = 'm'
    elif r_yunits.get() == 2:
        units = 'ft'
    elif r_yunits.get() == 3:
        units = e_o.get()
    
    # Plot
    plt.style.use('seaborn')
    plt.figure('uniTIDE - Observed, Predicted and Residuals',figsize=(12,6))
    plt.title(f'$Observed$: {file_obs}\n$Predicted$: {file_pre}',fontweight='bold')
    plt.plot(resample_obs.date,resample_obs.h,label='Observed',linewidth=1)
    plt.plot(resample_pre.date,resample_pre.h,label='Predicted',linewidth=1)
    plt.plot(resample_obs.date,df_residuals.h,label='Residuals',linewidth=1)
    plt.xlim(resample_obs.date.min(),resample_obs.date.max())
    
    # Adjusting X-axis depending on units.
    if r_xunits.get() == 1:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%j'))
        date_unit = 'Julian Days'
        plt.xlabel(date_unit + f' (year(s) = {np.unique(df_obs.date.dt.year)})',fontweight="bold")
    if r_xunits.get() == 2:
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d\n%H:%M'))
        date_unit = 'Datetime'
        plt.xlabel(date_unit,fontweight="bold")
    
    plt.ylabel(f'Tide height ({units})',fontweight="bold")
    plt.legend(facecolor='white',framealpha=0.6,frameon=True,borderpad=1, edgecolor="black")
    plt.tight_layout()
    plt.show()
    
        
    # Plot residual frequency (KDE)
    plt.figure('uniTIDE - Residuals distribution')

    x,y = np.split(df_residuals.h.plot.kde().get_children()[0].get_path().vertices,2,1)

    text = f"Mean = {np.round(np.mean(y),3)} {units}\nMedian = {np.round(np.median(y),3)} {units}\nMode = {np.round(x[y.argmax()][0],3)} {units}\nStd = {np.round(np.std(y),3)} {units}"
    plt.text(0.65,
         0.75,
         text,
         transform=plt.gca().transAxes,
         bbox=dict(facecolor='blue',alpha=0.15,edgecolor='black',boxstyle='round'))


    plt.title(f'$Observed$: {file_obs}\n$Predicted$: {file_pre}',fontweight='bold')
    plt.xlim(np.mean(y)-3*np.std(y),
              np.mean(y)+3*np.std(y))
    plt.fill_between(np.ravel(x), np.ravel(y), 0,
                      # facecolor="orange", # The fill color
                      color='blue',       # The outline color
                      alpha=0.2)  
    plt.ylabel('Density (KDE)',fontweight="bold")
    plt.xlabel(f'Residual $(Observed - Predicted)$ ({units})',fontweight="bold")
    plt.show()

    # Creating df for export
    df_to_export = pd.concat([resample_obs.date,df_residuals.h],axis=1)

    # Enabling buttons   
    b_export_residuals['state'] = 'normal'
    b_run_residuals_fft['state'] = 'normal'
    r_hours['state'] = 'normal'
    r_days['state'] = 'normal'
    r_hz['state'] = 'normal'
    
    b_run_residuals.config(bg='light green')
    

    return



#_____________________________________________________________________________#
#_______________________SPECTRAL/HARMONIC ANALYSIS DEFS_______________________#


def upload_file_fft(label_sumario,
                     upload_status,
                     date_col,
                     h_col,
                     skipr,
                     skipf,
                     sep,
                     other_sep,
                     b_upload_fft,
                     l_stat_hmax_val,
                     l_stat_hmin_val,
                     l_stat_hmean_val,
                     l_stat_startdate_val,
                     l_stat_enddate_val,
                     l_stat_dateinterv_val,
                     l_stat_sf_val,
                     b_run_fft,
                     r_hours,
                     r_days,
                     r_hz,
                     b_export_fft,
                     save_status,
                     ):

    global df,file
    
    # Open dialog and display path in label
    file = filedialog.askopenfilename(filetypes=[('All',"*.*")])
    upload_status.config(text=file)
    
    # Unfill statistics 
    l_stat_hmax_val['text']= ' '
    l_stat_hmin_val['text']=' '
    l_stat_hmean_val['text']=' '
    l_stat_startdate_val['text']=' '
    l_stat_enddate_val['text']=' '
    l_stat_dateinterv_val['text']=' '
    l_stat_sf_val['text']=' '
    save_status.config(text=' ')

    # Disable all buttons, since FFT is not performed yet!
    b_run_fft['state'] = 'disabled'
    r_hours['state'] = 'disabled'
    r_days['state'] = 'disabled'
    r_hz['state'] = 'disabled'
    b_export_fft['state'] = 'disabled'
    b_export_fft.config(bg=DEFAULT_BG_COLOR)
    b_run_fft.config(bg=DEFAULT_BG_COLOR)

    # Set browse button color to default
    b_upload_fft.config(bg=DEFAULT_BG_COLOR)

    # Deleting old dataframe, if it exists.
    if 'df' in globals():
        del df
    
    # Delete any data preview information
    label_sumario.delete('0.0',tk.END)
    
    # Tring to load data.
    try:
        # Defining separators/delimiters of *.txt
        if sep==1:
            sep=None
        else:
            sep=other_sep.get()
            
        # Load data
        cols_to_use = [int(date_col.get()),int(h_col.get())]
        df=pd.read_csv(file,engine='python',names=['date','h'],
                        skiprows= int(skipr.get()),
                        skipfooter= int(skipf.get()),
                        sep=sep,
                        usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]
    
        # Succed when delimiter is '\s{2,}' (two or more whitespaces).
        # This problem is expressed as heighs being times (00:00:00).
        if ':' in str(df.h[0]):
            df=pd.read_csv(file,engine='python',names=['date','h'],
                            skiprows= int(skipr.get()),
                            skipfooter= int(skipf.get()),
                            sep='\s{2,}',
                            usecols=(cols_to_use)).iloc[:, np.argsort(cols_to_use)]              
        else:
            pass
            
        # Converting dates to datetime vector and heights to floats.
        df.date = pd.to_datetime(df.date)
        df.h = df.h.astype("float")
        df.h = np.round(df.h,3)     # Don't need more than 3 decimals. It's tide.

        # Break try if there is any NaN
        if df['date'].isnull().sum() != 0:
            print(1/0)
        if df['h'].isnull().sum() != 0:
            print(1/0)

        # Upload successful!
        b_upload_fft.config(bg="Light green")
        
        # Fill data preview
        label_sumario.delete('0.0',tk.END)
        label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------               
    {df}''')

        # Fill statistics 
        l_stat_hmax_val['text']=df.h.max()
        l_stat_hmin_val['text']=df.h.min()
        l_stat_hmean_val['text']=np.round(df.h.mean(),3)
        l_stat_startdate_val['text']=df.date.min()
        l_stat_enddate_val['text']=df.date.max()
        l_stat_dateinterv_val['text']=df.date.max()-df.date.min()
        l_stat_sf_val['text']=f'{np.round(((df.date.max()-df.date.min())/len(df)).total_seconds()/60,1)} minute(s)'

        # Load successful! Enable all FFT buttons!
        b_run_fft['state'] = 'normal'
        r_hours['state'] = 'normal'
        r_days['state'] = 'normal'
        r_hz['state'] = 'normal'

    except:
               
        # Clear data preview
        label_sumario.delete('0.0',tk.END)
        
        # If used closes browser window without selecting any file, it will return to first condition: '<No file selected>'
        if len(file)==0:
            label_sumario.insert(tk.INSERT,'<Your data will appear here!>')
            upload_status['text']='<No file selected>'
        # If data was loaded, but not as expected, raise error.
        else:
            tk.messagebox.showinfo('Input error','''Invalid input.\n\nCheck list:
> Is my file correct?
> Are there headers on my file?
> Are there footers on my file?
> Is the date column index correct?
> Is the height column index correct?
> Is the deliminter correct?''')
            label_sumario.insert(tk.INSERT,'Invalid input.\n')  
            if 'df' in globals():
                label_sumario.insert(tk.INSERT,f'''----------------------------------------------------------
                                Preview:               
----------------------------------------------------------

{df}''')    

    return None



'''_________________________________________________________________________'''
'''___________________________________FRAMES________________________________'''


def info_frame():
    
    # Resize master window
    # master.geometry("566x633")
       
    frame = tk.Frame(master,bg='#1c4366').pack()
    the_welcome(frame)
    
    return None



def documentation_frame():
    
    return None



def plot_frame():

    global df
    DEFAULT_BG_COLOR='#f1f0f1'
    
    # Resize master window
    # master.geometry("566x633")

    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Plot tide'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)
    
    # Layout imput/browse 
    x = 5
    y = 5
    box_name = 'Data Input'
    lframe,e_skip_hrows,e_skip_frows,e_date_col,e_h_col,lframe_delimiter,r,e_other,upload_status,l_stat_hmax_val,l_stat_hmin_val,l_stat_hmean_val,l_stat_startdate_val,l_stat_enddate_val,l_stat_dateinterv_val,l_stat_sf_val,_sum = inpux_box(frame,box_name,x,y,)

    # Layout plot
    x=280
    y=5
    plot_frame,xunits_frame,r_xunits,yunits_frame,r_yunits,msl_y,msl_m,msl_d,msl_o,msl_all,e_msl_o,r_julian,r_dt,r_m,r_f,r_o,e_o,cb_msl_y,cb_msl_m,cb_msl_d,cb_msl_o,cb_msl_all=plot_box(frame,x,y)

    # Botão upload
    b_upload_plot = tk.Button(lframe, text='Browse file', font=('raleway', 10,'bold'),
                          fg = 'black',borderwidth=4,width=6,padx=73,pady=4,bg=DEFAULT_BG_COLOR,
                          command = lambda:upload_file_plot(label_sumario=_sum,
                                                      upload_status=upload_status,
                                                      date_col=e_date_col,
                                                      h_col=e_h_col,
                                                      skipr=e_skip_hrows,
                                                      skipf=e_skip_frows,
                                                      sep=int(r.get()),
                                                      other_sep=e_other,
                                                      b_upload_plot=b_upload_plot,
                                                      l_stat_hmax_val=l_stat_hmax_val,
                                                      l_stat_hmin_val=l_stat_hmin_val,
                                                      l_stat_hmean_val=l_stat_hmean_val,
                                                      l_stat_startdate_val=l_stat_startdate_val,
                                                      l_stat_enddate_val=l_stat_enddate_val,
                                                      l_stat_dateinterv_val=l_stat_dateinterv_val,
                                                      l_stat_sf_val=l_stat_sf_val,
                                                      b_plot_plot=b_plot_plot,
                                                      r_julian=r_julian,
                                                      r_dt=r_dt,
                                                      r_m=r_m,
                                                      r_f=r_f,
                                                      r_o=r_o,
                                                      e_o=e_o,
                                                      cb_msl_y=cb_msl_y,
                                                      cb_msl_m=cb_msl_m,
                                                      cb_msl_d=cb_msl_d,
                                                      cb_msl_o=cb_msl_o,
                                                      e_msl_o=e_msl_o,
                                                      cb_msl_all=cb_msl_all,
                                                      msl_y=msl_y,
                                                      msl_m=msl_m,
                                                      msl_d=msl_d,
                                                      msl_o=msl_o,
                                                      ))
    b_upload_plot.configure(anchor="center")
    b_upload_plot.place(relx=.5, y=145,anchor='center')

    # Botão de plot
    b_plot_plot = tk.Button(plot_frame,text='Plot Results',width=6,fg = 'black',font=('raleway', 10,'bold'),
                   padx=73,pady=4,borderwidth=4,bg=DEFAULT_BG_COLOR,
                   command=lambda:plot_plot(file=file,
                                            df=df,
                                            r_xunits=r_xunits,
                                            r_yunits=r_yunits,
                                            e_o=e_o,
                                            msl_y=msl_y,
                                            msl_m=msl_m,
                                            msl_d=msl_d,
                                            msl_o=msl_o,
                                            e_msl_o=e_msl_o,
                                            msl_all=msl_all
                                            ))
    b_plot_plot.place(x=28,y=174)
    b_plot_plot['state'] = tk.DISABLED



def compare_frame():

    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window
    # master.geometry("566x633")

    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Compare Tides'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)



def qc_frame():

    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window
    # master.geometry("566x633")

    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Quality Control'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)
    
    # Layout input/browse file
    x = 5
    y = 5
    box_name = 'Data Input'
    lframe,e_skip_hrows,e_skip_frows,e_date_col,e_h_col,lframe_delimiter,r,e_other,upload_status,l_stat_hmax_val,l_stat_hmin_val,l_stat_hmean_val,l_stat_startdate_val,l_stat_enddate_val,l_stat_dateinterv_val,l_stat_sf_val,_sum = inpux_box(frame,box_name,x,y)

    # Botão upload
    b_upload_qc = tk.Button(lframe, text='Browse file', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,
                          command = lambda:upload_file_qc(label_sumario=_sum,
                                                      upload_status=upload_status,
                                                      date_col=e_date_col,
                                                      h_col=e_h_col,
                                                      skipr=e_skip_hrows,
                                                      skipf=e_skip_frows,
                                                      sep=int(r.get()),
                                                      other_sep=e_other,
                                                      b_upload_qc=b_upload_qc,
                                                      l_stat_hmax_val=l_stat_hmax_val,
                                                      l_stat_hmin_val=l_stat_hmin_val,
                                                      l_stat_hmean_val=l_stat_hmean_val,
                                                      l_stat_startdate_val=l_stat_startdate_val,
                                                      l_stat_enddate_val=l_stat_enddate_val,
                                                      l_stat_dateinterv_val=l_stat_dateinterv_val,
                                                      l_stat_sf_val=l_stat_sf_val,
                                                      ))
    b_upload_qc.configure(anchor="center")
    b_upload_qc.place(relx=.5, y=145,anchor='center')



def bw_frame():
    
    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window
    # master.geometry("566x633")

    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Buttlerworth filter'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)

    # Layout upload/browse file
    x = 5
    y = 5
    box_name = 'Data Input'
    lframe,e_skip_hrows,e_skip_frows,e_date_col,e_h_col,lframe_delimiter,r,e_other,upload_status,l_stat_hmax_val,l_stat_hmin_val,l_stat_hmean_val,l_stat_startdate_val,l_stat_enddate_val,l_stat_dateinterv_val,l_stat_sf_val,_sum = inpux_box(frame,box_name,x,y)

    # Layout plot
    x=280
    y=150
    plot_frame,xunits_frame,r_xunits,yunits_frame,r_yunits,msl_y,msl_m,msl_d,msl_o,msl_all,e_msl_o,r_julian,r_dt,r_m,r_f,r_o,e_o,cb_msl_y,cb_msl_m,cb_msl_d,cb_msl_o,cb_msl_all=plot_box(frame,x,y)

    # Layout save
    x=280
    y=398    
    frame_save,r_res,r_res_none,r_res_1m,r_res_5m,r_res_other,e_res_other,save_status = save_box(frame,x,y)

    # Botão de salvar
    b_save = tk.Button(frame_save,text='Save File',width=6,fg = 'black',font=('raleway', 10,'bold'),
                    padx=73,pady=4,borderwidth=4,bg=DEFAULT_BG_COLOR,
                    command=lambda: save_file(b_save,
                                              save_status,
                                              df=filtered_bw,
                                              r_res=r_res,
                                              e_res_other=e_res_other))
    b_save.place(x=28,y=51)
    b_save['state'] = tk.DISABLED

    # Botão upload
    b_upload_bw = tk.Button(lframe, text='Browse file', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,
                          bg=DEFAULT_BG_COLOR,
                          command = lambda:upload_file_bw(label_sumario=_sum,
                                                      upload_status=upload_status,
                                                      e_fs = e_fs,
                                                      date_col=e_date_col,
                                                      h_col=e_h_col,
                                                      skipr=e_skip_hrows,
                                                      skipf=e_skip_frows,
                                                      sep=int(r.get()),
                                                      other_sep=e_other,
                                                      b_upload_bw=b_upload_bw,
                                                      b_run_bw = b_run_bw,
                                                      b_plot_bw=b_plot_bw,
                                                      b_save=b_save,
                                                      e_cutoff=e_cutoff,
                                                      e_order=e_order,
                                                      save_status=save_status,
                                                      l_stat_hmax_val=l_stat_hmax_val,
                                                      l_stat_hmin_val=l_stat_hmin_val,
                                                      l_stat_hmean_val=l_stat_hmean_val,
                                                      l_stat_startdate_val=l_stat_startdate_val,
                                                      l_stat_enddate_val=l_stat_enddate_val,
                                                      l_stat_dateinterv_val=l_stat_dateinterv_val,
                                                      l_stat_sf_val=l_stat_sf_val,
                                                      e_msl_o=e_msl_o,
                                                      r_julian=r_julian,
                                                      r_dt=r_dt,
                                                      r_m=r_m,
                                                      r_f=r_f,
                                                      r_o=r_o,
                                                      e_o=e_o,
                                                      cb_msl_y=cb_msl_y,
                                                      cb_msl_m=cb_msl_m,
                                                      cb_msl_d=cb_msl_d,
                                                      cb_msl_o=cb_msl_o,
                                                      cb_msl_all=cb_msl_all,
                                                      r_res_none=r_res_none,
                                                      r_res_1m=r_res_1m,
                                                      r_res_5m=r_res_5m,
                                                      r_res_other=r_res_other,
                                                      e_res_other=e_res_other,
                                                      msl_y=msl_y,
                                                      msl_m=msl_m,
                                                      msl_d=msl_d,
                                                      msl_o=msl_o
                                                      ))
    b_upload_bw.configure(anchor="center")
    b_upload_bw.place(relx=.5, y=145,anchor='center')
    
    # Botão de plot
    b_plot_bw = tk.Button(plot_frame,text='Plot Results',width=6,fg = 'black',font=('raleway', 10,'bold'),
                    padx=73,pady=4,borderwidth=4,bg=DEFAULT_BG_COLOR,
                    command=lambda: plot_plot(file,
                                              df,
                                              r_xunits,
                                              r_yunits,
                                              e_o,
                                              msl_y,
                                              msl_m,
                                              msl_d,
                                              msl_o,
                                              e_msl_o,
                                              msl_all,
                                              bw=True))
    b_plot_bw.place(x=28,y=173)
    b_plot_bw['state'] = tk.DISABLED
    
    
##### Buttlerworth filter!#####################################################
    
    frame_bw = ttk.LabelFrame(frame,text='Filtering Parameters',labelanchor='n')
    frame_bw.place(x=280,y=5,height=135,width=267)
    
    # LABEL/ENTRY FS
    l_fs = tk.Label(frame_bw,text='Sampling Frequency: ')
    l_fs.place(x=10,y=4)
    e_fs = tk.Entry(frame_bw,width=7)
    e_fs['state'] = 'disabled'
    e_fs.place(x=133,y=6)
    l_fs_units = tk.Label(frame_bw,text='Hz')
    l_fs_units.place(x=179,y=4)

    # LABEL/ENTRY CUTOFF
    l_cutoff = tk.Label(frame_bw,text='Cut-off Frequency: ')
    l_cutoff.place(x=10,y=24)
    e_cutoff = tk.Entry(frame_bw,width=7)
    e_cutoff['state'] = 'disabled'
    e_cutoff.place(x=133,y=26)
    l_cutoff_units = tk.Label(frame_bw,text='Hz')
    l_cutoff_units.place(x=179,y=24)
    
    # LABEL/ENTRY FILTER ORDER
    l_order = tk.Label(frame_bw,text='Filter Order: ')
    l_order.place(x=10,y=44)
    e_order = tk.Entry(frame_bw,width=7)
    e_order['state'] = 'disabled'
    e_order.place(x=133,y=47)    

    # Help BW button
    b_help_bw = tk.Button(frame_bw,text='?',font=('Rayleway','16','bold'),
                            fg='white',bg='#1c4366',command = help_bw_popup)
    b_help_bw.place(x=242,y=-7,width=20,height=20) 
    
    # Botão de run filter
    b_run_bw = tk.Button(frame_bw,text='Run Filter',width=6,fg = 'black',font=('raleway', 10,'bold'),
                   padx=73,pady=4,borderwidth=4,bg=DEFAULT_BG_COLOR,
                   command= lambda: run_bw(df=df,
                                           e_fs=e_fs.get(),
                                           fc=e_cutoff.get(),
                                           order=e_order.get(),
                                           b_run_bw=b_run_bw,
                                           b_plot_bw=b_plot_bw,
                                           b_save=b_save,
                                           save_status=save_status,
                                           e_msl_o=e_msl_o,
                                           r_julian=r_julian,
                                           r_dt=r_dt,
                                           r_m=r_m,
                                           r_f=r_f,
                                           r_o=r_o,
                                           e_o=e_o,
                                           cb_msl_y=cb_msl_y,
                                           cb_msl_m=cb_msl_m,
                                           cb_msl_d=cb_msl_d,
                                           cb_msl_o=cb_msl_o,
                                           cb_msl_all=cb_msl_all,
                                           r_res_none=r_res_none,
                                           r_res_1m=r_res_1m,
                                           r_res_5m=r_res_5m,
                                           r_res_other=r_res_other,
                                           e_res_other=e_res_other,
                                           ))
    b_run_bw.place(x=30,y=70)
    b_run_bw['state'] = tk.DISABLED


    return None



def resample_frame():

    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window
    # master.geometry("566x633")

    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Resample'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)
    
    # Layout input/browse  
    x = 5
    y = 5
    box_name = 'Data Input'
    lframe,e_skip_hrows,e_skip_frows,e_date_col,e_h_col,lframe_delimiter,r,e_other,upload_status,l_stat_hmax_val,l_stat_hmin_val,l_stat_hmean_val,l_stat_startdate_val,l_stat_enddate_val,l_stat_dateinterv_val,l_stat_sf_val,_sum = inpux_box(frame,box_name,x,y)

    # Layout save
    x=280
    y=5    
    frame_save,r_res,r_res_none,r_res_1m,r_res_5m,r_res_other,e_res_other,save_status = save_box(frame,x,y)    

    # Botão upload
    b_upload_resample = tk.Button(lframe, text='Browse file', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,bg=DEFAULT_BG_COLOR,
                          command = lambda:upload_file_resample(label_sumario=_sum,
                                                      upload_status=upload_status,
                                                      date_col=e_date_col,
                                                      h_col=e_h_col,
                                                      skipr=e_skip_hrows,
                                                      skipf=e_skip_frows,
                                                      sep=int(r.get()),
                                                      other_sep=e_other,
                                                      b_upload_resample=b_upload_resample,
                                                      l_stat_hmax_val=l_stat_hmax_val,
                                                      l_stat_hmin_val=l_stat_hmin_val,
                                                      l_stat_hmean_val=l_stat_hmean_val,
                                                      l_stat_startdate_val=l_stat_startdate_val,
                                                      l_stat_enddate_val=l_stat_enddate_val,
                                                      l_stat_dateinterv_val=l_stat_dateinterv_val,
                                                      l_stat_sf_val=l_stat_sf_val,
                                                      r_res_none=r_res_none,
                                                      r_res_1m=r_res_1m,
                                                      r_res_5m=r_res_5m,
                                                      r_res_other=r_res_other,
                                                      e_res_other=e_res_other,
                                                      b_save=b_save
                                                      ))
    b_upload_resample.configure(anchor="center")
    b_upload_resample.place(relx=.5, y=145,anchor='center')

    # Botão de salvar
    b_save = tk.Button(frame_save,text='Save File',width=6,fg = 'black',font=('raleway', 10,'bold'),
                    padx=73,pady=4,borderwidth=4,bg=DEFAULT_BG_COLOR,
                    command=lambda: save_file(b_save,
                                              save_status,
                                              df=df,
                                              r_res=r_res,
                                              e_res_other=e_res_other))
    b_save.place(x=28,y=51)
    b_save['state'] = tk.DISABLED



def residuals_frame():

    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window in case user changed the size
    master.geometry("843x633")

    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Residuals'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=826)

    # Layout input/browse OBSERVED
    x = 5
    y = 5
    box_name = 'Data Input (OBSERVED)'
    lframe,e_skip_hrows,e_skip_frows,e_date_col,e_h_col,lframe_delimiter,r,e_other,upload_status,l_stat_hmax_val,l_stat_hmin_val,l_stat_hmean_val,l_stat_startdate_val,l_stat_enddate_val,l_stat_dateinterv_val,l_stat_sf_val,_sum = inpux_box(frame,box_name,x,y)

    # Layout input/browse PREVISTA
    x = 280
    y = 5
    box_name = 'Data Input (PREDICTED)'
    lframe2,e_skip_hrows2,e_skip_frows2,e_date_col2,e_h_col2,lframe_delimiter2,r2,e_other2,upload_status2,l_stat_hmax_val2,l_stat_hmin_val2,l_stat_hmean_val2,l_stat_startdate_val2,l_stat_enddate_val2,l_stat_dateinterv_val2,l_stat_sf_val2,_sum2 = inpux_box(frame,box_name,x,y)

    # Botão upload OBSERVADA
    b_upload_residuals_OBS = tk.Button(lframe, text='Browse file', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,
                          command = lambda:upload_file_residuals(label_sumario=_sum,
                                                      upload_status=upload_status,
                                                      date_col=e_date_col,
                                                      h_col=e_h_col,
                                                      skipr=e_skip_hrows,
                                                      skipf=e_skip_frows,
                                                      sep=int(r.get()),
                                                      other_sep=e_other,
                                                      b_upload_residuals=b_upload_residuals_OBS,
                                                      l_stat_hmax_val=l_stat_hmax_val,
                                                      l_stat_hmin_val=l_stat_hmin_val,
                                                      l_stat_hmean_val=l_stat_hmean_val,
                                                      l_stat_startdate_val=l_stat_startdate_val,
                                                      l_stat_enddate_val=l_stat_enddate_val,
                                                      l_stat_dateinterv_val=l_stat_dateinterv_val,
                                                      l_stat_sf_val=l_stat_sf_val,
                                                      b_run_residuals=b_run_residuals,
                                                      b_export_residuals=b_export_residuals,
                                                      r_julian=r_julian,
                                                      r_dt=r_dt,
                                                      r_m=r_m,
                                                      r_f=r_f,
                                                      r_o=r_o,
                                                      e_o=e_o,
                                                      r_hours=r_hours,
                                                      r_days=r_days,
                                                      r_hz=r_hz,
                                                      b_export_residuals_fft=b_export_residuals_fft,
                                                      b_run_residuals_fft=b_run_residuals_fft,
                                                      save_status=save_status,
                                                      save_status_fft=save_status_fft,
                                                      obs = True,
                                                      pre = False
                                                      ))
    b_upload_residuals_OBS.configure(anchor="center")
    b_upload_residuals_OBS.place(relx=.5, y=145,anchor='center')

    # Botão upload PREDICTED
    b_upload_residuals_PRE = tk.Button(lframe2, text='Browse file', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,
                          command = lambda:upload_file_residuals(label_sumario=_sum2,
                                                      upload_status=upload_status2,
                                                      date_col=e_date_col2,
                                                      h_col=e_h_col2,
                                                      skipr=e_skip_hrows2,
                                                      skipf=e_skip_frows2,
                                                      sep=int(r2.get()),
                                                      other_sep=e_other2,
                                                      b_upload_residuals=b_upload_residuals_PRE,
                                                      l_stat_hmax_val=l_stat_hmax_val2,
                                                      l_stat_hmin_val=l_stat_hmin_val2,
                                                      l_stat_hmean_val=l_stat_hmean_val2,
                                                      l_stat_startdate_val=l_stat_startdate_val2,
                                                      l_stat_enddate_val=l_stat_enddate_val2,
                                                      l_stat_dateinterv_val=l_stat_dateinterv_val2,
                                                      l_stat_sf_val=l_stat_sf_val2,
                                                      b_run_residuals=b_run_residuals,
                                                      b_export_residuals=b_export_residuals,
                                                      r_julian =r_julian ,
                                                      r_dt=r_dt,
                                                      r_m=r_m,
                                                      r_f=r_f,
                                                      r_o=r_o,
                                                      e_o=e_o,
                                                      r_hours=r_hours,
                                                      r_days=r_days,
                                                      r_hz=r_hz,
                                                      b_export_residuals_fft=b_export_residuals_fft,
                                                      b_run_residuals_fft=b_run_residuals_fft,
                                                      save_status=save_status,
                                                      save_status_fft=save_status_fft,
                                                      obs = False,
                                                      pre = True,
                                                      
                                                      ))
    b_upload_residuals_PRE.configure(anchor="center")
    b_upload_residuals_PRE.place(relx=.5, y=145,anchor='center')

    # Residuals frame
    frame_residuals = ttk.LabelFrame(frame, text='Compute Residuals',labelanchor='n')
    frame_residuals.place(x=555,y=5,width=267,height=280)

    # Residuals plot frame
    frame_residuals_plot = tk.LabelFrame(frame_residuals, text='Plot options',labelanchor='n',
                                   font=('raleway', 10,'bold'),fg='#1c4366')
    frame_residuals_plot.place(x=5,y=5,width=254,height=116) 

    # X-axis Units
    xunits_frame = tk.LabelFrame(frame_residuals_plot,text='Date Units',labelanchor='n',
                                 font=('raleway', 9,'bold'),fg='#1c4366')
    xunits_frame.place(x=3,y=5,height=88,width=120)
    # Radio buttons for X-axis Units
    r_xunits = tk.IntVar()
    r_xunits.set('2')
    # Julian days 
    r_julian = tk.Radiobutton(xunits_frame,text='Julian days',variable=r_xunits,value=1,state='disabled')
    r_julian.place(x=10,y=12)  
    # Datetime 
    r_dt = tk.Radiobutton(xunits_frame,text='Datetime',variable=r_xunits,value=2,state='disabled')
    r_dt.place(x=10,y=32)      
 
    # Y-axis Units
    yunits_frame = tk.LabelFrame(frame_residuals_plot,text='Height Units',labelanchor='n',
                                 font=('raleway', 9,'bold'),fg='#1c4366')
    yunits_frame.place(x=127,y=5,height=88,width=120)   
    # Radio buttons for Y-axis Units
    r_yunits = tk.IntVar()
    r_yunits.set('1')
    # Meters
    r_m = tk.Radiobutton(yunits_frame,text='Meters',variable=r_yunits,value=1,state='disabled')
    r_m.place(x=10,y=2)  
    # Feets 
    r_f = tk.Radiobutton(yunits_frame,text='Feets',variable=r_yunits,value=2,state='disabled')
    r_f.place(x=10,y=22)   
    # Other height unit
    r_o = tk.Radiobutton(yunits_frame,text='Other',variable=r_yunits,value=3,state='disabled')
    r_o.place(x=10,y=42)     
    # Other Entry
    e_o = tk.Entry(yunits_frame,width=7,state='disabled')
    e_o.place(x=70,y=44)
    
    # Help RESIDUALS button
    b_help_residuals = tk.Button(frame_residuals,text='?',font=('Rayleway','16','bold'),
                            fg='white',bg='#1c4366',command = help_bw_popup)
    b_help_residuals.place(x=238,y=-7,width=20,height=20) 

    # Button run and plot residuals
    b_run_residuals= tk.Button(frame_residuals, text='Compute Residuals & Plot', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,state='disabled',
                          command = lambda: run_residuals(df_obs=df_obs,
                                                          df_pre=df_pre,
                                                          r_yunits=r_yunits,
                                                          r_xunits=r_xunits,
                                                          e_o=e_o,
                                                          b_export_residuals=b_export_residuals,
                                                          b_run_residuals_fft=b_run_residuals_fft,
                                                          r_hours=r_hours,
                                                          r_days=r_days,
                                                          r_hz=r_hz,
                                                          b_run_residuals=b_run_residuals,
                                                          save_status=save_status,
                                                          save_status_fft=save_status_fft,
                                                          b_export_residuals_fft=b_export_residuals_fft
                                                          ))
    b_run_residuals.configure(anchor="center")
    b_run_residuals.place(relx=.5, y=145,anchor='center')   

    # Button export residuals ASCII
    b_export_residuals = tk.Button(frame_residuals, text='Export ASCII', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,state='disabled',
                          command = lambda: export_ascii(df_to_be_exported=df_to_export,
                                                         button_export=b_export_residuals,
                                                         save_status=save_status))
    b_export_residuals.configure(anchor="center")
    b_export_residuals.place(relx=.5, y=185,anchor='center')  
    
    # Save Status
    save_status = tk.Label(frame_residuals, text=' ',wraplength=260,width=36,
                           font=('Rayleway','9',))
    save_status.configure(anchor="center",bg=DEFAULT_BG_COLOR)
    save_status.place(x=2,y=205) 

    # Main FFT residuals frame
    frame_residuals_fft = ttk.LabelFrame(frame,text='Residuals FFT',labelanchor='n')
    frame_residuals_fft.place(x=555,y=300,height=230,width=267)
    
    # FFT Scale frame
    frame_residuals_fft_scale = tk.LabelFrame(frame_residuals_fft,text='X-axis Scale',height=50,width=258,
                               font=('raleway', 10,'bold'),fg='#1c4366')
    frame_residuals_fft_scale.place(x=3,y=5)
    
    # Scale Options
    r_scale = tk.IntVar()
    r_scale.set('1')
    # Hours 
    r_hours = tk.Radiobutton(frame_residuals_fft_scale,text='Hours',variable=r_scale,value=1,state='disabled')
    r_hours.place(x=10,y=2)  
    # Days
    r_days = tk.Radiobutton(frame_residuals_fft_scale,text='Days',variable=r_scale,value=2,state='disabled')
    r_days.place(x=100,y=2)       
    # Hz
    r_hz = tk.Radiobutton(frame_residuals_fft_scale,text='Hz',variable=r_scale,value=3,state='disabled')
    r_hz.place(x=190,y=2)      

    # Button run FFT
    b_run_residuals_fft = tk.Button(frame_residuals_fft, text='Run FFT & Plot', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,state='disabled',
                          command = lambda: run_fft(df_to_export,
                                                    r_scale,
                                                    b_export_residuals_fft,
                                                    save_status_fft,
                                                    b_run_fft=b_run_residuals_fft))
    b_run_residuals_fft.configure(anchor="center")
    b_run_residuals_fft.place(relx=.5, y=77,anchor='center')  

    # Button export FFT
    b_export_residuals_fft = tk.Button(frame_residuals_fft, text='Export ASCII', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,state='disabled',
                          command = lambda: export_ascii(df_to_be_exported=df_fft,
                                                         button_export=b_export_residuals_fft,
                                                         save_status=save_status_fft))
    b_export_residuals_fft.configure(anchor="center")
    b_export_residuals_fft.place(relx=.5, y=120,anchor='center')  
    
    # Save Status
    save_status_fft = tk.Label(frame_residuals_fft, text=' ',wraplength=260,width=36,
                           font=('Rayleway','9',))
    save_status_fft.configure(anchor="center",bg=DEFAULT_BG_COLOR)
    save_status_fft.place(x=2,y=140) 

    # Help FFT
    b_help_fft = tk.Button(frame_residuals_fft,text='?',font=('Rayleway','16','bold'),
                            fg='white',bg='#1c4366',command = help_fft_popup)
    b_help_fft.place(x=240,y=-7,width=20,height=20) 





def fft_frame():

    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window
    # master.geometry("566x633")

    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Spectral/Harmonic Analysis'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)

    # Layout input/browse  
    x = 5
    y = 5
    box_name = 'Data Input'
    lframe,e_skip_hrows,e_skip_frows,e_date_col,e_h_col,lframe_delimiter,r,e_other,upload_status,l_stat_hmax_val,l_stat_hmin_val,l_stat_hmean_val,l_stat_startdate_val,l_stat_enddate_val,l_stat_dateinterv_val,l_stat_sf_val,_sum = inpux_box(frame,box_name,x,y)

    # Botão upload
    b_upload_fft = tk.Button(lframe, text='Browse file', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,
                          command = lambda:upload_file_fft(label_sumario=_sum,
                                                      upload_status=upload_status,
                                                      date_col=e_date_col,
                                                      h_col=e_h_col,
                                                      skipr=e_skip_hrows,
                                                      skipf=e_skip_frows,
                                                      sep=int(r.get()),
                                                      other_sep=e_other,
                                                      b_upload_fft=b_upload_fft,
                                                      l_stat_hmax_val=l_stat_hmax_val,
                                                      l_stat_hmin_val=l_stat_hmin_val,
                                                      l_stat_hmean_val=l_stat_hmean_val,
                                                      l_stat_startdate_val=l_stat_startdate_val,
                                                      l_stat_enddate_val=l_stat_enddate_val,
                                                      l_stat_dateinterv_val=l_stat_dateinterv_val,
                                                      l_stat_sf_val=l_stat_sf_val,
                                                      b_run_fft=b_run_fft,
                                                      r_hours=r_hours,
                                                      r_days=r_days,
                                                      r_hz=r_hz,
                                                      b_export_fft=b_export_fft,
                                                      save_status=save_status,
                                                      
                                                      ))
    b_upload_fft.configure(anchor="center")
    b_upload_fft.place(relx=.5, y=145,anchor='center')


    # FFT 
    
    # Main FFT frame
    frame_fft = ttk.LabelFrame(frame,text='Fast Fourier Transform',labelanchor='n')
    frame_fft.place(x=280,y=5,height=230,width=267)
    
    # FFT Scale frame
    frame_fft_scale = tk.LabelFrame(frame_fft,text='X-axis Scale',height=50,width=258,
                               font=('raleway', 10,'bold'),fg='#1c4366')
    frame_fft_scale.place(x=3,y=5)
    
    # Scale Options
    r_scale = tk.IntVar()
    r_scale.set('1')
    # Hours 
    r_hours = tk.Radiobutton(frame_fft_scale,text='Hours',variable=r_scale,value=1,state='disabled')
    r_hours.place(x=10,y=2)  
    # Days
    r_days = tk.Radiobutton(frame_fft_scale,text='Days',variable=r_scale,value=2,state='disabled')
    r_days.place(x=100,y=2)       
    # Hz
    r_hz = tk.Radiobutton(frame_fft_scale,text='Hz',variable=r_scale,value=3,state='disabled')
    r_hz.place(x=190,y=2)      

    # Button run FFT
    b_run_fft = tk.Button(frame_fft, text='Run FFT & Plot', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,state='disabled',
                          command = lambda: run_fft(df,
                                                    r_scale,
                                                    b_export_fft,
                                                    save_status,
                                                    b_run_fft))
    b_run_fft.configure(anchor="center")
    b_run_fft.place(relx=.5, y=77,anchor='center')    

    # Button export FFT
    b_export_fft = tk.Button(frame_fft, text='Export ASCII', font=('raleway', 10,'bold'),
                          fg = 'black',width=6,padx=73,pady=4,borderwidth=4,state='disabled',
                          command = lambda: export_ascii(df_to_be_exported=df_fft,
                                                         button_export=b_export_fft,
                                                         save_status=save_status))
    b_export_fft.configure(anchor="center")
    b_export_fft.place(relx=.5, y=120,anchor='center')  
    
    # Save Status
    save_status = tk.Label(frame_fft, text=' ',wraplength=260,width=36,
                           font=('Rayleway','9',))
    save_status.configure(anchor="center",bg=DEFAULT_BG_COLOR)
    save_status.place(x=2,y=140) 

    # Help FFT
    b_help_fft = tk.Button(frame_fft,text='?',font=('Rayleway','16','bold'),
                            fg='white',bg='#1c4366',command = help_fft_popup)
    b_help_fft.place(x=240,y=-7,width=20,height=20) 



def tideZoning_frame():

    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window
    # master.geometry("566x633")
    
    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Tide Zoning'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)



def tidePrediction_frame():

    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window
    # master.geometry("566x633")
    
    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Tide Prediction'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)



def createwf_frame():
    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window
    # master.geometry("566x633")

    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Create Workflow'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)



def openwf_frame():
    global df
    DEFAULT_BG_COLOR='#f1f0f1'

    # Resize master window
    # master.geometry("566x633")
    
    # Defining window style
    try:
        style = call_style()
    except:
        pass

    # Creating base frame
    title = 'Open Workflow'
    frame = base_layer(DEFAULT_BG_COLOR,title,master,frame_responsive_width=551)


# Creating main window (root)
master = tk.Tk()
master.title('uniTIDE')
# master.geometry("566x633")
master.geometry("843x633")
master.configure(bg='#1c4366')
# Making unable to resize in Y axis!
master.resizable(True, 0)

# Doing the proper Welcome!
the_welcome(master)

# Creating the menubar
menubar = Menu(master)
master.config(menu=menubar)

# Creating WELCOME! menu
welcome_menu = Menu(menubar, tearoff=False)
welcome_menu.add_command(label='Info',command = info_frame)
welcome_menu.add_command(label='Documentation',command = documentation_frame)
welcome_menu.add_separator()
welcome_menu.add_command(label='Exit',command=master.destroy)
menubar.add_cascade(label="Welcome!",menu=welcome_menu)

# Creating Visualization menu
vis_menu = Menu(menubar, tearoff=False)
vis_menu.add_command(label='Plot Tide',command=plot_frame)
vis_menu.add_command(label='Compare Tide',command=compare_frame)
menubar.add_cascade(label="Visualization",menu=vis_menu)

# Creating Processing menu
processing_menu = Menu(menubar, tearoff=False)
processing_menu.add_command(label='QC',command=qc_frame)
processing_menu.add_command(label='Buttlerworth filter',command=bw_frame)
processing_menu.add_command(label='Resample',command=resample_frame)
menubar.add_cascade(label="Processing",menu=processing_menu)

# Creating Analysis menu
analysis_menu = Menu(menubar, tearoff=False)
analysis_menu.add_command(label='Residuals',command=residuals_frame)
analysis_menu.add_command(label='Spectral/Harmonic Analysis',command=fft_frame)
menubar.add_cascade(label="Analysis",menu=analysis_menu)

# Creating Products menu
products_menu = Menu(menubar, tearoff=False)
products_menu.add_command(label='Tide Prediction',command=tidePrediction_frame)
products_menu.add_command(label='Tide Zoning',command=tideZoning_frame)
menubar.add_cascade(label="Products",menu=products_menu)

# Creating Workflow menu
workflow_menu = Menu(menubar, tearoff=False)
workflow_menu.add_command(label='Create Workflow',command=createwf_frame)
workflow_menu.add_command(label='Open Workflow',command=openwf_frame)
menubar.add_cascade(label="Workflow",menu=workflow_menu)



master.mainloop()



