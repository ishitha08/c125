from flask import Flask,jsonify,request
from classifier import get_prediction

app = Flask(__name__)
@app.route('/predict-visit',methods = ['POST'])

def predict_data():
    image = requets.files.get('digit')
    prediction = get_prediction(image)
    return jsonify({
        'prediction':prediction
    }),200

if __name__ == '__name__':
    app.run(debug = True)