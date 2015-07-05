# Rock-paper-scissors-lizard-Spock 



def name_to_number(name):
       
    if name == "Rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "Paper":
        return 2
    elif name == "Lizard":
        return 3
    elif name == "Scissors":
        return 4
    
    

def number_to_name(number):

    if number == 0:
        return "Rock"
    elif number == 1:
        return "Spock" 
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Lizard"
    elif number == 4:
        return "Scissors"
    
    
import random


input = raw_input("Choose Rock, Spock, Lizard, Paper or Scissors! \n")

a = name_to_number(input) + random.randrange(0, 5)
z = a - name_to_number(input)
x = number_to_name(z)
point = a
p= "Win!"
d= "Draw!"
c= "Lost!"


#Rock Function

def winner(point):
    if point > 2:
        return p
    elif point == 0:
        return d
    else:
        return c 


#Spock Function

def winner1(point):
    if (point % 4) == 1:
        return p
    elif (point % 4) == 2:
        return d
    else:
        return c    
    

#Paper Function

def winner2(point):
    if point == 2 :
        return p
    elif point == 3:
        return p  
    elif point == 4:
        return d
    else:
        return c



#Lizard Function

def winner3(point):
    if point == 5:
        return p
    elif point == 4:
        return p
    elif point == 6:
        return d
    else:
        return c


#Scissors Function

def winner4(point):
    if point == 7:
        return p
    elif point == 6:
        return p
    elif point == 8:
        return d
    else:
        return c



#Switch to each Functions

def inp(input):
    if input == "Rock":
        return winner(point)
    elif input == "Spock":
        return winner1(point)
    elif input == "Paper":
        return winner2(point)
    elif input == "Lizard":
        return winner3(point)
    elif input == "Scissors":
        return winner4(point)
    else:
        print "Pilih sesuai daftaaar!!!!"
        return

    print''
    print "You Choose", input + "!"
    print "The Computer choose", x + "!"
    print "You are", inp(input)
    print ''
