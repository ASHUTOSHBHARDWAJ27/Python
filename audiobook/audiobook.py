import pyttsx3
import PyPDF2
from tkinter.filedialog import *
import os
book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(open(book, 'rb'))
pages = pdfreader.numPages

print ("NOTE : counting start from 0")
i = int(input("Enter the page you want to start read:"))

print(pages)

for num in range(i,pages):
    text= pdfreader.getPage(num).extractText()
    
    print(text)
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()

