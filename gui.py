import tkinter as tk 
from tkinter import ttk
import forex2

def get_list():
    a= pd.read_csv("list.csv")
    b = a['']
    
def get_forex(fc, tc,rate):
    er = forex.get_rate(fc,tc)
    rate.configure(text=er)
    
    

main = tk.Tk()
main.title("Real Time Forex")
main.geometry("350x350")
#main.resizable(0,0)
w1 = ttk.Label(main, text="From Currency").grid(column=0,row=0,sticky=tk.W,padx=15)
w2 = ttk.Label(main, text="To Currency").grid(column=1,row=0,sticky=tk.W,padx=15)
w3 = ttk.Label(main,text="Exchange Rate --> ").grid(column=0,row=2)
rate = tk.Label(main, text="0.00")
rate.grid(column=1,row=2)

b1 = ttk.Button(main, text = "Submit",command= lambda: get_forex(from_c.get(),to_c.get(),rate)).grid(column=2,row = 1,rowspan=2, sticky=tk.N+tk.W+tk.E+tk.S,padx=20)


from_c = tk.StringVar()
fromc = ttk.Entry(main, width=14, textvariable=from_c)
fromc.grid(column = 0,row=1)

to_c = tk.StringVar()
toc = ttk.Entry(main, width = 15, textvariable = to_c)
toc.grid(column=1,row=1)
main.mainloop()
