import time
import random
import sys
import tkinter as tk #extreme_lite(info)
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from PIL import Image, ImageTk
import os

#all_list_here
#the_three_sword_of_qingcheng=["The First Apprentice"]
Bosses=["JWA_DO_GYUL","the_three_sword_of_qingcheng","Bright Rock","First Apprentice"]
player_name=""#var to store the player name


def display_with_image(text, image_path=None, delay=2):
    for widget in root.winfo_children():#use to clear old widget
        widget.destroy()
    if image_path and os.path.exists(image_path):
        image_path=image_path.replace("\\","//")
        try:
            img = Image.open(image_path)
            img.thumbnail((800, 300), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_label = Label(root, image=photo, bg="#1a1a1a")
            img_label.image = photo  # Keep a reference
            img_label.pack(pady=10)
        except Exception as e:
            print(f"Could not load image: {e}")

    text_label = Label(root, text=text, font=("Arial", 12), 
                       fg="#ffffff", bg="#1a1a1a", wraplength=850, justify="left")
    text_label.pack(pady=10, padx=10)
    
    root.update()
    time.sleep(delay)

def display_text(text, delay=2):
    display_with_image(text, image_path=None, delay=delay)

def display_image(image,delay=2):
    display_image(image,image_path=None,delay=delay) #test if this works

def submit_name():
    global player_name
    player_name = player_name_box.get()
    if player_name.strip() == "":
        display_text("Please enter a name....", delay=(2))
        show_input_screen() # Re-show the box if they missed it
    else:
        display_text(f"The Chronicle of {player_name}", delay=(2))
        intro_img()# start intro slide

def intro_img():
    for i in range(1, 11):
        path = f"img_file/intro_img/intro_{i}.png"
        display_with_image(f"The Chronicles of {player_name}", path, delay=2)
    start_flashback()# start flashback

def start_flashback():
    display_image(f"flashback","img_file/flashback_img/flashback_img_1.png",delay=(3))
    display_with_image(f"Master--{player_name}....","img_file/flashback_img/flashback_img_line_1.png",delay=(3))
    display_with_image(f"{player_name}-Yes Master?","img_file/flashback_img/flashback_img_line_1.png",delay=(2))
    display_with_image(f"Master--Tell me, what is the most important quality of a martial artist?","img_file/flashback_img/flashback_img_line_1.png",delay=(3))
    display_with_image(f"{player_name}--Well, would that not be Excellence in martial arts skills and depth of their QI?","img_file/flashback_img/flashback_img_line_2.png",delay=(3))
    display_with_image(f"Master--You are not wrong","img_file/flashback_img/flashback_img_line_2.png",delay=(2))
    display_with_image(f"In my opinion the most important quality is......","img_file/flashback_img/flashback_img_line_3.png",delay=(2))
    display_with_image(f"Harmony","img_file/flashback_img/flashback_img_line_4.png",delay=(4))
    display_with_image(f"All martial arts are based on the principle of harmony!","img_file/flashback_img/flashback_img_line_5.png",delay=(2))
    display_with_image(f"Harmony with yourself and others","img_file/flashback_img/flashback_img_line_5.png",delay=(2))
    start_chapter_1()

def start_chapter_1():
    display_with_image(f"{player_name}--You emphasized harmony your whole life","img_file/chapter_1_img/chapter_01_1.png",delay=(4))
    display_with_image(f"And yet","img_file/chapter_1_img/chapter_01_2.png",delay=(4))
    display_with_image(f"This is how you go...!","img_file/chapter_1_img/chapter_01_3.png",delay=(2))
    display_with_image(f"URRRRRRGH","img_file/chapter_1_img/chapter_01_3.png",delay=(4))
    display_with_image(f"MASTER","img_file/chapter_1_img/chapter_01_4.png",delay=(4))
    display_image(f"img_file/chapter_1_img/chapter_01_5.png",delay=(3))
    display_image(f"img_file/chapter_1_img/chapter_01_6.png",delay=(3))
    display_image(f"img_file/chapter_1_img/chapter_01_7.png",delay=(3))
    start_narration_1()

def start_narration_1():
    display_with_image(f"You and your master was attacked by Martial artist from the Light faction",delay=(3))
    display_with_image(f"The Three Sword of Qingcheng","img_file/narration_1_img/narration_1_img.png",delay=(3))
    display_with_image(f"Lead by The {Bosses[-1]} of Qingcheng Sect","img_file/narration_1_img/narration_1_img.png",delay=(3))
    display_with_image(f"The Mount Hua Sect {Bosses[-2]}","img_file/narration_1_img/narration_2_img.png",delay=(2))
    display_with_image(f"The Highly Esteemed Exorcist Squad","img_file/narration_1_img/narration_3_img.png",delay=(2))
    display_with_image(f"Lord of the Martial Alliance {Bosses[0]}","img_file/narration__img/narration_4_img.png",delay=(2))
    start_chaper_1_1()

def start_chaper_1_1():
    display_with_image(f"{player_name}--Let me ask you a question","img_file\chapter_1_1_img\chapter_1_1_1.png",delay=(2))
    display_image(f"img_file\chapter_1_1_img\chapter_1_1_2.png",delay=(1))
    display_with_image(f"{Bosses[-2]}--Go Head","img_file\chapter_1_1_img\chapter_1_1_3.png",delay=(2))
    display_image(f"img_file/chapter_1_1_img/chapter_1_1_4.png",delay=(1))
    display_with_image(f"{player_name}--I Know the people who gathered here are neither fools","img_file\chapter_1_1_img\chapter_1_1_5.png",delay=(2))
    display_with_image(f"So it also should be apparent that my master and i did not practiice the vile demonic art","img_file\chapter_1_1_img\chapter_1_1_6.png",delay=(2))
    display_image(f"img_file\chapter_1_1_img\chapter_1_1_7.png",delay=(1))
    display_with_image(f"Let us speak honestly then","imgfile\chapter_1_1_img\chapter_1_1_8.png",delay=(2))
    display_with_image(f"WHY DID YOU DO THIS!!","img_file\chapter_1_1_img\chapter_1_1_9.png",delay=(2))
    display_with_image(f"HE DEVOTED HIS WHOLE LIFE TO THE MARTIAL SOCIETY","img_file\chapter_1_1_img\chapter_1_1_9.png",delay=(2))
    display_with_image(f"SO WHY!!!","img_file\chapter_1_1_img\chapter_1_1_10.png",delay=(3))
    display_image(f"img_file\chapter_1_1_img\chapter_1_1_11.png",delay=(2))
    start_narration_1_1()

def start_narration_1_1():
    display_with_image(f"Half a year ago","img_file/narration_1_1_img/narration_1_1_1.png",delay=(2))
    display_with_image(f"A rumour started to spread","img_file/narration_1_1_img/narration_1_1_2.png",delay=(2))
    display_with_image(f"That the text of the vile and atrocious silent ten skills of the demon, Was in our possession.","img_file/narration_1_1_img/narration_1_1_2.png",delay=(2))
    display_with_image(f"Some went as far to say that we had already learned it ourselves","img_file/narration_1_1_img/narration_1_1_3.png",delay=(2))
    display_with_image(f"When we tried to protest these lies and proclaim our innocent.","img_file/narration_1_1_img/narration_1_1_4.png",delay=(2))
    display_with_image(f"No one listen","img_file/narration_1_1_img/narration_1_1_5.png",delay=(2))
    display_with_image(f"Later,we were visted by martial artists looking to verify the rumours themselves","img_file/narration_1_1_img/narration_1_1_6.png",delay=(2))
    display_with_image(f"Swearing upon the heavens that the book was not here.","img_file/narration_1_1_img/narration_1_1_7.png",delay=(2))
    display_with_image(f"My master cooperated with their investigation","img_file/narration_1_1_img/narration_1_1_8.png",delay=(2))
    display_with_image(f"Although we had accumulated vast literatures on martial arts.","img_file/narration_1_1_img/narration_1_1_9.png",delay=(2))
    display_with_image(f"We could say for certain that neither the silent ten skills of the demon, nor anything associated with it was in our possession.","img_file/narration_1_1_img/narration_1_1_9.png",delay=(2))
    display_with_image(f"But How.....","img_file/narration_1_1_img/narration_1_1_10.png",delay=(2))
    display_with_image(f"Was the Godforsaken text here....!","img_file/narration_1_1_img/narration_1_1_10.png",delay=(2))
    start_chapter_1_2()

def start_chapter_1_2():
    display_with_image(f"It is somone here..Trying to frame us and get rid of us","img_file/chapter_1_2_img/chapter_1_2_1.png",delay=(2))
    display_with_image(f"{player_name}--You have mouth so speak.","img_file/chapter_1_2_img/chapter_1_2_2.png",delay=(2))
    display_with_image(f"WHAT ARE YOU ALL DOING.","img_file/chapter_1_2_img/chapter_1_2_3.png",delay=(2))
    display_with_image(f"{Bosses[0]}--HOW LONG ARE YOU GOING TO LET THAT VILE KID SPOUT BULLSHIT","img_file/chapter_1_2_img/chapter_1_2_4.png",delay=(2))
    display_with_image(F"{player_name}=={Bosses[0]}","img_file/chapter_1_2_img/chapter_1_2_5.png",delay=(2))
    display_with_image(f"That right you were always envious of my master, My master surpassed you in both technique and personality,I am sure that is why you cannot tolerate him.","img_file/chapter_1_2_img/chapter_1_2_6.png",delay=(2))
    display_image(f"img_file/chapter_1_2_img/chapter_1_2_7.png",delay=2)
    display_with_image(f"{Bosses[0]}--Looks like your master never taught you,the consequences of speaking out of line","img_file/chapter_1_2_img/chapter_1_2_8.png",delay=(2))
    display_with_image("HO HO HO.","img_file/chapter_1_2_img/chapter_1_2_9.png",delay=(2))
    show_fight_chioce()

def show_input_screen():
    for widget in root.winfo_children():
        widget.destroy()

    instruction = Label(root, text="What is thy name?", font=("Arial", 14),
                        fg="#ffcc00", bg="#1a1a1a")
    instruction.pack(pady=10)
        
    global player_name_box            #making player_name useable
    player_name_box = Entry(root, font=("Arial", 14), justify="center")
    player_name_box.pack(pady=10)
    player_name_box.focus_set()
        
    submit_btn = Button(root, text="Begin Journey", command=submit_name,
                        font=("Arial", 12, "bold"), bg="#333", fg="white")
    submit_btn.pack(pady=20)

def show_fight_chioce():
    for widget in root.winfo_children():
        widget.destroy()

    display_with_image(f"{Bosses[0]} is taunting you! Fight or die.","img_file/fight_1_img/fight_1.png",delay=0)
    Button(root, text="FIGHT (One Final Strike)", command=execute_fight,
           bg="#800", fg="white", font=("Arial", 12, "bold"), width=25).pack(pady=10)
    Button(root, text="RUN (Coward's End)", command=handle_run,
           bg="#444", fg="white", font=("Arial", 12), width=25).pack(pady=10)

def execute_fight():
    gyul_health_bar=int(100)
    player_health_bar=int(100)

    gyul_hit=random.randint(20,30)
    player_hit=random.randint(35,50)

    final_gyul_hp=gyul_health_bar-player_hit
    final_player_hp=player_health_bar-gyul_hit
    
    display_with_image(f"img_file/fight_1_img/fight_1_2.png",delay=2)
    display_with_image(f"You have hit for {player_hit}","img_file/fight_1_img/fight_1_3.png",delay=(2))
    display_with_image(f"JWA DO-GYUL--HoW DARE YOU!","img_file/fight_1_img/fight_1_5.png",delay=(2))
    display_with_image(f"You were hit for {gyul_hit}","img_file/fight_1_img/fight_1_4.png",delay=(2))
    display_with_image(f"{Bosses[0]} lost 3 fingers","img_file/fight_1_img/fight_1_7.png",delay=(2))
    display_with_image(f"You were hit across the shoulder","img_file/fight_1_img/fight_1_6.png",delay=(2))

    status_text=(f"{Bosses[0]} Health {final_gyul_hp}\n\nYour Health {final_player_hp}")
    display_text(status_text,delay=(2))
    root.destroy()
    
    
def handle_run():
    for r in range(1, 11):
        path = f"img_file/fight_1_img/run_1_img/run_1_{r}.png"
        display_with_image(f"You were stabbed in the back. Your story ends here.", path, delay=2)
        sys.exit()
    start_chaper_1_3()

def start_chaper_1_3():
    display_with_image(f"Surprising!!","img_file/chapter_1_3_img/chapter_1_3_1.png",delay=2)
    display_with_image(f"He still stands","img_file/chapter_1_3_img/chapter_1_3_1.png",delay=2)
    display_image(f"img_file/chapter_1_3_img/chapter_1_3_2.png",delay=2)
    display_image(f"img_file/chapter_1_3_img/chapter_1_3_3.png",delay=2)
    display_with_image(f"Have you actually learned demonic arts,little demon","img_file/chapter_1_3_img/chapter_1_3_4.png",delay=2)
    display_with_image(f"You look pretty exhusted huh!!","img_file/chapter_1_3_img/chapter_1_3_5.png",delay=2)
    display_image(f"img_file/chapter_1_3_img/chapter_1_3_6.png",delay=2)
    display_image(f"img_file/chapter_1_3_img/chapter_1_3_7.png",delay=2)
    display_with_image(f"I'll give thise three fingers of mine as a gift for you to the afterlife","img_file/chapter_1_3_img/chapter_1_3_8.png",delay=2)
    display_with_image(f"Lord what happened","img_file/chapter_1_3_img/chapter_1_3_9.png",delay=2)
    display_with_image(f"oh","img_file/chapter_1_3_img/chapter_1_3_10.png",delay=2)
    display_with_image(f"Relax, we have slain the wrethed demon and its child","img_file/chapter_1_3_img/chapter_1_3_11.png",delay=2)
    display_with_image(f"BASTARD!!","img_file/chapter_1_3_img/chapter_1_3_12.png",delay=2)
    display_with_image(f"You're still alive....it must be because you have learned demonic arts.","img_file/chapter_1_3_img/chapter_1_3_13.png",delay=2)
    display_with_image(f"HEH HEH....i will be generous.","img_file/chapter_1_3_img/chapter_1_3_14.png",delay=2)
    display_with_image(f"Since you have a long journey ahead","img_file/chapter_1_3_img/chapter_1_3_15.png",delay=2)
    display_image(f"img_file/chapter_1_3_img/chapter_1_3_16.png",delay=2)
    display_with_image(f"Take some time to have a chat with each other","img_file/chapter_1_3_img/chapter_1_3_17.png",delay=2)
    display_with_image(f"HAAAH....so this is the end of the line.","img_file/chapter_1_3_img/chapter_1_3_18.png",delay=2)
    display_with_image(f"Master, I am sorry... this is it for me.","img_file/chapter_1_3_img/chapter_1_3_19.png",delay=2)
    display_image(f"img_file/chapter_1_3_img/chapter_1_3_20.png",delay=2)
    display_with_image(f"I told you we should not have been so kind and naive.","img_file/chapter_1_3_img/chapter_1_3_20.png",delay=2)
    display_with_image(f"Master....","img_file/chapter_1_3_img/chapter_1_3_21.png",delay=2)
    display_with_image(f"if only i could live once more","img_file/chapter_1_3_img/chapter_1_3_21.png",delay=2)
    display_image(f"img_file/chapter_1_3_img/chapter_1_3_21.png",delay=2)
    display_with_image(f"{Bosses[0]}...I will be sure to get revenge against him.","img_file/chapter_1_3_img/chapter_1_3_22.png",delay=2)
    display_with_image(f"Master, do not be so kind and foolish in the ""img_file/chapter_1_3_img/chapter_1_3_23.png",delay=3)
    display_image(f"img_file/chapter_1_3_img/chapter_1_3_23.png",delay=3)

#GUI window
root = tk.Tk()
root.title("The Chronicles of Heavenly Martial Arts")
root.geometry("900x700")
root.configure(bg="#1a1a1a")

show_input_screen()
root.mainloop()
