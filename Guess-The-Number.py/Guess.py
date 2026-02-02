import random
x = random.randint(10,100)


def hints(n,x,g):
    if n == 1 :
        if x % 2 != 0 :
            print("Odd")
        else:
            print("Even")

    elif n == 2 :
        print(x%10)

    elif n == 3 :
        if (x // 10) % 2 != 0:
            print("Odd")
        else:
            print('Else')

    elif n == 4 :
        print(abs(g-x))

    elif n == 5 :
        if g > x:
            print('High')
        else :
            print('Low')
    else :
        print('INVALID NUMBER')

def process_hints(g,x):
    hint_no = int(input("Enter the hint number you want to use :"))
    hints(hint_no,x,g)




def game():
        #Initial guess
        g = int(input("Enter your double digit lucky number : "))
        if g == x :
            print('YOU WIN!!')
            return

        #First hint
        process_hints(g,x)

        #First guess
        g = int(input("Enter your First guess :"))
        if g == x :
            print('YOU WIN!!')
            return

        #Second hint
        process_hints(g,x)


        #Second guess
        g = int(input("Enter your Second guess :"))
        if g == x :
            print('YOU WIN!!')
            return


        #Third hint 
        process_hints(g,x)


        #Third guess
        g = int(input("Enter your Third guess :"))
        if g == x :
            print('YOU WIN!!')
        else :
            print('YOU LOOSE \n Correct Answer ', x)

game()