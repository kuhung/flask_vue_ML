from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from flair.models import TextClassifier
from flair.data import Sentence
from flask import session

app = Flask(__name__)
app.secret_key = "super_secret_key"
# # app.config['SECRET_KEY'] = 'oh_so_secret'

# app.config['MONGO_DBNAME'] = 'exposeModel'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/exposeModel'
# mongo = PyMongo(app)

CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify("welcome to Arafa API")

# @app.route('/my_session', methods=['GET'])
# def return_session():
#     result = []
#     data_result = session['my_result']
#     result.append ({'title': data_result['title'], 'tag': data_result['tag'] })
  
#     return jsonify(result)

@app.route('/api/tasks', methods=['GET'])
def get_result():
    result = []
    data_result = session['my_result']
    result.append ({'title': data_result['title'], 'tag': data_result['tag'] })
    session.clear()
    return jsonify(result)

@app.route('/api/task', methods=['POST'])
def input_predict_text():
    classifier = TextClassifier.load_from_file('models/best-model.pt')

    title = request.get_json()['title']

    sentence = Sentence(title)
    # # run NER over sentence
    classifier.predict(sentence)

    text = sentence.to_plain_string()
    label = sentence.labels[0]
    result = {'title' : text, 'tag' : label.value}
    session['my_result'] = result
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
