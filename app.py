from doctest import debug
from flask import Flask, render_template,jsonify, request, url_for, redirect, send_file, session
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"

@app.route("/", methods = ["GET", "POST"])
def index():return render_template("youtube.html")

@app.route("/youtube", methods = ["GET", "POST"])
def youtube():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return jsonify({'error': "Invalid URL! Please Provide a valid YouTube URL"})
        data = {
            "url" : url.thumbnail_url,
            "title": url.title,
            "stream": {i.itag: i.resolution for i in url.streams.filter(progressive=True)}
        }
        return jsonify(data)

@app.route("/facebook")
def facebook():
    return render_template("facebook.html")

@app.route("/instagram")
def instagram():
    return render_template("instagram.html")

@app.route("/download", methods = ["GET", "POST"])
def download_video():
    if request.method == "POST":
        buffer = BytesIO()
        url = YouTube(session['link'])
        itag = request.form.get("itag")
        video = url.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=url.title, mimetype="video/mp4") 
    return render_template('error.html', error="There is an error whil downloading your file please try again later")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)