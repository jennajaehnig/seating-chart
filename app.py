from flask import Flask
import flask
import subprocess
import os
import sys
import csv
import random
# import sqlite3

app = Flask(__name__)

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


# def ask_to_randomize():
#     yes = {'yes', 'ye', 'y'}
#     no = {'no', 'n'}
#     randomize = False

#     for i in range(3):
#         choice = input("Would you like to randomize groups? [y/n] ").lower()
#         # console.log(choice)
#         if choice in yes:
#             randomize = True
#             return randomize
#         elif choice in no:
#             randomize = False
#             return randomize
#         else:
#             sys.stdout.write("Please respond with 'y' or 'n'\n")
#             if(i == 2):
#                 sys.exit()
#             continue


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
    connection = sqlite3.c

    # try:
    #     with open('static/Roster.csv', 'r') as csvfile:
    #         header = next(csvfile)
    #         reader = csv.reader(csvfile)
    #         for row in reader:
    #             first_name = row[7].strip()
    #             if(row[10].strip()):
    #                 first_name = row[10].strip()
    #             last_name = row[6].strip()
    #             # print(f"First Name: {first_name}, Last Name: {last_name}")
    #             student_list.append(first_name + ' ' + last_name)
    #         print(student_list)
    # except FileNotFoundError:
    #     print(f"Error: The file '{filename}' does not exist.")
    # except IOError as e:
    #     print(f"Error: Unable to open or read the file '{filename}': {e}")
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")


@app.route('/submit/', methods=['POST'])
def submit():
    if flask.request.method == 'POST':
        groupSize = (int)(flask.request.form['groupSize'])
        
        # Now you can use the data as required
        # For example, let's print it and return it to the user
        print(f"Group size: {groupSize}")

        filename = 'Roster.csv'
        student_list = []
        readfile(filename, student_list)
        # num_students_per_group = get_num_groups()

        random.shuffle(student_list)
        Groups = generate_groups(student_list, groupSize)
        print_groups(Groups)
        # randomize = ask_to_randomize()

        # while(randomize):
        #     # student_list = file.readlines()
        #     random.shuffle(student_list)
        #     # func(student_list)
        #     Groups = generate_groups(student_list, num_students_per_group)
        #     print_groups(Groups)
        #     randomize = ask_to_randomize()



    return flask.redirect('/')
        
    
@app.route('/static/images/<path:filename>')
def load_img(filename):
    directory = 'static/images/'
    if not os.path.exists(os.path.join(directory, filename)):
        flask.abort(404)
    return flask.send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run(debug=True)
