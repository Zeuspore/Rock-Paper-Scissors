import random

print("Welcome to Rock Paper Scissors \n")
choices=["R", "P", "S"]

#computer chooses randomly
CPU=random.choice(choices)

#My code    
while True:
    player=input("Input your selection from the options below\n R=Rock\n P=Paper\n S=Scissors\n ").upper().strip()

    if player == CPU:
        print(f"Player selected ({player}) : CPU selected ({CPU})")
        print("It is a Tie!")
        
    
    elif player == "R":
            if CPU == "P":
                print(f"Player selected ({player}) : CPU selected ({CPU})")
                print("CPU Win!")
                break
            
            if CPU == "S":
                print(f"Player selected ({player}) : CPU selected ({CPU})")
                print("You Win!")
                break
            
    elif player == "P":
            if CPU == "R":
                print(f"Player selected ({player}) : CPU selected ({CPU})")
                print("You Win!")
                break
            if CPU == "S":
                print(f"Player selected ({player}) : CPU selected ({CPU})")
                print("CPU Win!")
                break            
    elif player == "S":
            if CPU == "R":
                print(f"Player selected ({player}) : CPU selected ({CPU})")
                print("CPU Win!")
                break
            if CPU == "P":
                print(f"Player selected ({player}) : CPU selected ({CPU})")
                print("You Win!")
                break
    else:
         print("Wrong Input")
         
    
            
        