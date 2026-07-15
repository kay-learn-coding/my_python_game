import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import os

# Initialize root once here
root = tk.Tk()
root.title("My RPG Adventure")
root.geometry("800x600")
root.configure(bg="#1a1a1a")

# Global game variables
player_name = ""

def display_with_image(text, image_path=None, delay=2):
    """Universal function to draw text and images to the shared root window."""
    for widget in root.winfo_children():
        widget.destroy()
        
    if image_path and os.path.exists(image_path):
        image_path = image_path.replace("\\", "//")
        try:
            img = Image.open(image_path)
            img.thumbnail((800, 300), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_label = Label(root, image=photo, bg="#1a1a1a")
            img_label.image = photo  
            img_label.pack(pady=10)
        except Exception as e:
            print(f"Could not load image: {e}")

    text_label = Label(root, text=text, font=("Arial", 12), 
                       fg="#ffffff", bg="#1a1a1a", wraplength=700)
    text_label.pack(pady=20)
    root.update()
    
    # Use non-blocking sleep so the Tkinter window stays responsive
    root.after(int(delay * 1000))

def display_image(image_path, delay=2):
    display_with_image("", image_path=image_path, delay=delay)
