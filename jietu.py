from selenium import webdriver  # 从selenium库导入webdirver
import os
from PIL import Image,ImageDraw,ImageFont
import time
from time import sleep

def jietu(url):
    brower = webdriver.PhantomJS()

    brower.get(url)

    try:
        element=brower.find_element('css selector', '.prom-sum')
        element.click()
    except:
        pass
    brower.maximize_window()
    title=brower.title
    brower.save_screenshot('./screen_shot/%s.png'% title)
    print(brower.title)
    brower.close()
    print('close')

    #
    # for img in os.listdir('./screen_shot'):
    #     if img.endswith('.png'):
    #         print('%s裁剪中。。' % img)
    im = Image.open('./screen_shot/%s.png' % title)
    x = 0
    y = 315
    w = 1920
    h = 850
    region = im.crop((x, y, x + w, y + h))
    font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.TTF',40)
    draw = ImageDraw.Draw(region)
    draw.text((1350,700),time.asctime( time.localtime(time.time()) ),fill='black', font=font)
    region.save("./screenshot_final/%s.png" % title)

# #
f = open('url.txt')
line = f.readlines()
for l in line:
    url= l
    print(url)
    jietu(url)
