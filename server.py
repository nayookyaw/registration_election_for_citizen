from flask import Flask, render_template, url_for, jsonify, request

import os
import json

app = Flask(__name__)

app._static_folder = os.path.abspath("templates/static/")

@app.route('/')
def index():
    return render_template("views/election.html", message="Manual")

@app.route('/get/time')
def get_times():
    with open("templates/static/data.json") as data_file:
        data = json.load(data_file)
        print (data['total_seconds'])
        return jsonify({"result" : data['total_seconds']})

@app.route('/help')
def help():
    return render_template("views/help.html")

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=7000, debug=True)