#!/usr/bin/python
# -*- coding: utf-8 -*-

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import urllib2
import io,sys
from time import *
from PIL import Image
import PIL.ImageOps
import ImageDraw
import ImageFont


SLEEP_TIME  = 30
RST = 24


url = "https://info.weather.yandex.net/24/3_white.ru.png?domain=ru"

tmp_file = '/tmp/wather.png'


def GetImage(url, Invert=True):
    try:
        url2 = urllib2.urlopen(url)
        data = url2.read()
        #default 175x114
        image = Image.open(io.BytesIO(data))
        try:
            image.save(tmp_file)
        except:
            print "write file error"
        #convert to 128x32
        #image = image.crop( (11,35,165,74))
        image = image.crop( (20,40,100,95))
        if Invert:
            image = image.convert("L")
            image = PIL.ImageOps.invert(image)
        image = image.resize((128,64))
        image = image.convert('1')
        return image
    except:
        return None


if len(sys.argv) > 1:
    invert = False
else:
    invert = True


disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

image = GetImage(url, invert)
if image <> None:
    disp.image(image)
else:
    text = "fail connect"
    line = 1
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', size=16)


    width = disp.width
    height = disp.height

    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    text_h = draw.textsize(text, font)[1]
    draw.rectangle((0, line * text_h ,width,height), outline=0, fill=0)
    draw.text((0, line * text_h ), text,  font=font, fill=255)

    line  = 4
    text = strftime("%d-%m-%Y %H:%M")
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', size=12)
    text_h = draw.textsize(text, font)[1]
    draw.text((0, line * text_h ), text,  font=font, fill=255)
    
    disp.image(image)
        
    

disp.display()


