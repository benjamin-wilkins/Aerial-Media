from os import listdir
from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/videos")
def videos():
    videos = listdir("static/videos")
    return render_template("videos.html", videos=videos)

@app.route("/pictures")
def pictures():
    pictures = listdir("static/pictures")
    return render_template("pictures.html", pictures=pictures)

@app.route("/audio")
def audio():
    audio = listdir("static/audio")
    return render_template("audio.html", audio=audio)

if __name__ == "__main__":
    app.run(host="192.168.1.95", port=5000, debug=False)
