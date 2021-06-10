from flask import Flask,request, render_template

from flask import jsonify
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('model.tf')


app = Flask(__name__)

class_name = ['negative','postive']
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction',methods=['POST'])
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