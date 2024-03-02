from flask import Flask
import flask
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/run_python_script', methods=['POST'])
def run_python_script():
    # Run your Python script using subprocess
    subprocess.run(['python', 'seating_chart.py'])
    return 'Python script executed successfully!'

@app.route('/static/images/<path:filename>')
def load_img(filename):
    directory = 'static/images/'
    if not os.path.exists(os.path.join(directory, filename)):
        flask.abort(404)
    return flask.send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run(debug=True)
