from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import model
from tensorflow.keras.preprocessing.image import save_img
import numpy as np
from PIL import Image
import cv2
app = Flask(__name__)


Resnet_roc = model.load_model('static/model/Resnet_roc.h5')
# autoencoder = model.load_model('static/model/autoencoder_128.h5')
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        X_test = []
        image = model.preprocess_image(path)
        X_test.append(image)
        X_test= np.array(X_test).reshape(-1,128,128,3)
        # preprocess_autoencoder = model.predict(image,autoencoder)
        # rescale_autoencoder = model.rescale_img(preprocess_autoencoder)
        # result_VGG19 =model.predict(np.expand_dims(rescale_autoencoder, axis=0)*1/255.0,VGG19)
        result = model.predict(X_test,Resnet_roc) 
        sign_label = model.translate_result(result) 
        # top_scores, top_scores_percentage = model.top(result_VGG19,class_names, n=1)
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        save_img(path, img)    
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename, label = sign_label)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
if __name__ == "__main__":
    app.run()
