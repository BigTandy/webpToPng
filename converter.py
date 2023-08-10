# Bud Patterson
# WebP to PNG Converter
# Aug 9 2023


import os
from PIL import Image


if not os.path.exists("./webp"):
    os.makedirs("./webp")

ps = [f for f in os.listdir('.') if f.endswith('.webp')]

print(ps)



for im in ps:
    img = Image.open(im).convert('RGB')
    img.save(f"{im[:-5]}.png", 'png')
    os.rename(f'./{im}', f'./webp/{im}')

