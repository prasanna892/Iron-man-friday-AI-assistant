from gtts import gTTS
import os
text1 = "man"
language = "ta"
obj = gTTS(text=text1, lang=language,slow=False)
obj.save("tamil.mp3")
os.system("start tamil.mp3")