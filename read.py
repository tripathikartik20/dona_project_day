from PIL import Image
import cv2
import pytesseract
from textblob import TextBlob
import webp
import os
import shutil
dest="C:/Users/PREDATOR/Desktop/dona/dona_project_day/gif_data/"
op_dest="C:/Users/PREDATOR/Desktop/dona/dona_project_day/filtered_data/"
for i in range(107):
    ip=dest+str(i)+".webp"
    op = f"{dest}tmp.gif"
    anim = webp.load_images(ip)
    anim[0].save(op, save_all=True, append_images=anim[:1], duration=1, loop=0)
    im = Image.open(op)
    im.seek(0)
    im.save("tmp.png")
    img=cv2.imread("tmp.png")
    try:
        crop_img = img[0:170,200:470]
        txt = pytesseract.image_to_string(crop_img)
    except Exception:
        txt=""
    word=txt.replace("\n", "")
    word=word.replace(" ", "")
    word = ''.join(filter(str.isalnum, word))
    word=word.lower()
    b = TextBlob(word)
    ans=str(b.correct())
    print(f"corrected text: {ans}")
    fname = op_dest+ans+".webp" if ans else f"{op_dest}unknown{str(i)}.webp"
    shutil.copyfile(ip, fname)
