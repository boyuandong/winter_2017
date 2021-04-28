import random
def main():
    guess_times=0
    random_num=random.randint(1,20)
    continue_game=True
    # game continues when wrong guess less than 6 and the player does not gess the correct number
    while guess_times<6 and continue_game:
        enter_num=input("Enter a guess (1-20): ")
        enter_num=int(enter_num)
        # if the player guesses the number not between 1 and 20
        if enter_num<1 or enter_num>20:
            print("That number is not between 1 and 20!")
        else:
            # if the player guesses the correct number the game ends
            if enter_num==random_num:
                print("Correct! The number was "+str(random_num)+".")
                continue_game=False
            # if the player does not guess the correct number
            else:
                # wrong guesses plus 1
                guess_times+=1
                # print the warning
                if enter_num>random_num:
                    print("Too high!")
                elif enter_num<random_num:
                    print("Too low!")
            
main()