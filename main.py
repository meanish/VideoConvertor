from flask import Flask, request, send_file
from flask_cors import CORS
from moviepy import VideoFileClip  #foraskfilename that provides file path on same dir
import os

app = Flask(__name__) #mandatory using app route
CORS(app)  # allow cross origin with react front


#create a dir folder and to store download 
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)


@app.route('/convert', methods=['POST']) #post req
def convert_video():

    video_file = request.files['video']

    print(dir(video_file)) #provide all infor about the video_file uploaded

    video_path = os.path.join(TEMP_DIR, video_file.filename) #video temp store dir used for convertor
    audio_path = os.path.join(TEMP_DIR, "audioconvo.mp3") # download store in temp 


   # store temporarily until the convertor is done
    video_file.save(video_path)

#try catch exception in py

    try:
         # Convert video to audio
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)
        print("Convertion Done SucessFully")
    except Exception as e:
        return str(e), 500
    finally:
        video.close() # ensuring the video file is closed

    # sending the audio file to the client
    return send_file(audio_path, as_attachment=True)

# run the app
if __name__ == '__main__':
    app.run(debug=True) #flash run on port 5000 on default
