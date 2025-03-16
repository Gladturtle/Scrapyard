import tkinter as tk

def on_drag(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

root = tk.Tk()
root.overrideredirect(True) 
root.geometry("400x300")  


srs_cat = tk.PhotoImage(file='srs_cat.png')

srs_cat_label = tk.Label(root,image=srs_cat)
srs_cat_label.pack()





root.mainloop()
