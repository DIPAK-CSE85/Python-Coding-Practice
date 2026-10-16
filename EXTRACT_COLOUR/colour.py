# program to extract colors from any image
# install dependency first: pip install colorgram.py
from pathlib import Path
import colorgram

image_path = Path(__file__).with_name("dipak.jpg")
colors = colorgram.extract(str(image_path), 10)  # pass image name and how many colors you want

color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))  # store each color as a tuple in the list

print(color_list)  # used to print the list