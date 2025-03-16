import tkinter as tk
import threading
from PIL import Image, ImageTk
import time
import random
from backend import detection, randomize_cood, play_music, randomize_deg, randomize_img, instatiate_model, generate_response

instatiate_model()

def fade_out(window, alpha):

    if alpha > 0:
        window.attributes("-alpha", alpha)
        window.after(50, fade_out, window, alpha - 0.05)
    else:
        window.destroy()

def slide_up(window, start_offset, target_offset, x_coor):

    if start_offset > target_offset:
        window.geometry(f"400x300+{x_coor}+{start_offset}")
        window.after(10, slide_up, window, start_offset - 2, target_offset)
 

def spin_image(canvas, image_label, img_path, angle=0):

    rotated_img = Image.open(img_path).rotate(angle, expand=True)
    rotated_photo = ImageTk.PhotoImage(rotated_img)
    image_label.config(image=rotated_photo)
    image_label.image = rotated_photo  

    if angle < 360:  
        root.after(50, spin_image, canvas, image_label, img_path, angle + 10)

def pulse_image(image_label, img_path, scale_factor=1.0, direction=1):

    img = Image.open(img_path)
    new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
    
    resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
    pulse_photo = ImageTk.PhotoImage(resized_img)
    image_label.config(image=pulse_photo)
    image_label.image = pulse_photo

    if scale_factor > 1.2 or scale_factor < 0.8:
        direction *= -1  

    new_scale = scale_factor + (0.05 * direction)
    root.after(100, pulse_image, image_label, img_path, new_scale, direction)


def wobble_image(image_label, base_x, direction=1):
    current_x = image_label.winfo_x()
    displacement = current_x - base_x
    if abs(displacement) >= 20:
        direction = -direction
    new_x = current_x + (5 * direction)
    image_label.place_configure(x=new_x)
    root.after(50, wobble_image, image_label, base_x, direction)



def fade_in(alpha=0.0):

    if alpha < 1.0:
        root.attributes("-alpha", alpha)
        root.after(50, fade_in, alpha + 0.05)
    else: 
        root.after(5000, fade_out, root, 1.0)

while detection():
    root = tk.Tk()
    root.overrideredirect(True)  
    root.attributes("-alpha", 0.0)  
    root.attributes('-topmost', True)
    
    transparent_color = "magenta"
    root.config(bg=transparent_color)
    root.attributes('-transparentcolor', transparent_color)

    message = generate_response()
    sound = threading.Thread(target=play_music)
    sound.start()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 400
    window_height = 300
    x = (screen_width - window_width) // 2
    center_y = (screen_height - window_height) // 2 
    start_y = center_y + 50  
    root.geometry(f"{window_width}x{window_height}+{x}+{start_y}")

    x, center_y, start_y = randomize_cood(0, 0, screen_width - window_width, screen_height - window_height)
    
    text_label = tk.Label(root, text=message, font=("Arial", 14, "bold"), fg="black", bg="white", wraplength=380, justify="left")
    text_label.pack(pady=10, padx=10)
    
    img_path = f"./data/{randomize_img()}"
    original_image = Image.open(img_path)
    srs_cat = ImageTk.PhotoImage(original_image)

    canvas = tk.Canvas(root, width=window_width, height=window_height, bg=transparent_color, highlightthickness=0)
    canvas.pack()

    image_label = tk.Label(canvas, image=srs_cat, bg=transparent_color)
    image_label.pack()

    anim_num = random.randint(0,3)

    slide_up(root, start_y, center_y, x)
    fade_in()
    if anim_num==0:
        spin_image(canvas=canvas,image_label=image_label, img_path=img_path) 
    elif anim_num==1:
        pulse_image(image_label=image_label, img_path=img_path)  
    elif anim_num==2:
        wobble_image(image_label, x) 
    else:
        pulse_image(image_label=image_label, img_path=img_path)  
  

    root.mainloop()
