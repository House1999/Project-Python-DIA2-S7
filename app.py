from flask import Flask, request, render_template, redirect, url_for, flash, jsonify

import pickle
import json
import pandas as pd
import numpy as np

app = Flask(__name__,template_folder='templates',static_url_path="/static", static_folder='static')


# This is optional : if we want a rendered home page and manual requests on the site

@app.route('/')
def home():
 	return render_template("main.html")

@app.route('/predict/', methods=['POST'])
def predict():

    data = request.get_json()
    
    # Scale the data

    df = pd.DataFrame(data).T

    X_test_num  = df
    X_test_num = X_test_num.drop([1,14],axis=1)

    X_test_cat = df
    X_test_cat = X_test_cat[[1,14]]

    scaled_col_test = scaler.transform(X_test_num)
    encoded_col_test = one_hot_encoder.transform(X_test_cat)

    scaled_data  = np.concatenate([scaled_col_test,encoded_col_test],axis=1)
    
    # Predict 

    prediction = model.predict(scaled_data)
    
    return jsonify(result = round(float(prediction),3))

@app.route('/predict-site/',methods=['POST'])
def predictSite():	

    duration = float(request.form['duration'])
    width = int(request.form['width'])
    o_width = int(request.form['o_width'])
    height = int(request.form['height'])
    o_height = int(request.form['o_height'])
    bitrate = int(request.form['bitrate'])
    o_bitrate = int(request.form['o_bitrate'])
    framerate = float(request.form['framerate'])
    o_framerate = float(request.form['o_framerate'])

    i = int(request.form['i'])
    p = int(request.form['p'])
    b = int(request.form['b'])

    i_size = int(request.form['i_size'])
    p_size = int(request.form['p_size'])
    b_size = int(request.form['b_size'])

    frames = i + p + b
    size = i_size + p_size + b_size

    umem = float(request.form['umem'])

    codec = request.form['codec']
    o_codec = request.form['o_codec']

    data = [duration,codec,width,height,bitrate,framerate,i,p,b,frames,i_size,p_size,b_size,size,o_codec,o_bitrate,o_framerate,o_width,o_height,umem]

    # Scale the data

    df = pd.DataFrame(data).T

    X_test_num  = df
    X_test_num = X_test_num.drop([1,14],axis=1)

    X_test_cat = df
    X_test_cat = X_test_cat[[1,14]]

    scaled_col_test = scaler.transform(X_test_num)
    encoded_col_test = one_hot_encoder.transform(X_test_cat)

    scaled_data  = np.concatenate([scaled_col_test,encoded_col_test],axis=1)
    
    # Predict 
    
    prediction = model.predict(scaled_data)

    #return jsonify(result = round(float(prediction),3))
    return render_template("result.html",utime=round(float(prediction),3))


if __name__ == '__main__':

    model = pickle.load(open('model/model.pickle', 'rb'))
    scaler = pickle.load(open('model/scaler.pickle', 'rb'))
    one_hot_encoder = pickle.load(open('model/ohe.pickle', 'rb'))

    app.run(debug=False, host='127.0.0.1')