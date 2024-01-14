import sys
import random
import csv
import pandas as pd

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

def ask_to_randomize():
    yes = {'yes', 'ye', 'y'}
    no = {'no', 'n'}
    randomize = False

    for i in range(3):
        choice = input("Would you like to randomize groups? [y/n] ").lower()
        # console.log(choice)
        if choice in yes:
            randomize = True
            return randomize
        elif choice in no:
            randomize = False
            return randomize
        else:
            sys.stdout.write("Please respond with 'y' or 'n'\n")
            if(i == 2):
                sys.exit()
            continue

def readfile(filename, student_list):

    try:
        with open('static/Roster.csv', 'r') as csvfile:
            header = next(csvfile)
            reader = csv.reader(csvfile)
            for row in reader:
                first_name = row[7].strip()
                if(row[10].strip()):
                    first_name = row[10].strip()
                last_name = row[6].strip()
                # print(f"First Name: {first_name}, Last Name: {last_name}")
                student_list.append(first_name + ' ' + last_name)
            print(student_list)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError as e:
        print(f"Error: Unable to open or read the file '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    filename = 'Roster.csv'
    student_list = []
    readfile(filename, student_list)
    num_students_per_group = get_num_groups()

    random.shuffle(student_list)
    Groups = generate_groups(student_list, num_students_per_group)
    print_groups(Groups)
    randomize = ask_to_randomize()

    while(randomize):
        # student_list = file.readlines()
        random.shuffle(student_list)
        # func(student_list)
        Groups = generate_groups(student_list, num_students_per_group)
        print_groups(Groups)
        randomize = ask_to_randomize()

main()
