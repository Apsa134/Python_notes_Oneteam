from my_package import module

num = int(input("Enter the number:"))

print(module.is_even(num))
print(module.hi())

#GTTS

from gtts import gTTS
import os
speech = gTTS(text ="Hai am Biyona, how are you?",lang ='en')
speech.save("sample.mp3")
os.system("start sample.mp3")