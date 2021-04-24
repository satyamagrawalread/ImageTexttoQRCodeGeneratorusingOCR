import pytesseract as py
py.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import qrcode

from tkinter import *
from tkinter import filedialog
import os 
import tkinter as tk
from PIL import Image, ImageTk

def showimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG file", "*.png"), ("All Files", "*.*")))
    img = Image.open(fln)
    # text = py.image_to_string(img)
    img.thumbnail((600, 600))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    img1 = cv2.imread(fln)
    text = py.image_to_string(img1)
    print(text)
    img_qr = qrcode.make(text)
    img_qr.save("mini.jpg")

root = Tk()



frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="Browse Image", command=showimage)
btn.pack(side=tk.LEFT)

btn2 = Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)

root.title("Image Brower")
root.geometry("600x700")
root.mainloop()