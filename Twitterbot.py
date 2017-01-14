from tkinter import *
from tkinter import ttk
import tkinter as tk
import tweepy
import cfg_list
import os
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    
root = Tk()
stat = StringVar()
user = ''

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    api = tweepy.API(auth)
    return tweepy.API(auth)

def jalankan():
    try:
        df = cfg_list.daftar()
        for a in df:
            api = get_api(a)
            tweet = str(stat.get())
            status = api.update_status(status=tweet)
            user = str(api.me().screen_name)
            print("tweet pada username " + str(api.me().screen_name) + " sukses")

    except ValueError:
        pass

def analyzer():
    child = tk.Toplevel(root)
    
    mainframe = ttk.Frame(child, padding="3 3 3 3")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    ttk.Label(mainframe, text="Analyzer").grid(column=1, row=1, sticky=W)
    ttk.Label(mainframe, text="Hashtag").grid(column=1, row=3, sticky=W)
    tag_entry = ttk.Entry(mainframe, width=10, textvariable="Change This Text")
    tag_entry.grid(column=2, row=3, sticky=(W, E))
    ttk.Button(mainframe, text="Analyze", command=callback).grid(column=3, row=3, sticky=W)
    ttk.Button(mainframe, text="Plot", command=plotter).grid(column=3, row=6, sticky=W)

    ttk.Label(mainframe, text="Total").grid(column=1, row=4, sticky=W)
    ttk.Label(mainframe, text="Real").grid(column=1, row=5, sticky=W)
    ttk.Label(mainframe, text="Robot").grid(column=1, row=6, sticky=W)

    ttk.Label(mainframe, text=": 1000").grid(column=2, row=4, sticky=W)
    ttk.Label(mainframe, text=": 210").grid(column=2, row=5, sticky=W)
    ttk.Label(mainframe, text=": 790").grid(column=2, row=6, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

def plotter():
    child = tk.Toplevel(root)
    app = mygui(child)
    
def myplotcode():
    x = np.linspace(0,2*np.pi)
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.plot(x, (x**2)/2)

    return fig

def plotbar():
    f = Figure(figsize=(5,4), dpi=100)
    ax = f.add_subplot(111)
    data = (20, 35, 30, 35, 27)

    ind = np.arange(5)
    width = .5
    rects1 = ax.bar(ind, data, width)

    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)


class mygui(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.fig = myplotcode()
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().config(width=300, height=300)
        self.canvas.show()

        self.canvas.get_tk_widget().pack()
        self.pack(fill=tk.BOTH, expand=1)

def open_cfg():
    try:
        os.system('gedit cfg_list.py')
    except ValueError:
        pass

def about():
    child = tk.Toplevel(root)

    mainframe = ttk.Frame(child, padding="3 20 3 20")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    ttk.Label(mainframe, text="This tool made by \n fzrbbx.").grid(column=1, row=1, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

def callback():
    print("null")

def main():
    root.title("Twitterbot v.1")    

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label="Menu", menu=filemenu)
    filemenu.add_command(label="Edit Config", command=open_cfg)
    filemenu.add_command(label="Analyzer", command=analyzer)
    filemenu.add_command(label="Show Log", command=callback)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Usage", command=callback)
    helpmenu.add_command(label="About", command=about)

    ttk.Label(mainframe, text="Tweet").grid(column=1, row=1, sticky=W)

    stat_entry = ttk.Entry(mainframe, width=20, textvariable=stat)
    stat_entry.grid(column=2, row=1, sticky=(W, E))

    ttk.Button(mainframe, text="Execute", command=jalankan).grid(column=3, row=1, sticky=W)
    #ttk.Button(mainframe, text="Edit Config", command=open_cfg).grid(column=3, row=2, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    
    stat_entry.focus()    

    root.bind('<Return>', jalankan)
    root.mainloop()

if __name__ == "__main__" :
    main()
    
