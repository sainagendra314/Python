
import simplegui
import random
import math 

max = 100
guess_val = None 
    
def new_game():
    '''starts new game by generating new secret number'''
    
    global secret_number
    global remain_guess 
    
    secret_number = random.randint(0,max)
    print(secret_number)
      
    remain_guess=int(math.ceil(math.log(max,2)))
    
def range100():
    global max
    max = 100
    new_game()

def range1000():
    global max
    max = 1000
    new_game()

def input_guess(guess):
    ''' takes input from user and determine if number proximity
    and reduces the count of remaining guess by one '''
    global guess_val
    global remain_guess
    
    guess_val = int(guess)
     
    if guess_val>secret_number:
        print "is greater "
        remain_guess -= 1
        print "remaining guess",remain_guess
        
    elif guess_val<secret_number:
        print "is less" 
        remain_guess -= 1
        print "remaining guess",remain_guess

    elif guess_val == secret_number:
        print "is correct" 
        new_game()
        
f=simplegui.create_frame("guess the number",200,200)
f.add_button("Range is (0,100]",range100,200)
f.add_button("Range is (0,1000]",range1000,200)
f.add_input("Enter a guess",input_guess,200)
new_game()
f.start()
