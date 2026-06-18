# Heavenly User Game - Text-Based Adventure Framework

An interactive, graphic-assisted, text-based RPG storytelling game built with Python using `tkinter` for the user interface and Pillow (`PIL`) for dynamic image asset rendering. The application pairs dialog and multi-choice state transitions with background scenes to create an immersive visual novel style experience.

---

## Key Features

- **Event-Driven UI Management:** Uses Python's native `tkinter` interface to handle screen elements dynamically, sweeping away historical layouts via widget purging (`winfo_children().destroy()`) upon event transitions.
- **Dynamic Asset Pipeline:** Employs the Pillow (PIL) imaging module to process asset formats. Uses high-quality LANZOS downsampling to constrain scenery illustrations into unified dimensions (`800x300`) across canvas changes.
- **Adaptive Input Sanitization:** Replaces file system path patterns (`\\` to `//`) to guarantee cross-compatibility between Unix-like and Windows execution environments.
- **Procedural Pacing Control:** Synchronizes scene changes with customizable timeline delays using the `time` module, letting the user experience dialogue steps naturally.

---

## Required Assets Setup

The game relies on localized assets to run without throwing soft rendering errors. Ensure your repository directory layout matches this structure:

```
my_game_project/
│
├── Python_Heavenly_User_Game.py    # Main game engine file
└── img_file/                       # Imagery storage directory
    └── chapter_1_3_img/            # Chapter 1 scene files
        ├── chapter_1_3_15.png
        ├── chapter_1_3_16.png
        ├── chapter_1_3_17.png
        └── ... (chapter artwork assets)

## Installation and Setup
Prerequisites
- Python 3.x installed.
- Pillow image processing package.

## Configuration Instructions
= Install the third-party Pillow requirements library:
```
pip install Pillow
```
- Run the application from your root directory:
```
python Python_Heavenly_User_Game.py
```

## Core Logic Methods Overview
display_with_image(text, image_path=None, delay=2)
- The central la-yout director of the script. It:

- Clears out existing interface panels so memory allocations do not overlap.

- Verifies file system boundaries for image assets, generating fallback shell panels gracefully if paths fail.

- Renders synchronized subtitle cards under image elements to drive chapter transitions.

## Author
- Name: Kazeem Olalekan Sola-Raji
