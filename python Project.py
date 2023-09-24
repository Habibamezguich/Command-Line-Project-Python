import time
import getpass
from collections import namedtuple
from time import sleep, strftime
from cfonts import render, say

M=""
email="" 
name =""
pswd=""
pd=""

###https://pypi.org/project/python-cfonts/
output = render('welcome to| ORDINO', colors=['blue', 'yellow'], align='center' )
print(output)

############## 
def first_menu():
    print('%100s' % "----------1.User menu----------") 
    print('%100s' % "----------2.Admin menu---------")
    choices =int(input("\nPlease enter your role as a number : \n"))
    if choices==1:
        User_menu()
    elif choices==2:
        Admin_menu()
    else:
        first_menu()

############ Add + Delete  function using list (Matrix)
def Add_user():
    global M
    L=int(input("Enter number of users: "))
    C=int(input("Donner le nombre des colonnes: "))
    M=[]
    for i in range(0,L):
        Liste =[]
        for j in range (0,C):
            ID=input("Enter the ID: ")
            NAME=input("Enter the name: ")
            EMAIL=input("Enter the email: ")
            PHONE=input("Enter the phone number: ")
            Liste.append(ID)
            Liste.append(NAME)
            Liste.append(EMAIL)
            Liste.append(PHONE)
            M.append(Liste)
    print("Current list : ",M )
    menulist=int(input("Enter a choice\n├──1 Delete user\n├──2 Add user \n"))
    if menulist ==1:
        Delete_user()
    elif menulist==2:
        Add_user()
    else: 
        User_menu

############ Delete  function
def Delete_user():
    p=int(input("enter position of use\n"))
    if not M:
        print('Empty list')
    else:
        del (M[p])
        print("New list:",M)
    menulist=int(input("Enter a choice\n├──1 Add user\n├──2 Delete user \n"))
    if menulist ==1:
        Add_user()
    else:
        Delete_user()


############ Create_account function
def create_account():
    global name
    name=input("Enter your first name : ")
    second_name=input("Enter your second name : ")
    global email 
    email=input("Enter your email or mobile number : ")
    password()
    #using ANSI escape code https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#decorations
    print("\033[1;32;40m Thanks,",name,"! Your account has been successfully created.")
    print (u"\u001b[0m")
    menulist=int(input("Enter a choice\n ├──1 About us \n ├──2 Sign in\n  "))
    if menulist ==1:
        about_us()
    else:
        sign_in()



############ Password check
def password():
    while True:
        global pswd
        pswd = getpass.getpass('Password:')
        if (len(pswd)>5 and len(pswd)<15):
            print("\033[1;32;40m Your password is valid")
            return
        else:
            print (u"\u001b[31mMake sure your password is at lest 6 letters, Please try again !")
            print (u"\u001b[0m")


############ sign_in function
def sign_in():
    email_in=input("Enter your email or mobile number : ")
    passw = getpass.getpass("What is your password?")
    while passw !=pswd:
        print("try again")
        passw=input('What is your password? : ')
    else :
        print (u"\u001b[36mHello\nwe're so happy you're here, the concept is simple: ORDINO helps you get more organised, get motivated, and get more work done.")
        print (u"\u001b[0m")
        menulist=int(input("Enter a choice\n├──1 Connect channels\n├──2 Go to my Board \n├──3 About us\n├──4 Display my information\n"))
        if menulist ==1:
            connect_channel()
        elif menulist==2:
           start_calendar()
        elif menulist==3:
            about_us()
        else:
            display_info()
        

############ About us function
def about_us():
    print('''
                        .-"""-.
                       / o===o \  
                       \       /
                       ( \___/ )
          _________ooo__\_____/________________
        /                                      |
        | ORDINO is a a social media marketing |
        | tool that helps professsionals,teams | 
        |     and businesses automate their    |
        |         social media accounts        |
         \______________________ooo___________/
                       |  |  |
                       |_ | _|
                       |  |  |
                       |__|__|
                       (_/ \_)
                                          ''')
    menulist=int(input("Enter a choice\n├──1 Create account\n├──2 sign in \n├──3 Return to 1st menu"))
    if menulist ==1:
        create_account()
    elif menulist==2:
        sign_in()
    else:
        first_menu()


############ connect channel function: using named tuple 
def connect_channel():
    channels = namedtuple("channels",["first","second","third"])
    liste=[]
    for i in range(0,1):
        print("Enter 3 social media channels you want to manage : ")
        first=(input("1 : "))
        second=input("2 : ")
        third=(input("3 : "))
        accounts=channels(first,second,third)
        liste.append(accounts)
    print("\u001b[33m",liste)
    print (u"\u001b[0m")


    menulist=int(input("Enter a choice\n ├──1 About us \n ├──2 Dashboard\n ├──3 Display information\n"))
    if menulist ==1:
        about_us()
    elif menulist==2:
        start_calendar()
    else:
        display_info()


############Dashboard function using dictionnary

# this is an an empty dictionary called calendar.
calender = {}

def welcome():
    print("Welcome to the dashboard")
    sleep(1)
    #strftime(format),represente le temps sous forme d’une chaîne de caractères.
    print("Today is : ",strftime("%A %B %dth, %Y",)) #(%A)Jour de la semaine(%B)Nom complet du mois dans la langue locale.(%Y)Année complète sur quatre chiffres.
    sleep(1)
    print("What would you like to do?")

# Calendar 
def start_calendar():
    welcome()
    start = True
    while(start):
        #user should enter A to Add, U to Update, V to View, D to Delete, X to Exit with upper case and if not we send a message and reload the user_choices
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == 'V':
            if bool(calender) == False:
                print("Calender is empty.")
            else:
                print(calender)
        elif user_choice == 'U':
            date = input("What date?: ")
            update = input("Enter the update: ")
            calender[date] = update
            print("Update successful.")
            print(calender)
        elif user_choice == 'A':
            event = input("Enter the post: ")
            date = input("Enter date (MM/DD/YYYY): ")
            print(date[0:3])
            if len(date) > 10 or int(date[6:10]) - int(strftime("%Y")) > 0:
                print("Invalid date was entered.")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == 'Y':
                    continue
                elif try_again == 'N':
                    print("Exiting program.")
                    start = False
            else:
                calender[date] = event
                print("Event was sucessfully added.")
                print(calender)
        elif user_choice == 'D':
            if bool(calender) == False:
                print("Calender is empty.")
            else:
                event = input("What event?: ")
                for date in calender:
                    if event == calender[date]:
                        #del to delete calendar[date].
                        del calender[date]
                        print("Event was successfully deleted.")
                    else:
                        print("Incorrect event was specified.")
        elif user_choice == 'X':
                menulist=int(input("Enter a choice\n├──1 About US \n├──2 Connect channels\n├──3 Display information\n"))
                if menulist ==1:
                    about_us()
                elif menulist==2:
                    connect_channel()
                else:
                    display_info()
                    break
                start = False


############ Display information function 
def display_info():
    print('your name is : ' ,name); time.sleep(2)
    print('your email is : ' ,email); time.sleep(2)
    print('Change your password ')
    password=input("Your existing password:\n")
    passwrd=input("Your new password:\n")
    if (len(passwrd)>5 and len(passwrd)<15):
        print("\033[1;32;40m Your password have been changed successfully!")
        print (u"\u001b[0m")
    else:
        print (u"\u001b[31mMake sure your password is at lest 6 letters, Please try again !")
        print (u"\u001b[0m")
        new_passwrd=input("Your New password:\n")
    menulist=int(input("Enter a choice\n├──1 Dashboard\n├──2 Connect Channels\n├──3 About us"))
    if menulist ==1:
        start_calendar()
    elif menulist==2:
        connect_channel()
    else:
        about_us()


############ Display information function 
def Admin_menu(): 
    pd="admin"
    name = input("Hello admin! Welcome to Ordino \nUsername: ") #Ask's the User for Username input
    pd = input("Password: ") # Ask's the user for their password
    if pd != "admin":
        name = input("Try again\nUsername: ") #Ask's the User for Username input
    else:
        print("""
    ╭── Admin Menu───────────────╮                                              
    ├──1 Add user                │ 
    ├──2 Delete user             │
    ├──3 Update About us         │                                                            
    ╰────────────────────────────╯""")
        choices =int(input("\nPlease enter your choice as a number : \n"))
#choices for admin
        while True :
            if choices == 1: 
                Add_user()
                break 
            elif choices == 2:
                Delete_user()
                break
            else:
                about_us()
                break

############ Display information function 
def User_menu():
    print("""
    ╭── User Menu───────────────╮    
    ├──1 Create account         │ 
    ├──2 Sign in                │                        
    ├──3 About us               │  
    ├──4 Admin menu             │                                           
    ╰───────────────────────────╯""")
    choices =int(input("\nPlease enter your choice as a number : \n"))
#choices for simple user
    while True :
        if choices == 1: 
            create_account()
            break 
        elif choices == 2:
            sign_in()
            break
        elif choices==3:
            about_us()
            break
        else:
            print("Try again",Admin_menu())
            break
first_menu()