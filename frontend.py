import tkinter as tk
import time 
import psutil
import random
from PIL import Image, ImageTk
from backend import detection,randomize



def fade_out(window, alpha):
    """Fade out the window gradually."""
    if alpha > 0:
        window.attributes("-alpha", 1)
        window.after(50, fade_out, window, alpha - 0.05)
    else:
        window.destroy()

def slide_up(window, start_offset, target_offset,x):
    """Animate the window sliding slightly upwards in the center of the screen."""
    if start_offset > target_offset:
        window.geometry(f"400x300+{x}+{start_offset}")
        window.after(10, slide_up, window, start_offset - 2, target_offset)

def fade_in(alpha=0.0):
    if alpha < 1.0:
        root.attributes("-alpha", alpha)
        root.after(50, fade_in, alpha + 0.05)
    else:
        root.after(3000, fade_out, root, 1.0)  # Stay for 3 seconds before fading out

while detection():
    root = tk.Tk()
    root.overrideredirect(True)  # Remove window decorations
    root.attributes("-alpha", 0.0)  # Start fully transparent
    root.attributes('-topmost', True)
    
    # Get screen dimensions and set window geometry
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 400
    window_height = 300
    x = (screen_width - window_width) // 2
    center_y = (screen_height - window_height) // 2  # Center position
    start_y = center_y + 50  # Start slightly below the center
    root.geometry(f"{window_width}x{window_height}+{x}+{start_y}")
    
    # Load and rotate the image
    original_image = Image.open("srs_cat.png")
    rotated_image = original_image.rotate(20, expand=True)  # Tilt 20 degrees left
    srs_cat = ImageTk.PhotoImage(rotated_image)
    
    # Create a canvas that fills the window
    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white", highlightthickness=0)
    canvas.pack()
    
    # Calculate offsets to center the rotated image in the canvas
    img_width, img_height = rotated_image.size
    offset_x = (window_width - img_width) // 2
    offset_y = (window_height - img_height) // 2

    # Place the image on the canvas using the top-left anchor
    canvas.create_image(offset_x, offset_y, image=srs_cat, anchor="nw")
    
    slide_up(root, start_y, center_y,x)
    fade_in()
    root.mainloop()
