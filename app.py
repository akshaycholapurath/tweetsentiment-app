from flask import Flask,request, render_template

from flask import jsonify
import tensorflow as tf
import numpy as np
from flask_cors import CORS,cross_origin

model = tf.keras.models.load_model('sentiment_model1')


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

class_name = ['negative','postive']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction',methods=['POST'])
@cross_origin()
def pred():
    data = request.json
    text = data['text']
    textarr = np.array([text])
    pred_prob = model.predict(textarr)
    pred = tf.squeeze(tf.round(pred_prob), axis=1)
    index = int(pred[0])
    return jsonify({"Prediction":class_name[index]})


if __name__ == '__main__':
    app.run(debug=False)