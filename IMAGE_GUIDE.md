# Adding Images to Your Game - Quick Guide

## How to Use Images in Your Game

### 1. **Display Text Only** (Default)
```python
display_text("Your narrative text here", delay=2)
```

### 2. **Display Text WITH an Image** (New!)
```python
display_with_image("Your narrative text here", "img_file/image_name.png", delay=3)
```

## File Structure
Make sure your images are in the `img_file` folder:
```
my_python_game/
├── img_file/
│   ├── master_scene.png
│   ├── three_sword.png
│   ├── boss_fight.png
│   └── ... more images
└── my_python_game_VB/
    └── Python_Heavenly_User_Game.py
```

## Examples

### Example 1: Scene with Boss Image
```python
display_with_image(f"{name}--You have mouth so speak.\nLet us speak honestly!", 
                   "img_file/jwa_do_gyul.png", delay=3)
```

### Example 2: Flashback with Master
```python
display_with_image(f"Master--Tell me, what is the most important quality of a martial artist?", 
                   "img_file/master_flashback.png", delay=3)
```

### Example 3: Fight Scene
```python
display_with_image(f"You strike with your spear!\nDamage dealt: {hit}", 
                   "img_file/combat_scene.png", delay=2)
```

## Important Notes

1. **Image Path**: Always use relative path from the workspace root: `"img_file/image_name.png"`
2. **Image Size**: Images are automatically resized to fit (max 800x300 pixels)
3. **File Format**: Supports PNG, JPG, GIF, and other common formats
4. **Delay**: Set the delay in seconds (delay=2 means display for 2 seconds)
5. **Optional**: If the image file doesn't exist, the text will still display

## How Images are Displayed

The GUI window will:
- Display the image at the top
- Show your narrative text below it
- Wait for the specified delay time
- Then clear and display the next scene

## Installation Requirements

Your game now requires:
- `tkinter` (usually included with Python)
- `Pillow` (PIL) - install with: `pip install Pillow`

## Current Implementation

Your game has been updated with two helper functions:

1. **`display_text(text, delay=2)`** - Display text only
2. **`display_with_image(text, image_path, delay=2)`** - Display text + image

Both are already imported and ready to use throughout your game!

## Tips for Best Results

- Use high-quality images (PNG recommended)
- Keep images consistent in style for immersion
- Use appropriate delays so readers can see the image
- Consider the narrative flow when placing images
- Test on your target resolution (default: 900x700)

Good luck with your game! 🎮
