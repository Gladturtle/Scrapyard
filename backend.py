import psutil
import random
import time
def detection():
    while True:
        while True:
            running = "Code.exe" in [p.name() for p in psutil.process_iter()]
            if running == True:
                break
        time.sleep(random.randint(0,300))
        running = "Code.exe" in [p.name() for p in psutil.process_iter()]
        if running == True:
            return True
        else:
            continue



def fade_out(window, alpha):
    """Fade out the window gradually."""
    if alpha > 0:
        window.attributes("-alpha", alpha)
        window.after(50, fade_out, window, alpha - 0.05)
    else:
        window.destroy()

def slide_up(window, start_offset, target_offset):
    """Animate the window sliding slightly upwards in the center of the screen."""
    if start_offset > target_offset:
        window.geometry(f"400x300+{window.winfo_x()}+{start_offset}")
        window.after(10, slide_up, window, start_offset - 2, target_offset)

def show_popup():
    """Display the image popup in the center of the screen with a slight upward slide animation, tilt effect, and fade-out."""
    root = tk.Tk()
    root.overrideredirect(True)  # Remove window decorations
    root.attributes("-alpha", 0.0)  # Start fully transparent
    
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
    
    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white", highlightthickness=0)
    canvas.pack()
    canvas.create_image(window_width // 2, window_height // 2, image=srs_cat)
    
    def fade_in(alpha=0.0):
        if alpha < 1.0:
            root.attributes("-alpha", alpha)
            root.after(50, fade_in, alpha + 0.05)
        else:
            root.after(3000, fade_out, root, 1.0)  # Stay for 3 seconds before fading out
    
    slide_up(root, start_y, center_y)
    fade_in()
    root.mainloop()

def monitor_vs_code():
    """Continuously monitor VS Code and display the popup when it opens."""
    if detection():
        show_popup()

if __name__ == "__main__":
    monitor_vs_code()
