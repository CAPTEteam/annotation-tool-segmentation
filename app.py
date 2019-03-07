from flask import Flask, redirect, url_for, request, render_template, session
from PIL import Image
import numpy as np
import base64
import re
from io import BytesIO
import os
from werkzeug import secure_filename
from models.users.views import user_blueprint

app = Flask(__name__, static_url_path='')
app.debug= True

app.secret_key = "65re4g56er4"
# Registration of Blueprint path 
app.register_blueprint(user_blueprint, url_prefix="/users")

@app.route('/')
def home():
    # There is no more home for now
    # Either the user is already logged and it's showing the systems dashboard, either it asks to log
    if True:
        return render_template('users/login.html')
    else:
        return redirect(session['project'])

@app.route("/<project>")
def hello(project):
    return render_template('index.html',project = project)

@app.route('/upload', methods=['POST'])
def get_image():
    image_b64 = request.values['imageBase64']
    project = request.values['project']
    image_data = re.sub('^data:image/.+;base64,', '', image_b64)
    image_PIL = Image.open(BytesIO(base64.b64decode((image_data))))
    filename = request.values["filename"]
    image_PIL.save(os.path.join(app.root_path,"static/data/",project,"annotations",filename))

    return "complete"

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
