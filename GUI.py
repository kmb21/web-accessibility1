import tkinter as tk

window = tk.Tk()

objs = []

frm_test = tk.Frame(master = window, relief = tk.RAISED, borderwidth=10)
objs.append(frm_test)
btn_test = tk.Button(master = frm_test, text = "Click Me")
objs.append(btn_test)

for object in objs:
    object.pack()






window.mainloop()
