import time
from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Calibri.ttf', size=90)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-90, 10), '5', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

if __name__ == '__main__':
    image = Image.open('test.jpg')
    #image.width()
    image.show()
    add_num(image)
    image.show()
