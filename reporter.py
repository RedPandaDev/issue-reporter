import tkinter as tk
from tkinter import messagebox
import datetime
import os

fields = 'Summary', "Reference","Date", 'Solution','Things Tried', 'Forwarded?', 'Environment', 'Files'

def fetch(entries):
    if "yes" in entries[5][1].get().lower():
        date = datetime.datetime.now().strftime("Forwarded_%d_%m_%Y")+".txt"
    else:
        date = datetime.datetime.now().strftime("inProgress_%d_%m_%Y")+".txt"


    if not os.path.exists(date):
        open(date, 'w').close()

    file = open(date, 'a')
    
    for entry in entries:
        field = entry[0]
        if entry[0] =="Issue" :
            text  = entry[1].get(1.0,tk.END)
        else:
            text  = entry[1].get()
        file.write('%s: %s\n' % (field, text)) 
    file.write("\n")
    file.close() 

    if messagebox.askokcancel("Clear data?"," you like to clear the form?"):
        clearForm(entries)

def makeform(root, fields):
    entries = []

    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))

    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text="Issue", anchor='w')
    ent = tk.Text(row)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    entries.append(("Issue", ent))


    return entries

def clearForm(entries):
    now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    for entry in entries:
        field = entry[0]
        if entry[0] =="Issue" :
           entry[1].delete(1.0, tk.END)
        elif entry[0] == "Date":
        	entry[1].delete(0, tk.END)
        	entry[1].insert(0,now)
        else:
           entry[1].delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)

    now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    ents[2][1].insert(0,now)

    b1 = tk.Button(root, text='Save', command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.RIGHT, padx=5, pady=5)


    b2 = tk.Button(root, text='Clear', command=(lambda e=ents: clearForm(e)))
    b2.pack(side=tk.RIGHT, padx=5, pady=5)
    lbl1 = tk.Label(root, text="XYZ is not working on the production server, this seems like an overflow error stemming from report generation, see screenshot.""")
    lbl1.pack(side=tk.LEFT, padx=5, pady=5)





    root.mainloop()