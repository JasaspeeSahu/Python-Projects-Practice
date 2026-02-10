import random 

print("WELCOME! TO THE ULTIMATE GAME OF ROCK, PAPER AND SCCISORS")
def play():
    user = input("Enter your choice. \n \"r\" for Rock , \"p\" for Paper and \'s\' for Scissors. " )
    computer = random.choice(["r","p","s"])

    
    
    if is_win(user,computer) :
        print(computer)
        print ('YOU WON')
    elif user == computer :
        print(computer)
        print(" It\'s a TIE")
    else:
        print(computer)
        print('YOU LOST') 
    



def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent =='p') or (player =='p' and opponent =='r'):
        return True 
    
play() 