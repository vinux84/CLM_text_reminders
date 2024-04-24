from os import system, name
import time
from clm_library import clm_students


class NonetypeException(Exception):
    """Detect Nonetype."""

part_number_list = ['3', '4', '5', '6', '7', '8']

part_type_dict = {
    'r': 'Bible Reading',
    's': 'Starting a Conversation',
    'f': 'Following Up',
    'm': 'Making Disciples',
    't': 'Talk',
    'e': 'Explaining Your Beliefs',
    'hu': 'Humility',
    'k': 'Kindness', 
}

part_theme_dict = {
    'p': 'PUBLIC WITNESSING',
    'i': 'INFORMAL WITNESSING',
    'h': 'HOUSE TO HOUSE',
    't': 'Talk',
    'd': 'Demonstration',
    'di': 'Discussion',
}


part_info = []
part_i = []
hh_part_info = []
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


def get_part_theme(part_theme):
    for t_key, t_value in part_theme_dict.items():
        if t_key == part_theme:
            return t_value
        

def get_student(last_name, first_name):
    m = '_minor'
    check_minor = first_name + m
    for last, first in clm_students.items():
        if last.lower() == last_name:           
            l = last
            for fn, i in first.items():
                if fn.lower() == first_name:
                    f = fn
                    t = first[fn]
                    return f,l,t
                elif fn.lower() == check_minor:
                    for m in i:
                        if m.lower() == first_name:
                            fnm = m
                            tm = i[m]
                            gfn = clm_students[last][fn]['Guardian_first_name']
                            gln = clm_students[last][fn]['Guardian_last_name']
                            gt = clm_students[last][fn]['title']
                            return fnm, l, tm, gfn, gln, gt

def find_pronoun(title):
    if title == 'Brother':
        he = 'he'
        his = 'his'
        return he, his
    else:
        she = 'she'
        her = 'her'
        return she, her

def exception_handler(t):
    print(f'\nPart {t} not found, Choose from the available part {t}s...')
    time.sleep(5)

def bible_reading_or_talk(part_i):
    clear_screen()
    pronoun = find_pronoun(part_i[4])
    print("\nCOPY BELOW INTO A MESSAGE")
    print("-------------------------\n")
    if len(part_i) >= 7:
        print(f"Hello {part_i[7]} {part_i[6]}, just a reminder that for this coming Tuesday night’s meeting {part_i[2]} is scheduled for the part:")
    else:
        print(f"Hello {part_i[4]} {part_i[3]}, just a reminder that for this coming Tuesday night’s meeting you are scheduled for the part:")
    if part_i[1] == 'Bible Reading':
        print(f"""
#{part_i[0]}  |  {part_i[1]}""")
    elif len(part_i) >= 7:
        print(f"""
#{part_i[0]}  |  {part_i[1]} - {part_i[8]}""")
    else:
        print(f"""
#{part_i[0]}  |  {part_i[1]} - {part_i[5]}""")
    if len(part_i) >= 7:
        print(f"""
Please text back to confirm that {pronoun[0]} can or cannot do the assignment.""")
    else:
        print("""
Please text back to confirm that you can or cannot do the assignment.""")
    print("""

Thank you.

Your Brother,
-Vincent Benningfield- """)
    print("\n---------------------------\n\n\n")
    input("Are you done? Press any key to continue...")



def demonstration(part_i, hh_part_info):
    clear_screen()
    pronoun = find_pronoun(part_i[4])
    pronoun_hh = find_pronoun(hh_part_info[4])
    print("\nCOPY BELOW INTO A MESSAGE")
    print("-------------------------\n")
    if len(part_i) == 9:
        print(f"Hello {part_i[7]} {part_i[6]}, just a reminder that for this coming Tuesday night’s meeting {part_i[2]} is scheduled for the part:")
    else:
        print(f"Hello {part_i[4]} {part_i[3]}, just a reminder that for this coming Tuesday night’s meeting you are scheduled for the part:")
    if len(part_i) == 9:
        print(f"""
#{part_i[0]}  |  {part_i[1]} - {part_i[8]}""")
    else:
        print(f"""
#{part_i[0]}  |  {part_i[1]} - {part_i[5]}""")
    if len(part_i) == 9:
        print(f"""
with {hh_part_info[2]} {hh_part_info[3]} as {pronoun[1]} householder.""")
    else:
        print(f"""
with {hh_part_info[2]} {hh_part_info[3]} as your householder.""")
    if len(part_i) == 9:
        print(f"""
Please text back to confirm that {pronoun[0]} can or cannot do the assignment.""")
    else:
        print(f"""
Please text back to confirm that you can or cannot do the assignment.""")
    print("""
Thank you.

Your Brother,
-Vincent Benningfield- """)
    print("\n---------------------------\n\n\n")
    print("\nCOPY HOUSEHOLDER'S MESSAGE BELOW INTO A MESSAGE")
    print("-----------------------------------------------\n")
    if len(hh_part_info) == 9:
        print(f"Hello {hh_part_info[7]} {hh_part_info[6]}, just a reminder that for this coming Tuesday night’s meeting {hh_part_info[2]} is scheduled for the part:")
    else:
        print(f"Hello {hh_part_info[4]} {hh_part_info[3]}, just a reminder that for this coming Tuesday night’s meeting you are scheduled for the part:")
    if len(hh_part_info) == 9:
        print(f"""
#{hh_part_info[0]}  |  {hh_part_info[1]} - {hh_part_info[8]}""")
    else:
        print(f"""
#{hh_part_info[0]}  |  {hh_part_info[1]} - {hh_part_info[5]}""")
    if len(hh_part_info) == 9:
        print(f"""
{pronoun_hh[0]}'s {part_i[2]} {part_i[3]}'s householder.""")
    else:
        print(f"""
You are {part_i[2]} {part_i[3]}'s householder.""")
    if len(hh_part_info) == 9:
        print(f"""
Please text back to confirm that {pronoun_hh[0]} can or cannot do the assignment.""")
    else:
        print("""
Please text back to confirm that you can or cannot do the assignment.""")
    print("""
Thank you.

Your Brother,
-Vincent Benningfield- """)
    print("\n---------------------------\n\n")
    input("Are you done? Press any key to continue...")


def name_example(choice):
    clear_screen()
    get_title = get_part_type(choice)
    print('Enter the Name of the Christian Example')
    print('---------------------------------------\n')
    example_name = input('> ')
    e_name = example_name.capitalize()
    what = f'{get_title}-What {e_name} Did'
    imitate = f'{get_title}-Imitate {e_name}'
    clear_screen()
    print('Choose the Title of Part')
    print('------------------------\n')
    print(f'Enter [W] for {what}\n')
    print(f'Enter [I] for {imitate}\n')
    k_type = input('> ').lower()
    if k_type == 'w':
        part_info.append(what)
    elif k_type == 'i':
        part_info.append(imitate)
    else:
        print("\nPlease choose between titles, enter Christian example again...")
        time.sleep(5)
        name_example(choice)
    
    
def house_holder():
    clear_screen()
    print("\nEnter the Householder's Name")
    print('----------------------------\n')
    first_name = input("First Name: ").lower()
    last_name = input("Last Name: ").lower()
    person_giving_part = get_student(last_name, first_name)
    if person_giving_part is None:
        print("\nName misspelled or student not found, enter name again...")
        time.sleep(5)
        house_holder()
    else:
        person_list = list(person_giving_part)
        hh_part_info.extend(part_info)
        hh_part_info.extend(person_list)
        
        

def student_name(*args, **kwargs):
    clear_screen()
    print("\nEnter the Student's Name")
    print('------------------------\n')
    first_name = input("First Name: ").lower()
    last_name = input("Last Name: ").lower()
    person_giving_part = get_student(last_name, first_name)
    try:
        person_list = list(person_giving_part)
    except TypeError:
        print("\nName misspelled or student not found, enter name again...")
        time.sleep(5)
        student_name(*args, **kwargs)
    else:
        for t in args:
            if t == 'r':
                part_i = part_info + person_list
                bible_reading_or_talk(part_i)
            elif t == 't':
                for kw in kwargs.values():
                    part_i = part_info + person_list
                    part_i.append(kw)
                    bible_reading_or_talk(part_i)
            elif t == 'e':
                for theme in args:
                    if theme == 'e_talk':
                        for kw in kwargs.values():
                            part_i = part_info + person_list
                            g_theme = get_part_theme('t')
                            total_theme = g_theme + " " + kw 
                            part_i.append(total_theme)
                            bible_reading_or_talk(part_i)
                    elif theme == 'e_demonstration':
                        for kw in kwargs.values():
                            house_holder()
                            part_i = part_info + person_list
                            g_theme = get_part_theme('d')
                            total_theme = g_theme + " " + kw
                            part_i.append(total_theme)
                            hh_part_info.append(total_theme)
                            demonstration(part_i, hh_part_info)
            elif t == 'k' or t == 'hu':
                part_i = part_info + person_list
                g_theme = get_part_theme('di')
                part_i.append(g_theme)
                bible_reading_or_talk(part_i)
            else:
                if t == 'h' or t == 'p' or t == 'i':
                    house_holder()
                    part_i = part_info + person_list
                    for theme in args:
                        if theme == 'h':
                            g_theme = get_part_theme('h')
                            part_i.append(g_theme)
                            hh_part_info.append(g_theme)
                        elif theme == 'p':
                            g_theme = get_part_theme('p')
                            part_i.append(g_theme)
                            hh_part_info.append(g_theme)
                        elif theme == 'i':
                            g_theme = get_part_theme('i')
                            part_i.append(g_theme)
                            hh_part_info.append(g_theme)
                        demonstration(part_i, hh_part_info)
            

def student_part_theme(choice):
    clear_screen()
    pth = 'theme'
    if choice == 'r':
        student_name(choice)
    elif choice == 't':
        print('\nEnter the Theme of the Talk')
        print('------------------------------\n')
        talk_t = input('> ')
        student_name(choice, talk_theme=f'Theme: {talk_t}')
    elif choice == 'e':
        print('\nIs This a Talk or a Demonstraion?')
        print('---------------------------------\n')
        print('Enter [T] for Talk\n')
        print('Enter [D] for Demonstration\n')
        choice_e = input('> ').lower()
        if choice_e == 't':
            print('\nEnter the Theme of the Talk')
            print('------------------------------\n')
            talk_e = input('> ')
            student_name(choice, 'e_talk', talk_theme=f'- Theme: {talk_e}')
        elif choice_e == 'd':
            print('\nEnter the Theme of the Demonstration')
            print('------------------------------\n')
            demo_e = input('> ')
            student_name(choice, 'e_demonstration', demo_theme=f'- Theme: {demo_e}')
        else:
            print("\nPlease choose between talk or demonstration...")
            time.sleep(5)
            student_part_theme(choice)
    elif choice == 'k' or choice == 'hu':
        name_example(choice)
        student_name(choice)
    else:
        print('\nChoose the Theme of the Part')
        print('----------------------------\n')
        print('Enter [H] for HOUSE TO HOUSE\n')
        print('Enter [P] for PUBILC WITNESSING\n')
        print('Enter [I] for INFORMAL WITNESSING\n')
        choice_t = input('> ').lower()
        try:
            if choice_t == 'h' or choice_t == 'p' or choice_t == 'i':
                pass
            else:
                raise NonetypeException
        except:
            exception_handler(pth)
            student_part_theme(choice)
        else:
            student_name(choice_t)
    
def student_part_type():
    clear_screen()
    pt = 'type'
    print('\nChoose the Type of Part')
    print('-----------------------\n')
    print('Enter [R] for Bible Reading\n')
    print('Enter [E] for Explaining Your Beliefs\n')
    print('Enter [S] for Starting a Conversation\n')
    print('Enter [F] for Following Up\n')
    print('Enter [M] for Making Disciples\n')
    print('Enter [T] for Talk\n')
    print('Enter [K] for Kindness-\n')
    print('Enter [HU] for Humility-\n')
    choice = input('> ').lower()
    if choice == 'k' or choice == 'hu':
        student_part_theme(choice)
    else:
        p_type = get_part_type(choice)
        try:
            if p_type is None:
                raise NonetypeException   
        except:
            exception_handler(pt)
            student_part_type()
        else:
            part_info.append(p_type)
            student_part_theme(choice)
        
    
def student_part_number():
    clear_screen()
    pn = 'number'
    print("\nEnter the Student Part Number")
    print('-----------------------------\n')
    print("Part numbers available are 3 - 8\n")
    p_number = input('> ')
    part_number = get_part_number(p_number)
    try:
        if part_number is None:
            raise NonetypeException   
    except:
        exception_handler(pn)
        student_part_number()
    else:
        part_info.append(part_number)
        student_part_type()
    
    
def main():
    global c
    c += 1
    student_part_number()
    part_info.clear()
    part_i.clear()
    hh_part_info.clear()
    
def intro():
    while True:
        clear_screen()
        print("\nCopy & Paste Text Message to Students")
        print("-------------------------------------\n")
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

