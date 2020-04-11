from flask import Flask, jsonify, request
# from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from flair.models import TextClassifier
from flair.data import Sentence
from flask import session
import os

model_path = '/root/flask_vue_ML'
expose = Flask(__name__)
expose.secret_key = "super_secret_key"
# expose.config['MONGO_DBNAME'] = 'exposeModel'
# expose.config['MONGO_URI'] = 'mongodb://localhost:27017/exposeModel'
# mongo = PyMongo(expose)

CORS(expose)
classifier = TextClassifier.load_from_file(os.path.join(model_path,'models/best-model.pt'))

@expose.route('/', methods=['GET'])
def index():
    return jsonify("welcome to Arafa API")


@expose.route('/api/tasks', methods=['GET'])
def get_result():
    result = []
    try:
        data_result = session['my_result']
        result.append ({'title': data_result['title'], 'tag': data_result['tag'] })
    except:
        result.append ({'title': 'The txt you input', 'tag': 'spam or harm' })
    return jsonify(result)

@expose.route('/api/task', methods=['POST','GET'])
def input_predict_text():

    title = request.get_json()['title']
    # TODO: title type check
    sentence = Sentence(title)
    classifier.predict(sentence)

    text = sentence.to_plain_string()
    label = sentence.labels[0]
    result = {'title' : text, 'tag' : label.value}
    session['my_result'] = result
    
    return jsonify(result)

if __name__ == '__main__':
    # expose.run(debug=True)
    expose.run(host='0.0.0.0')
