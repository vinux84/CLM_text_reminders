from os import system, name
import time
from clm_library import clm_students

part_number_list = ['3', '4', '5', '6', '7', '8']
part_type_dict = {
    'r': 'Bible Reading',
    's': 'Starting a Conversation',
    'f': 'Following Up',
    'm': 'Making Disciples',
    't': 'Talk',
    'e': 'Explaining Your Beliefs',
    'k': 'Kindness-What Jesus Did',
    'kj': 'Kindness-Imitate Jesus',
}

c = 0


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def get_part_number(part_number):
    for n in part_number_list:
        if n == part_number:
            return n


def get_part_type(part_type):
    for t_key, t_value in part_type_dict.items():
        if t_key == part_type:
            return t_value


def get_student(last_name, first_name):
    for last in clm_students.keys():
        if last_name.lower() == last.lower():
            last_n = (clm_students[last])
            for first, title in last_n.items():
                if first.lower() == first_name.lower():
                    return first, last, title


def bible_reading_or_talk(part_number, type_of_talk, person_giving_part):
    print("\nCOPY BELOW INTO A MESSAGE")
    print("---------------------------\n")
    print(f"""Hello {person_giving_part[2]} {person_giving_part[1]}, just a reminder that for this coming Tuesday night’s meeting you are scheduled for the part:

#{part_number} - {type_of_talk}

Please text back to confirm that you can or cannot do the assignment.

Thank you.

Your Brother,
-Vincent Benningfield- """)
    print("\n---------------------------\n\n\n")
    input("Are you done? Press any key to continue...")


def demonstration(part_number, type_of_talk, person_giving_part, householder):
    print("\nCOPY BELOW INTO A MESSAGE")
    print("---------------------------\n")
    print(f"""Hello {person_giving_part[2]} {person_giving_part[1]}, just a reminder that for this coming Tuesday night’s meeting you are scheduled for the part:

#{part_number} - {type_of_talk}

with {householder[0]} {householder[1]} as your householder. 

Please text back to confirm that you can or cannot do the assignment.

Thank you.

Your Brother,
-Vincent Benningfield- """)
    print("\n---------------------------\n\n\n")
    print("\nCOPY HOUSEHOLDER'S MESSAGE BELOW INTO A MESSAGE")
    print("-------------------------------------------------\n")
    print(f"""Hello {householder[2]} {householder[1]}, just a reminder that for this coming Tuesday night’s meeting you are scheduled for the part:

#{part_number} - {type_of_talk}""")
    print(f"""
You are {person_giving_part[0]} {person_giving_part[1]}'s householder.""")
    print("""
Please text back to confirm that you can or cannot do the assignment.

Thank you.

Your Brother,
-Vincent Benningfield- """)
    print("\n---------------------------\n\n\n")
    input("Are you done? Press any key to continue...")


def main():
    global c
    c += 1
    clear_screen()
    print("\nEnter the Student Part Number")
    print('-----------------------------\n')
    p_number = input('> ')
    part_number = get_part_number(p_number)
    clear_screen()
    print('\nNext Choose the Type of Part')
    print('------------------------------\n')
    print('Enter [R] for Bible Reading\n')
    print('Enter [S] for Starting a Conversation\n')
    print('Enter [F] for Following Up\n')
    print('Enter [M] for Making Disciples\n')
    print('Enter [T] for Talk\n')
    print('Enter [E] for Explaining Your Beliefs\n')
    print('Enter [K] for Kindness-What Jesus Did\n')
    print('Enter [KJ] for Kindness-Imitate Jesus\n')
    choice = input('> ').lower()
    part_type = get_part_type(choice)
    clear_screen()
    print("\nNext Enter the Student's Name")
    print('------------------------------\n')
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    print('\n')
    if choice == 'r' or choice == 't' or choice == 'k' or choice == 'kj':
        person_giving_part = get_student(last_name, first_name)
        clear_screen()
        bible_reading_or_talk(part_number, part_type, person_giving_part)
    else:
        hh_first_name = input("House Holder's First Name: ")
        hh_last_name = input("House Holder's Last Name: ")
        person_giving_part = get_student(last_name, first_name)
        householder = get_student(hh_last_name, hh_first_name)
        clear_screen()
        demonstration(part_number, part_type, person_giving_part, householder)


def intro():
    while True:
        clear_screen()
        print("\nCopy & Past Text Message to Students")
        print("------------------------------------\n")
        if c == 0:
            print('Press [1] to make a text reminder')
        elif c >= 1:
            print('Press [1] to make another text reminder')
        print('Press [2] to quit\n')
        intro_choice = input('> ')
        if intro_choice == '1':
            main()
        elif intro_choice == '2':
            exit()
        else:
            clear_screen()
            print("That's not a valid option")
            time.sleep(3)


intro()
