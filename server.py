#!/usr/bin/env python3
from flask import Flask, jsonify, request
import prediction

app = Flask(__name__)

VERSION = 0.1
HOST = '127.0.0.1'
PORT = 1234


@app.route("/api/")
def version():
    return jsonify({"version": VERSION})


@app.route("/api/images", methods=['POST', 'GET'])
def image():
    if request.method == 'POST':
        data = request.get_json()
        p = prediction.predict_image(data['image'])
        return jsonify(p)

    return "ok"


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)

