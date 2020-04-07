#!/usr/bin/env python3
ans = " "

while ans != "No":
    ans = input('Lets play the random questions game, answer this: "Is water wet? Yes or no? There is only one right answer": ').lower().strip()
    if ans == "yes": 
        print("INCORRECT! Your answer was dumb and you probably have a dumb name like Chad")
        break
    elif ans == "no":
        print("Correct! You are obviously one of the smartest people in your class and probably the next Einstein!")
        break
    else:
        print("ANSWER THE QUESTION! only options are yes or no!")

while ans != "Marvel":
    ans = input('Next question: Is Marvel or DC better?: ').lower().strip()
    if ans == "marvel":
        print("Correct!, but the DC is cool too")
        break
    elif ans == "dc":
        print("Incorrect! But Marvel is cool too")
        break
    else:
        print("ANSWER THE QUESTION! Only option is Marvel or DC!")
        
while ans != "Cookie":
    ans = input('Final question! What part of an Oreo taste best? Cookie or cream?: ').lower().strip()
    if ans == "cream":
        print("Correct!, you have cured cancer and saved humanity!")
        break
    elif ans == "cookie":
        print("Incorrect! You have doomed humanity to Covid19")
        break
    else:
        print("ANSWER THE QUESTION! Only option is cookie or cream!")

