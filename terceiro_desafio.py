from flask import Flask, jsonify, request, make_response
from segundo_desafio import personagens

app = Flask(__name__)

@app.route('/characters/', methods=['POST'])
def criar_personagem():
    data = request.json
    personagens.append(data)
    return jsonify(data), 201

@app.route('/characters/', methods=['GET'])
def ver_personagens():
    return make_response(jsonify(personagens), 200)

if __name__ == '__main__':
    app.run(debug=True)
    