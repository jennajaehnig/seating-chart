from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_script', methods=['POST'])
def run_python_script():
    # Run your Python script using subprocess
    subprocess.run(['python', 'seating_chart.py'])
    return 'Python script executed successfully!'

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
