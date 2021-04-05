from gtts import gTTS  # imported this module for text to speech conversion
import os

file = open('sample.txt')  # text that you want to convert from the file
text = file.read()

language = 'en'  # en is for english

obj = gTTS(text = text, lang = language, slow = False)
# we have used slow because our converted video will have high speed
obj.save("sample.mp3")

# to open the video file automatically we have to import os

os.system("sample.mp3")
