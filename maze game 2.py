import sys
import webbrowser
def fun():
    print("\n\n\tGAME OVER!!!!")
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=Furs535ly94")
    sys.exit()

#room0
def room0(chance):
    print('''
\tyou are in room no 0!!!
\tnow you have 2 options...
\t\t1) go to room in front of you, room 3
\t\t2) go to room to your right, room 1
''')
    user_choice=int(input("Enter your choice"))
    chance=chance+1
    if(chance>7):
        print("Sorry no chance left for you")
        fun()
    if(user_choice==1):
        room3(chance)
    elif(user_choice==2):
        room1(chance)

#room 1
def room1(chance):
    print('''
\tyou are in room no 1 now!!!
\tnow you have 2 options...
\t\t1) go to room in front of you, room 2
\t\t2) go to room to your left, room 0
''')
    user_choice=int(input("Enter your choice"))
    chance=chance+1
    if(chance>7):
        print("Sorry no chance left for you")
        fun()
    if(user_choice==1):
        room2(chance)
    elif(user_choice==2):
        room0(chance)

#room 2
def room2(chance):
    print('''
\tyou are in room no 2 now!!!
\tnow you have 3 options...
\t\t1) go to room in front of you, room 8
\t\t2) go to room to your left, room 3
\t\t3) go tothe room behind you, room 1
''')
    user_choice=int(input("Enter your choice"))
    chance=chance+1
    if(chance>7):
        print("Sorry no chance left for you")
        fun()
    if(user_choice==1):
        room8()
    elif(user_choice==2):
        room3(chance)
    elif(user_choice==3):
        room1()

#room 3
def room3(chance):
    print('''
\tyou are in room no 3 now!!!
\tnow you have 4 options...
\t\t1) go to room in front of you, room 8
\t\t2) go to room to your left, room 4
\t\t3) go tothe room behind you, room 0
\t\t4) go to the room in your right, room 2
''')
    user_choice=int(input("Enter your choice"))
    chance=chance+1
    if(chance>7):
        print("Sorry no chance left for you")
        fun()
    if(user_choice==1):
        room8()
    elif(user_choice==2):
        room4(chance)
    elif(user_choice==3):
        room0(chance)
    elif(user_choice==4):
        room2(chance)

#room 4
def room4(chance):
    print('''
\tyou are in room no 4 now!!!
\tnow you have 3 options...
\t\t1) go to room in front of you, room 7
\t\t2) go to room to your right, room 3
\t\t3) go tothe room behind you, room 5
''')
    user_choice=int(input("Enter your choice"))
    chance=chance+1
    if(chance>7):
        print("Sorry no chance left for you")
        fun()
    if(user_choice==1):
        room7(chance)
    elif(user_choice==2):
        room3(chance)
    elif(user_choice==3):
        room5()

#room5
def room5():
    print("You entered the room of the deads!!")
    print("Game over for you!!!!!!!!")
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=Furs535ly94")

#room6
def room6():
    print("You found the tressure....")
    print("You won!!!!!!!!!!!!! congo!!! party!!!!")
    
#room7
def room7(chance):
    print('''
\tyou are in room no 7 now!!!
\tnow you have 2 options...
\t\t1) go to room to your right, room 6
\t\t2) go tothe room behind you, room 4
''')
    user_choice=int(input("Enter your choice"))
    chance=chance+1
    if(chance>7):
        print("Sorry no chance left for you")
        fun()
    if(user_choice==1):
        room6()
    elif(user_choice==2):
        room4(chance)

#room8
def room8():
    print("You entered the room of the deads!!")
    print("Game over for you!!!!!!!!")
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=Furs535ly94")

room0(0)
