from flask import Flask, render_template, request, url_for, redirect, send_file, session
from pytube import YouTube
# from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"

@app.route("/", methods = ["GET", "POST"])
@app.route("/youtube", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return render_template("error.html")
        return render_template("youtube.html", url = url, download=True)
    return render_template("youtube.html")

@app.route("/facebook")
def facebook():
    return render_template("facebook.html")

@app.route("/instagram")
def instagram():
    return render_template("instagram.html")

@app.route("/download", methods = ["GET", "POST"])
def download_video():
#     if request.method == "POST":
#         buffer = BytesIO()
#         url = YouTube(session['link'])
#         itag = request.form.get("itag")
#         video = url.streams.get_by_itag(itag)
#         video.stream_to_buffer(buffer)
#         buffer.seek(0)
#         return send_file(buffer, as_attachment=True, download_name=url.title, mimetype="video/mp4")
    return redirect(url_for("home"))

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run()