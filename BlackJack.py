import random
import time
import subprocess as sp

def playagain():
    main()
    

def gameover():
    print("\n====== You Crashed! ======")
    print("Game Over! \n")
    again = str(input("Do you wanna play again? \nAnswer: "))
    loop3 = 1
    while loop3 == 1: 
        if(again == "yes"):
            loop3 = 0
            playagain()
        elif(again == "no"):
            loop3 = 0
            print("Goodbye!\n")
            quit()
        else:
            print("Please select 'yes' or 'no'")

def computerwon():
    print("Your cards total:",player.cards)
    print("\nComputer cards total:",computer.cards,"\n")
    print("====== Computer Won ======")
    print("Game Over! \n".upper())
    again = str(input("Do you wanna play again? \nAnswer:"))
    loop3 = 1
    while loop3 == 1: 
        if(again == "yes"):
            loop3 = 0
            playagain()
        elif(again == "no"):
            loop3 = 0
            print("Goodbye!\n")
            quit()
        else:
            print("Please select 'yes' or 'no'")

def draw():
    print("Your cards total:",player.cards)
    print("Computer cards total:",computer.cards,"\n")
    print("====== Its Draw! ======".upper())
    print("Game Over! \n")
    again = str(input("Do you wanna play again? \nAnswer:"))
    loop3 = 1
    while loop3 == 1: 
        if(again == "yes"):
            loop3 = 0
            playagain()
        elif(again == "no"):
            loop3 = 0
            print("Goodbye!\n")
            quit()
        else:
            print("Please select 'yes' or 'no'") 

def won():
    print("")
    print("Your cards total:",player.cards + player.newcard)
    print("Computer cards total:",computer.cards)
    print("====== You Won! ======\n".upper())
    again = str(input("Do you wanna play again? \nAnswer: "))
    loop3 = 1
    while loop3 == 1: 
        if(again == "yes"):
            loop3 = 0
            playagain()
        elif(again == "no"):
            loop3 = 0
            print("Goodbye!\n")
            quit()
        else:
            print("Please select 'yes' or 'no'")  

def main():
    tmp = sp.call('clear',shell=True)
    print("\n========= BLACKJACK =========")
    loop6 = 1
    while loop6 == 1:
        tutorial = str(input("\nDo you wanna read tutorial?\nAnswer: ")) 
        if(tutorial == "yes"):
            print("\nFirst, you and Computer will take 2 cards.")
            print("If you get over of 21, you will lose.")
            print("If you and computer under of 21, higher score till 21 will win\n")
            loop6 = 0
            time.sleep(2)
        elif(tutorial == "no"):
            loop6 = 0
            time.sleep(1)
        else:
            print("Please select 'yes' or 'no'")
    playername = str(input("\nWhats your name?: "))
    global player
    player = Player(playername,random.randint(2,10),750)
    global computer
    computer = Computer("Computer",random.randint(2,10))
    game()

def computerstour():
    print("")
    print("Computer hidden card was:",computer.hidden)
    ifstatement = computer.cards == 21 and player.cards == 21
    loop4 = 1
    while loop4 == 1:
        if(computer.cards < player.cards):
            if(computer.cards < 21):
                computer.takecard()
                print("Computer took",computer.cards - computer.oldcards)
                computer.newcard = 0
                time.sleep(1)
            else:
                loop4 = 0
                won()
        elif(computer.cards == player.cards or ifstatement == True):
            draw()
        else:
            if(computer.cards <= 21):
                loop4 = 0
                computerwon()
            else:
                won()
            
        

class Player:
    
    count = 0

    def __init__(self, name,cards,credit):
        self.credit = credit
        self.name = name 
        self.cards = cards
        Player.count += 1

    def takecard(self):
        Player.oldcards = self.cards
        Player.newcard = random.randint(2,10)
        self.cards += Player.newcard


#class NewGame:
    
#    counter = 0
#    def __init__(self,name):
#        self.name = name      
#        NewGame.counter +=1

class Computer:

    def __init__(self,name,cards):
        self.name = name
        self.cards = cards
        Computer.hidden = cards

    def takecard(self):
        Computer.oldcards = self.cards
        Computer.newcard = random.randint(2,10)
        self.cards += Computer.newcard
 
 
def game():
    print("")
    print("Welcome", player.name+"!")
    print("Computer Card 1: Hidden")
    computer.takecard()
    print("Computer Card 2:",computer.newcard)
    time.sleep(1)
    print("")
    print("Your Card 1:",player.cards)
    player.takecard()
    print("Your Card 2:",player.newcard)
    player.newcard = 0
    time.sleep(1)
    loop2 = 1
    while loop2 == 1:
        if(player.cards > 21):
            loop2 = 0
            print("Your cards total:",player.cards,"\n")
            gameover()
        else:
            print("Your cards total:",player.cards,"\n")
            question = str(input("Do you wanna take card? \nAnswer: "))
            if(question == "yes"):
                player.takecard()
                print("You took",player.cards - player.oldcards)
                player.newcard = 0
                time.sleep(1)
            elif(question == "no"):
                loop2 = 0
                computerstour()
            else:
                print("Please select 'yes' or 'no'")

main()
