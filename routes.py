from app import app
from flask import render_template, request
import csv
import subprocess

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/router_info', methods=['POST'])
def router_info():
    username = request.form['username']
    with open('router_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        router_data = list(reader)
    return render_template('router_info.html', username=username, router_data=router_data)

@app.route('/connect', methods=['POST'])
def connect():
    username = request.form['username']
    ip_address = request.form['ip_address']
    port = request.form['port']
    command = f"ssh {username}@{ip_address} -p {port}"
    subprocess.run(command, shell=True)
    return "SSH connection started"