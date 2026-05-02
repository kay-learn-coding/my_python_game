import time
import random
import sys
import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from PIL import Image, ImageTk
import os

#All list here
Bosses=["JWA_DO_GYUL","The Three Sword of Qingcheng","Bright Rock","First Apprentice"]

# Initialize GUI window
root = tk.Tk()
root.title("The Chronicles of Heavenly Martial Arts")
root.geometry("900x700")
root.configure(bg="#1a1a1a")

# Helper function to display image with text
def display_with_image(text, image_path=None, delay=2):
    """Display text and optionally an image on the GUI"""
    # Clear previous widgets
    for widget in root.winfo_children():
        widget.destroy()
    
# Display image if provided
    if image_path and os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((800, 300), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_label = Label(root, image=photo, bg="#1a1a1a")
            img_label.image = photo  # Keep a reference
            img_label.pack(pady=10)
        except Exception as e:
            print(f"Could not load image: {e}")
    
# Display text
    text_label = Label(root, text=text, font=("Arial", 12), 
                       fg="#ffffff", bg="#1a1a1a", wraplength=850, justify="left")
    text_label.pack(pady=10, padx=10)
    
    root.update()
    time.sleep(delay)

# Alternative: Just display text (for simpler scenes)
def display_text(text, delay=2):

    """Display text only on the GUI"""
    display_with_image(text, image_path=None, delay=delay)


def show_input_screen():
    """This creates the widgets on the screen"""
    # Clear the screen first
    for widget in root.winfo_children():
        widget.destroy()

    instruction = Label(root, text="What is thy name?", font=("Arial", 14), 
                        fg="#ffcc00", bg="#1a1a1a")
    instruction.pack(pady=10)

    global name_entry 
    name_entry = Entry(root, font=("Arial", 14), justify="center")
    name_entry.pack(pady=10)
    name_entry.focus_set() 

    submit_btn = Button(root, text="Begin Journey", command=submit_name,
                        font=("Arial", 12, "bold"), bg="#333", fg="white")
    submit_btn.pack(pady=20)
    root.update()

#display input_box for player to use
def submit_name():
    player_name = name_entry.get().capitalize()
    if player_name.strip() == "":
        display_text("Please enter a name....", delay=1)
        show_input_screen() # Re-show the box if they missed it
    else:
        # This will clear the button/box and show the name
        display_text(f"The Chronicle of {player_name}", delay=2)

#Add the text entry box
global name_entry # Make it global so submit_name can see it
name_entry = Entry(root, font=("Arial", 14), justify="center")
name_entry.pack(pady=10)
name_entry.focus_set() # Puts the typing cursor in the box automatically

#Add the button-- for after name is entered
submit_btn = Button(root, text="Begin Journey", command=submit_name,
                        font=("Arial", 12, "bold"), bg="#333", fg="white")
submit_btn.pack(pady=20)
display_text(f"The Chronicle of {name_entry}", delay=(2))

#intro
#play intro slide
for i in range(1, 11):
    path = f"C:/my_python_game/img_file/intro_img/intro_{i}.png"
    display_with_image("The Chronicles of ........", path, delay=2)


#flashback
display_text(f"chapter 1",delay=(3)).capitalize()
display_with_image(f"flashback","C:\my_python_game\img_file\flashback_img\flashback_img_1.png",delay=(3)).capitalize()
display_with_image(f"Master--{name_entry}....","C:\my_python_game\img_file\flashback_img\flashback_img_line_1.png",delay=(3))
display_with_image(f"{name_entry}-Yes Master?","C:\my_python_game\img_file\flashback_img\flashback_img_line_1.png",delay=(2))
display_with_image(f"Master--Tell me, what is the most important quality of a martial artist?","C:\my_python_game\img_file\flashback_img\flashback_img_line_1.png",delay=(3))
display_with_image(f"{name_entry}--Well, would that not be Excellence in martial arts skills and depth of their QI?","C:\my_python_game\img_file\flashback_img\flashback_img_line_2.png",delay=(3))
display_with_image(f"Master--You are not wrong","C:\my_python_game\img_file\flashback_img\flashback_img_line_2.png",delay=(2))
display_with_image(f"In my opinion the most important quality is......","C:\my_python_game\img_file\flashback_img\flashback_img_line_3.png",delay=(2))
display_with_image(f"Harmony","C:\my_python_game\img_file\flashback_img\flashback_img_line_4.png",delay=(4))
display_with_image(f"All martial arts are based on the principle of harmony!","C:\my_python_game\img_file\flashback_img\flashback_img_line_5.png",delay=(2))
display_with_image(f"Harmony with yourself and others","C:\my_python_game\img_file\flashback_img\flashback_img_line_5.png",delay=(2))

show_input_screen() #show the box and text
root.mainloop() #keep GUI open -- need to always be at the end

#Flashback end

'''
#chapter_1.1
print(f"{name}--You emphasized harmony your whole life")
time.sleep(4)
print("And yet")
time.sleep(4)
print("This is how you go...!")
time.sleep(2)
print("URRRRRRGH")
time.sleep(4)
print("MASTER")
time.sleep(4)

#narration
print("You and your master was attacked by Martial artist from the Light faction")
time.sleep(3)
print("The Three Sword of Qingcheng")
time.sleep(3)
print(f"Lead by The {Bosses[-1]} of Qingcheng Sect")
time.sleep(3)
print(f"The Mount Hua Sect {Bosses[-2]}")
time.sleep(2)
print("The Highly Esteemed Exorcist Squad")
time.sleep(2)
print("North River Peng Clan")
time.sleep(2)
print("Mountain Cleaver")
time.sleep(2)
print(f"Lord of the Martial Alliance {Bosses[0]}")
time.sleep(2)
#narration_end

#Continue_1.2
print(f"{name}--Let me ask you a question")
time.sleep(2)
print(f"{Bosses[-2]}--Go Head")
time.sleep(2)
print(f"{name}--I Know the people who gathered here are neither fools")
time.sleep(2)
print("So it also should be apparent that my master and i did not practiice the vile demonic art")
time.sleep(2)
print("Let us speak honestly then")
time.sleep(2)
print("WHY DID YOU DO THIS!!")
time.sleep(2)
print("HE DEVOTED HIS WHOLE LIFE TO THE MARTIAL SOCIETY")
time.sleep(2)
print("SO WHY!!!")
time.sleep(3)

#narration
print(f"Half a year ago")
time.sleep(2)
print(f"A rumour started to spread")
print("That the text of the vile and atrocious silent ten skills of the demon, Was in our possession.")
time.sleep(2)
print("Some went as far to say that we had already learned it ourselves")
time.sleep(2)
print("When we tried to protest these lies and proclaim our innocent.")
time.sleep(2)
print("No one listen")
time.sleep(2)
print("Later,we were visted by martial artists looking to verify the rumours themselves")
time.sleep(2)
print(f"Swearing upon the heavens that the book was not here.")
time.sleep(2)
print(f"My master cooperated with their investigation")
time.sleep(2)
print(f"Although we had accumulated vast literatures on martial arts.")
time.sleep(2)
print(f"We could say for certain that neither the silent ten skills of the demon, nor anything associated with it was in our possession.")
print("But How.....")
time.sleep(2)
print("Was the Godforsaken text here....!")
time.sleep(2)
#narration_end

#chapter_1.3
print(f"It is somone here..Trying to frame us and get rid of us")
time.sleep(2)
print(f"{name}--You have mouth so speak.")
time.sleep(2)
print(f"WHAT ARE YOU ALL DOING.")
time.sleep(2)
print(f"{Bosses[0]}--HOW LONG ARE YOU GOING TO LET THAT VILE KID SPOUT BULLSHIT")
time.sleep(2)
print(F"{name}=={Bosses[0]}")
time.sleep(2)
print("That right you were always envious of my master\n" \
"My master surpassed you in both technique and personality\n" \
"I am sure that is why you cannot tolerate him")
time.sleep(2)
print(f"{Bosses[0]}--Looks like your master never taught you\n" \
"the consequences of speaking out of line")
time.sleep(2)
print("HO HO HO.")
time.sleep(2)

#First_Fight
fight_1=input(f"{Bosses[0]} Taunting you while within the range of your spear\n" \
"What do you do?\n" \
"F for Fight!\n" \
"R for Run!\n").lower()

#action
GYUL_health_bar=int(100)
hit=random.randint(5,15)
GYUL_health_bar_after_HIT=GYUL_health_bar-hit

Your_health_bar=int(100)
your_hit=random.randint(20,40)
your_health_bar_after_hit=Your_health_bar-your_hit

#fight_1
if fight_1=="f":
    print(f"You have hit for {hit}")
    print(f"You were hit for {your_hit}")
    print("JWA DO-GYUL--HoW DARE YOU!")
    time.sleep(2)
    print(f"{Bosses[0]} lost 3 fingers\n"
          "You were hit across the shoulder")
    print(f"{Bosses[0]} Health {GYUL_health_bar_after_HIT}")
    print(f"Your Health {your_health_bar_after_hit}")
else:
    print("You were stabbed in the back, such a shame your story was cut short")
    sys.exit()

#fight_1_end

#chapter_1.4
print(f"{Bosses[0]}--YOU LITTLE....!")
time.sleep(2)
print("")
time.sleep(2)
'''