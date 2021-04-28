import random
def main():
    # (a,b) guess intervals
    a=0
    b=100
    # choose the computer guess or user to guess
    choose=input('User or Computer:')
    if choose=='Computer' or choose=='computer':
        Computer(a,b)
    elif choose=='User' or choose=='user':
        User(a,b)
def Computer(a,b):
    # -The user guess the number be using binary search
    found=False
    low=a
    high=b+1    
    guess_list=list(range(a,b+1))
    while not found:
        guess=(low+high)//2
        print('Computer Guess:'+str(guess))
        hint=input()
        if hint=='win':
            print('Hooray the computer won')
            found=True
        elif hint=='+':
            low=guess+1
        elif hint=='-':
            high=guess-1
        elif hint=='exit':
            break
def User(a,b):
    # -The user to guess a random number created by the computer
    found=False
    answer=random.randint(a,b)
    guess_times=8
    i=0
    while i<guess_times and not found:
        guess=int(input('Your Guess:'))
        if guess==answer:
            print('Hooray you won!')
            found=True
        elif guess<answer:
            print('Too Low.')
        elif guess>answer:
            print('Too High.')
        i+=1
    
main()