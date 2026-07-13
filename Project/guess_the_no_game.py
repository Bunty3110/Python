# guess the no game
from random import randint
num=randint(0,10)

while True:
    try:
        guess=int(input('make a guess between 0 to 10     '))
        if 0<=guess<11:
            if guess==num:
                print("you made a right guess")
                break
            else:
                print("wrong guess you missed by", abs(num-guess))
                print("try again")
              
        else:
            print("guess between 0 and 10 , Comeon retry")
     
    except ValueError:
        print("please guess a number in int")
            