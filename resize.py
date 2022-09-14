from PIL import Image
import os

height = 512
width = 512

def resizer(infile):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        new_img = im.resize((height, width), Image.ANTIALIAS)
        new_img.mode = 'RGB'
        new_img.save(file + "_resized.jpg", "JPEG")


if __name__ == '__main__':
    resizer('uploads/2022-09-03_13-34-19.png')