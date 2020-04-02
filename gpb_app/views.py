#! /usr/bin/env python3
# coding: utf-8

import random
from flask import Flask, render_template, request, jsonify

from .models.api_requests import APIRequests
from .models.parser import Parser
import config as cf

app = Flask(__name__)
app.config.from_object('config')

@app.route('/chatbox', methods=['POST'])

def chatbox():
    """Route to connect Python backend and JS frontend"""
    query = request['query']

    if len(query) <= 1:         #if the user doesn't write a single character
        empty_error = cf.EMPTY_QUERY_ANSWER
        return jsonify({'error': empty_error})

    parser = Parser(request.form['textinput'])      #parse the user input
    parser.clean_input_of_symbols()
    parser.clean_input_of_stopwords()

    try:
        place = APIRequests(parser.final_query_in_string)     #call the API to search the place contained in the user query
    except:
        return jsonify({'error': "Ton Internet déraille complètement..."})

    if place.location_datas is False:
        error_list = cf.ANSWERS_ADRESS_FAIL
        random_index = random.randint(0, 3)
        missing_place_answer = error_list[random_index]
        return jsonify({'error': missing_place_answer})
    else:
        answers_list = cf.ANSWERS_ADRESS_OK
        random_index = random.randint(0, 3)
        text_location = answers_list[random_index]

    if 

    

@app.route('/')
@app.route('/index/')
def index():
    """Display the web page with html and css code"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run()