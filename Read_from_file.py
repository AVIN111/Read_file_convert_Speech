from gtts import gTTS 
import os

ta = open("read.txt","r") 
m = ta.read().replace("\n"," ")
lang = 'en'

output = gTTS(text=m, lang=lang, slow=False)

output.save("output.mp3")
ta.close()
os.system("start output.mp3")