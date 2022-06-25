from doctest import debug
from flask import Flask, render_template,jsonify, request, send_file, session, send_from_directory
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

@app.route("/download", methods = ["POST"])
def download_video():
    if request.method == "POST":
        buffer = BytesIO()
        url = YouTube(session['link'])
        itag = request.form.get("itag")
        video = url.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=url.title+'.mp4', mimetype=video.mime_type) 
    return jsonify({'error': 'Something went wrong'})

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)