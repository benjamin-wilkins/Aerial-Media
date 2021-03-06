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

@app.route("/videos/new", methods=["POST"])
def newvid():
    f = request.files["file"]
    name = f.filename
    location = "static/videos/" + name
    f.save(location)
    f.close()
    return redirect(url_for(videos))

@app.route("/pictures/new", methods=["POST"])
def newpic():
    f = request.files["file"]
    name = f.filename
    location = "static/pictures/" + name
    f.save(location)
    f.close()
    return redirect(url_for(pictures))

@app.route("/audio/new", methods=["POST"])
def newaud():
    f = request.files["file"]
    name = f.filename
    location = "static/audio/" + name
    f.save(location)
    f.close()
    return redirect(url_for(audio))

@app.route("/video/<video>")
def vidplayer(video):
    return render_template("video-player.html", video=video)

@app.route("/picture/<picture>")
def picplayer(picture):
    return render_template("picture-player.html", picture=picture)

@app.route("/sound/<audio>")
def audplayer(audio):
    return render_template("audio-player.html", audio=audio)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
