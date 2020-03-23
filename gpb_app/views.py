#! /usr/bin/env python3
# coding: utf-8

from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()