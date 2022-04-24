from nis import cat
from flask import Flask, render_template, request, session
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    if(request.method == 'POST'):
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except Exception as e:
            return render_template('error.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)