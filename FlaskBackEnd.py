from flask import Flask, render_template, request, send_from_directory
from bs4 import BeautifulSoup
import os
# Assuming the accessibilitySoup is in the same directory
from accessibilitySoup import *

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        savepath = request.form.get('savepath')

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            
            with open(filepath, 'r') as file:
                content = file.read()
                soup = BeautifulSoup(content, 'html.parser')
                # Call the functions you defined in 'accessibilitySoup' to process the soup
                # ... (like htmlTag(soup), headTag(soup), etc.)

            processed_filepath = os.path.join(PROCESSED_FOLDER, file.filename)
            with open(processed_filepath, 'w') as file:
                file.write(str(soup))

            return send_from_directory(PROCESSED_FOLDER, file.filename, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(PROCESSED_FOLDER):
        os.makedirs(PROCESSED_FOLDER)
    app.run(debug=True)
