
from PIL import Image
import os, math, time, re
import tkinter as tk
from tkinter import simpledialog
max_sprites_row = 1
max_frames_row = 96

frames = []

tile_width = 0
tile_height = 0

spritesheet_width = 0
spritesheet_height = 0

folder_names = ['screen', 'roll', 'printer', 'open']

for name in folder_names :
    path = 'E:/Users/Francois/Pictures/nuances4/nuances4-anim/nuances4_AME/' + name + "/"

    files = os.listdir(path)

    file_title = re.search(".+?(?=[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9]|[0-9][0-9]|[0-9]&\.)", files[0]).group(0)

    for current_file in files :
        try:
            with Image.open(path + current_file) as im :
                frames.append(im.getdata())
        except:
            print(current_file + " is not a valid image")

    tile_width = frames[0].size[0]
    tile_height = frames[0].size[1]

    if len(frames) > max_frames_row :
        spritesheet_width = tile_width * max_frames_row
        required_rows = math.ceil(len(frames)/max_frames_row)
        spritesheet_height = tile_height * required_rows
    else:
        spritesheet_width = tile_width*len(frames)
        spritesheet_height = tile_height

    spritesheet = Image.new("RGBA",(int(spritesheet_width), int(spritesheet_height)))

    for current_frame in frames :
        top = tile_height * math.floor((frames.index(current_frame))/max_frames_row)
        left = tile_width * (frames.index(current_frame) % max_frames_row)
        bottom = top + tile_height
        right = left + tile_width
        
        box = (left,top,right,bottom)
        box = [int(i) for i in box]
        cut_frame = current_frame.crop((0,0,tile_width,tile_height))
        
        spritesheet.paste(cut_frame, box)

    spritesheet.save(file_title + time.strftime("%Y-%m-%dT%H-%M-%S") + ".png", "PNG")
