from flask import Flask, redirect, url_for, request, render_template
from PIL import Image
import numpy as np
import base64
import re
from io import BytesIO
import os
from werkzeug import secure_filename

app = Flask(__name__, static_url_path='')
app.debug= True

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def get_image():
    image_b64 = request.values['imageBase64']
    image_data = re.sub('^data:image/.+;base64,', '', image_b64)
    image_PIL = Image.open(BytesIO(base64.b64decode((image_data))))
    filename = request.values["filename"]
    image_PIL.save(os.path.join(app.root_path,"static/data/annotations/",filename))

    return "complete"

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
