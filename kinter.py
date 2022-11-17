# Import Module
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from fpdf import FPDF
r = sr.Recognizer()
def pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    f = open("myfile.txt", "r")
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')
    pdf.output("notes.pdf")
#GUI related dependencies 
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
def speech():
    exec(open("speech.py").read())
def speechtotext():
    exec(open("speechtotext.py").read())
def pdf():
    exec(open("pdf.py").read())
    print("pdf saved to device successfully")
def mailpdf():
    exec(open("mail.py").read())
# Create Tkinter Object
root = tk.Tk()
root.minsize(width=500,height=500)
root.title("Tech Zombies GUI for Automated notes maker from Audio Recordings")
# Read the Image of ui from figma
image = Image.open("Slide1.png")
# Resize the image using resize() method
resize_image = image.resize((850, 700))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label2 = tk.Label(root,image=img)
label2.pack()
label3=tk.Label(text='Tech Zombies Presents', font=("Century Schoolbook",16 ,"bold"),bg="#ffffff")
label3.place(relx=0.31,rely=0.17,expand=True)
#button1=tk.Button(command=hai,text="click this")
#button1.place(relx=0.5,rely=0.7)
label4=tk.Label(text='Automated Notes Maker from Audio Recordings', font=("Bahnschrift Light SemiCondensed",11),bg="#ffffff")
label4.place(relx=0.32,rely=0.23)
label4=tk.Label(text='Would You like to Record or Upload your Audio ?',font=("Poplar Std",11),bg="#ffffff")
label4.place(relx=0.315,rely=0.28)
w =tk.Checkbutton(text="Record",font=("Orator Std",11),bg="#ffffff")
w.place(relx=0.315,rely=0.315)
x=tk.Checkbutton(text="Upload",font=("Orator Std",11),bg="#ffffff")
x.place(relx=0.315,rely=0.355)
label5=tk.Button(command=speech,text="Click here to start recording",activebackground="#f49d6e",borderwidth=0,font=("Arial",14 ),bg="#FE6F4F",fg="white")
label5.place(relx=0.37,rely=0.409)
label7=tk.Label(text="Salient Features",font=("Arial",12 ),bg="#ffffff")
label7.place(relx=0.33 ,rely=0.59)
label8=tk.Label(text="Free and easy to use",font=("Calibri",11),bg="#ffffff")
label8.place(relx=0.33,rely=0.63)
label9=tk.Label(text="Provides accurate and precise conversion of audio to pdf",font=("Calibri",11) ,bg="#ffffff")
label9.place(relx=0.33,rely=0.66)
label10=tk.Label(text="Acts as a mediator in form of speech signals ",font=("Calibri",11),bg="#ffffff")
label10.place(relx=0.33,rely=0.69)
btn = tk.Button(text="Are you ready to save pdf?",bg='#FCC863',font=("Calibri",11),borderwidth=0,command=pdf,activebackground="#ffb17a")
btn.place(relx=0.32,rely=0.73)
btn3 = tk.Button(text="Wanna Mail  the PDF?",bg='#FCC863',font=("Calibri",11),borderwidth=0,command=mailpdf,activebackground="#ffb17a")
btn3.place(relx=0.53,rely=0.73)
label6=tk.Button(command=speechtotext,borderwidth=0,text="Click here to convert Uploaded Audio File",activebackground="#f49d6e",font=("Arial",11,"bold"),bg="#FE6F4F",fg="white")
label6.place(relx=0.325,rely=0.79)
last=tk.Label(text='Copyrights 2022 ©. All Right Reserved. Thiagarajar College Of Engineering',font=("Arial",8,"bold"),bg="#ffffff")
last.place(relx=0.274,rely=0.88)
# Execute Tkinter
root.mainloop()
