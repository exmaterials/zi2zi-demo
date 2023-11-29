from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt
import os
import numpy as np
import pathlib
import argparse

def draw_single_char(ch, font, canvas_size, x_offset, y_offset):
    img = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((x_offset, y_offset), ch, (0, 0, 0), font=font)
    return img

def draw_example(ch, src_font, canvas_size, x_offset, y_offset):
    src_img = draw_single_char(ch, src_font, canvas_size, x_offset, y_offset)
    example_img = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))
    example_img.paste(src_img, (0, 0))
    return example_img

def generate_font_image(src_font, chara, img_size = 80, chara_size = 60, x_offset = 0, y_offset = 0):
    font = ImageFont.truetype(src_font, size = chara_size)
    if(x_offset != 0 or y_offset != 0):
        img = draw_example(chara, font, img_size, x_offset, y_offset)
    else:
        img = draw_example(chara, font, img_size, (img_size-chara_size)/2, (img_size-chara_size)/2)
    return img

def plot(img):
    plt.figure()
    plt.imshow(img)
    plt.axis('off')  # Optional: Turn off the axis labels
    plt.show()

if __name__ == '__main__':

    src_font = './ttf_folder/01-柳公权柳体.ttf'
    chara = '柳'

    img = generate_font_image(src_font, chara,
                              img_size   = 80,
                              chara_size = 60,
                              x_offset   = 0,
                              y_offset   = 0)

    plot(img)