from app import app
from flask import render_template, request
import csv

@app.route('/')
def index():
    # Read data from CSV file
    data = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    
    # Render template with data
    return render_template('index.html', data=data)




# ''' username request'''

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/greet', methods=['POST'])
# def greet():
#     username = request.form['username']
#     return render_template('greet.html', username=username)