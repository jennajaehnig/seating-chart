import sys
import random

def get_num_groups():
    num_groups = 0
    for i in range(3):
        try:
            num_groups = int(input("What size groups do you want? "))
            print()
        except ValueError:
            print("Please enter an integer value.")
            continue
        else:
            break
    return num_groups

def generate_groups(student_list):
    Groups = {}
    curr_num_students = 0
    num_students_per_groups = int(get_num_groups())
    if(num_students_per_groups == 0):
        print("You did not enter a valid group size.")
        sys.exit()

    for student in student_list:
        idx = curr_num_students//num_students_per_groups
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

def main():

    try:
        file = open('students.txt')
    except FileNotFoundError:
        print("File not found.")

    student_list = file.readlines()

    Groups = generate_groups(student_list)
    print_groups(Groups)
    randomize = ask_to_randomize()

    while(randomize):
        # student_list = file.readlines()
        random.shuffle(student_list)
        # func(student_list)
        Groups = generate_groups(student_list)
        print_groups(Groups)
        randomize = ask_to_randomize()

main()
