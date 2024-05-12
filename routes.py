from app import app
from flask import render_template, request
import csv
import subprocess
import paramiko


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


@app.route('/connect', methods=['POST'])
def connect():
    ip_address = request.form['ip_address']
    port = request.form['port']
    username = request.form['username']  # Assuming you've added a field for username in your form
    password = request.form['password']  # Assuming you've added a field for password in your form

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=ip_address, port=int(port), username=username, password=password)
        # Do something with the SSH connection, like executing commands or opening a shell
        ssh_client.close()
        return "SSH connection established"
    except Exception as e:
        return f"Failed to establish SSH connection: {str(e)}"

# To run Powershell cmd 
# @app.route('/connect', methods=['POST'])
# def connect():
#     ip_address = request.form['ip_address']
#     port = request.form['port']
#     # Execute PowerShell command to establish SSH connection
#     command = f"ssh -p {port} {ip_address}"
#     subprocess.run(["powershell", "-Command", command])
#     return "SSH connection established"

























# @app.route('/')
# def index():
#     # Read data from CSV file
#     data = []
#     with open('data.csv', newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             data.append(row)
    
#     # Render template with data
#     return render_template('index.html', data=data)




# ''' username request'''

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/greet', methods=['POST'])
# def greet():
#     username = request.form['username']
#     return render_template('greet.html', username=username)