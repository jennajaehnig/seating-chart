from flask import Flask
import flask
import subprocess
import os
import sys
import csv
import random
import sqlite3
import pandas as pd


app = Flask(__name__)

connection = sqlite3.connect('seating_chart.db')


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/run_python_script', methods=['POST'])
def run_python_script():
    # Run your Python script using subprocess
    subprocess.run(['python', 'seating_chart.py'])
    return 'Python script executed successfully!'


def get_num_groups():
    num_groups = 0
    for i in range(3):
        try:
            num_groups = int(input("What size groups do you want? "))
            print(num_groups)
        except ValueError:
            print("Please enter an integer value.")
            continue
        else:
            break
    return num_groups


def generate_groups(student_list, num_students_per_group):
    Groups = {}
    curr_num_students = 0
    if(num_students_per_group == 0):
        print("You did not enter a valid group size.")
        sys.exit()

    for student in student_list:
        idx = curr_num_students//num_students_per_group
        Groups.setdefault(idx, [])
        Groups[idx].append(student.strip())
        curr_num_students += 1

    return Groups


def print_groups(Groups):

    for group, students in Groups.items():
        students_str = ', '.join(students)
        print(f"Group {group + 1}: {students_str}")
    print()


def readfile(filename, student_list):

    cur = connection.execute(
        "DROP TABLE IF EXISTS students"
    )

    cur = connection.execute( 
        '''
        CREATE TABLE students( 
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(40) NOT NULL);
        '''
    )

    with open(os.path.join('static', filename), 'r') as csvfile:
        contents = csv.reader(csvfile)
        next(contents)  # Skip header if exists

        data_to_insert = [(row[7], row[6]) for row in contents]

        # Execute the SQL command to insert multiple rows
        cur = connection.executemany(
            "INSERT INTO students (first_name, last_name) VALUES (?, ?)",
            (data_to_insert)
        )

    cur = connection.execute(
        "SELECT * FROM students"
    )
    rows = cur.fetchall()
    
    for r in rows:
        student_list.append(r[1] + ' ' + r[2])


def display_groups(Groups):

    for group in Groups:
        for student in group:
            cur = connection.execute('''
                SELECT img_url FROM students WHERE first_name = ?,
                ''', (student[0], ))
            student_img_url = cur.fetchone()
            


@app.route('/submit/', methods=['POST'])
def submit():
    if flask.request.method == 'POST':
        try:
            groupSize = int(flask.request.form['groupSize'])
        except ValueError:
            print('Please enter a group size')

        # Now you can use the data as required
        # For example, let's print it and return it to the user
        print(f"Group size: {groupSize}")

        filename = 'Roster.csv'
        student_list = []
        readfile(filename, student_list)

        random.shuffle(student_list)
        Groups = generate_groups(student_list, groupSize)
        print_groups(Groups)
        display_groups(Groups)

    return flask.redirect('/')
        
    
@app.route('/static/images/<path:filename>')
def load_img(filename):
    directory = 'static/images/'
    if not os.path.exists(os.path.join(directory, filename)):
        flask.abort(404)
    return flask.send_from_directory(directory, filename)


if __name__ == '__main__':
    app.run(debug=True)
