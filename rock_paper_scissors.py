import random

def fun():
    user = input("'r'= rock\n'p'=paper\n's'=scissors\nwhat is your choice? :")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return "its a tie"
        
    if is_win(user,computer):
        return "you won!"
    
    
    return "you lost!"
    
def is_win(player,opponent):
    if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p' )or (player == 'p' and opponent == 'r') :
        return True  
    
print(fun())