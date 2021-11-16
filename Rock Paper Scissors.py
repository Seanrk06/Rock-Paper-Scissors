
def main():

    import random 
    import time

    # countdown
    def timer():
        print("\n3")
        slow = time.sleep(2)
        print("2")
        slow = time.sleep(2)
        print("1 \n")
        slow = time.sleep(2)

    # confirmation of 'attack'
    def attackc():
        print(usera)
        userac = input("is the statement above your attack?, please confirm: ")
        if userac == 'yes':
            timer()
        else:
            print("please stop the program or confirm \n")

    # prompts user for ready confirmation
    go = True 
    while go:
        ready = input("are you ready?: ")
        if ready == 'yes':
            timer()
            go = False
        else:
            print("please type 'yes' ")


    flag1 = True
    while flag1:
        #prompts user for 'attack'
        usera = input("what will your attack be? (rock paper or scissors): ")
        if usera == 'rock':
            print(usera)
            flag1 = False
            flag4 = True
            while flag4:
                userac = input("is the statement above your attack?, please confirm: ")
                if userac == 'yes':
                    flag4 = False
                    timer()
                else:
                    print("\nplease stop the program or confirm")
            

        if usera == 'paper': 
            print(usera)
            flag1 = False
            flag4 = True
            while flag4:
                userac = input("is the statement above your attack?, please confirm: ")
                if userac == 'yes':
                    flag4 = False
                    timer()
                else:
                    print("\nplease stop the program or confirm")
            

        
        if usera == 'scissors':
            print(usera)
            flag1 = False
            flag4 = True
            while flag4:
                userac = input("is the statement above your attack?, please confirm: ")
                if userac == 'yes':
                    flag4 = False
                    timer()
                else:
                    print("\nplease stop the program or confirm")
            

    #creates computers 'attack'
    compattack = random.randint(1,3)
    if compattack == 1:
        compattack = "rock"
    if compattack == 2:
        compattack = "paper"
    if compattack == 3:
        compattack = "scissors"
    print("your attacker has chosen:",compattack)

    win = 0
    loss = 0
    tie = 0


    flag = True
    while flag:
        if compattack == "rock":
            if usera == "rock":
                print("both you and your oppenent have chosen the same attacks!")
                tie += 1
                flag = False
            if usera == "paper":
                print("you have won congratulations")
                win += 1
                flag = False
            if usera == "scissors":
                print("your attacker has won")
                loss += 1
                flag = False

        if compattack == "paper":
            if usera == "paper":
                print("both you and your oppenent have chosen the same attacks!")
                tie += 1
                flag = False
            if usera == "rock":
                print("your attacker has won")
                loss += 1
                flag = False
            if usera == "scissors":
                print("you have won congratulations")
                win += 1
                flag = False

        if compattack == "scissors":
            if usera == "scissors":
                print("both you and your oppenent have chosen the same attacks!")
                tie += 1
                flag = False
            if usera == "rock":
                print("you have won congratulations")
                win += 1
                flag = False
            if usera == "rock":
                print("your attacker has won")
                loss += 1
                flag = False
    # prompts user to play again
    continueq = input("\n Do you want to play another round: ")
    if continueq == "yes":
        main()
    else:
        print("you got,",win,"wins,",loss,"losses in addition to",tie,"ties" )

main()

