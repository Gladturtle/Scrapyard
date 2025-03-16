import tkinter as tk

def on_drag(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

root = tk.Tk()
root.overrideredirect(True) 
root.geometry("400x300")  
root.configure(bg="lightblue")  


title_bar = tk.Frame(root, bg="blue", relief="raised", bd=2, height=30)
title_bar.pack(fill=tk.X)
title_bar.bind("<B1-Motion>", on_drag)


close_btn = tk.Button(title_bar, text="X", bg="red", fg="white", command=root.destroy)
close_btn.pack(side=tk.RIGHT, padx=5, pady=2)


label = tk.Label(root, text="Borderless Tkinter Window", bg="lightblue", font=("Arial", 14))
label.pack(pady=50)

root.mainloop()
