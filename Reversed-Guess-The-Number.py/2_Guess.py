print("Please enter \"h\" fir Higher or \"l\" for Lower if the aanswer is not \'c\' Correct ")

digits = int(input ('How amny digits does the number have?'))

def highlow(guess):
    ans = input('is the guess higher or lower ?')
    while ans != "c":
        
        if ans == 'h' :
            guess -= 2
            print(guess) 
        elif ans=='l':
            guess += 2
            print(guess) 
    if ans == 'c':
            print('The guess was Correct')
        

if digits ==1 :
    num = (input("Is the numbder Even or Odd?"))
    if num == "even":
        guess =2 
        print(guess)
        highlow(guess)
    else:
        guess =1
        print(guess)
        highlow(guess)

def twohighlow(guess):
    ans = input('is the guess higher or lower ?')
    while ans != "c": 
            if ans == 'h' and guess > 10+int(num)  :
                guess -= 10
                print(guess) 
            elif ans == 'l' and guess <= 99:
                guess += 10
                print(guess) 
            else:
                print("incorrect input Try again")
            ans = input('is the guess higher or lower ?')
    if ans == 'c':   
         print('The guess was Correct')
            
if digits ==2 :
     num = (input("what is the number at ones palce?"))
     guess = 10+ int(num)
     print(guess)
     twohighlow(guess)
     



