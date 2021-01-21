import PyPDF2

import pyttsx3
def speaker(audio):
    engine = pyttsx3.init('sapi5')
    voices= engine.getProperty('voices') #getting details of current voice
    engine.setProperty('voice', voices[1].id)
    engine.say(audio) 
    engine.runAndWait()
a = PyPDF2.PdfFileReader("ramya.pdf")
str = ""
for i in range(1,5):
    str += a.getPage(i).extractText()

with open("machine.txt" , 'w' , encoding="utf-8") as wr:
    wr.write(str)
with open("machine.txt"  ) as wr1:
    a= wr1.read()

speaker(a)