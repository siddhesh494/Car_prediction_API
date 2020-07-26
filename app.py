import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("new.html")

@app.route('/predicts',methods=['POST'])
def predicts():
    '''
    For rendering results on HTML GUI
    '''
    x=request.form
    print(x)
    a=request.form['car']
    b=request.form['fuel']
    c=request.form['aspiration']
    d=request.form['body']
    e=request.form['engine-location']
    
    f=request.form['engine-type']
    g=request.form['engine size']
    h=request.form['compression ratio']
    i=request.form['horse power']
    j=request.form['peak rpm']
    
    final_features=[[int(a[0:2]), int(b[:2]), int(c[:2]), int(d[:2]), int(e[:2]), int(f[:2]), int(g), int(h), int(i), int(j)]]
    #int_features = [int(x[0:2]) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('new.html', prediction_text='--------------------Current car value is ${}-------------------'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

