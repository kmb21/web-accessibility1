import tkinter as tk
from tkinter import filedialog
from accessibilitySoup import *

filepath = ""
savepath = ""

def open_file(event):
    global filepath
    filepath = filedialog.askopenfilename()
    address_entry.delete(0, tk.END)
    address_entry.insert(0, filepath)
    
def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

def remediation():
    if filepath != "" and savepath != "":
        soup = Soup(filepath)
        soup.standardized()
        soup.savefile(path=savepath)
        
        
def save_file():
    global savepath
    savepath = filedialog.asksaveasfilename()
    save_entry.delete(0, tk.END)
    save_entry.insert(0, savepath)
    
def clear_button():
    address_entry.delete(0, tk.END)
    save_entry.delete(0, tk.END)

def appFrame():
    app_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
    app_frame.pack(expand=True,fill=tk.BOTH)

    app_frame.rowconfigure([0,1], weight=1, minsize=5)
    app_frame.columnconfigure([0,1,2], weight=1, minsize=5)
    return app_frame

def labels(app_frame):
    label = tk.Label(master=app_frame, text="Enter file path:")
    label.grid(row=0, column=0, sticky='e', pady=5)  
    
    save_label = tk.Label(app_frame, text="Save Location:")
    save_label.grid(row=1, column=0, sticky="e", pady=5)
    
def addressEntry(app_frame):
    address_entry = tk.Entry(master=app_frame, width=30, state="normal")
    address_entry.grid(row=0, column=1, sticky='ew', pady=5) 
    return address_entry

def saveEntry(app_frame):
    save_entry = tk.Entry(app_frame, width=30)
    save_entry.grid(row=1, column=1, sticky="we", pady=5)
    return save_entry

def buttons(app_frame):    
    open_btn = tk.Button(master=app_frame, text="Open File", command=lambda: open_file(None))
    open_btn.grid(row=0, column=2, sticky='w', pady=5)  
    
    save_button = tk.Button(app_frame, text="Save As", command=save_file)
    save_button.grid(row=1, column=2, sticky="w", pady=5)

    open_btn.bind("<Return>", open_file)
    save_button.bind("<Return>", save_file)

    rem_btn = tk.Button(text="Remediate", master=window, command=remediation)
    rem_btn.pack(side=tk.RIGHT)

    clr_btn = tk.Button(text="Clear", master=window, command=clear_button)
    clr_btn.pack(side=tk.RIGHT)
    
################################################ MAIN CODE ######################################################
        
window = tk.Tk()
window.minsize(600,200)
window.maxsize(600,200)
window.title("Accessibility Script")
window.geometry("600x200")

##The main frame that keeps the window together(app_frame )  
app_frame = appFrame()
labels(app_frame)
address_entry = addressEntry(app_frame)
save_entry = saveEntry(app_frame)
buttons(app_frame)

    

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
