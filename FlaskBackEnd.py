from flask import Flask, render_template, request, send_from_directory
import os
from bs4 import BeautifulSoup
from accessibilitySoup import Soup

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'html'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file uploaded', 400

        file = request.files['file']
        filename_save_as = request.form.get("filename", "processed.html")

        if file.filename == '':
            return 'No selected file', 400

        if file and allowed_file(file.filename):
            # Use your Soup class to process the file
            soup_instance = Soup(file)
            soup_instance.standardized()
            path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], filename_save_as)
            soup_instance.savefile(path_to_save)

            # Here, we redirect the user to the download route
            return render_template("index.html", file_ready=True, file_name=filename_save_as)

    return render_template('index.html', file_ready=False)

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    return send_from_directory(directory=app.config["UPLOAD_FOLDER"], filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

