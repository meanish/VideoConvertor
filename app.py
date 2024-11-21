import moviepy
from tkinter.filedialog import *

vid = askopenfilename()
video = moviepy.VideoFileClip(vid)


audio = video.audio

# right audio file
audio.write_audiofile("audioconvo.mp3")

print("Sucessfully converted and download")



print(dir(moviepy))