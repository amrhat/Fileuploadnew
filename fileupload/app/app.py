from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')  # GUI anzeigen

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return "Datei hochgeladen!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
