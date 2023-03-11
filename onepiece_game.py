print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the world of One Piece.")
print("Can you survive in world of the Pirates?")

print("How to play this Game!\n1. Choose between the given Options.\n2. Dont not type anything other than the given options or you will end up losing the game!\nGood Luck")

stage1 = input("Ask any one of them to be your partner: 'Shanks' or 'BlackBeard'!\n")

if stage1 == "Shanks" or stage1 == "shanks":
    print("Shanks agreed to be your partner and get on your board.\n")
    stage1_1 = input("Shanks : Which island you wanna visit 'Eligia' or 'Sabaody' ?\n")
    if stage1_1 == "Eligia" or stage1_1 == "eligia":
        print("You Ended up Dying fighting the Tol Musica: The Ghost!!\n")
    elif stage1_1 == "Sabaody" or stage1_1 == "sabaody":
        stage1_12 = input("You got caught up in a Sabaody incident! You are now sorrounded by Navy! Escape with Shanks or Betray Him!!\nChoose between 'Escape' and 'Betray'!\n")
        if stage1_12 == "Escape" or stage1_12 == "escape":
            print("You Successfully Escape the navy without any problem!\n")
            stage1_13 = input("Shanks : You are a good Pirate! Tell me what is Dream!\nChoose between 'Fight Him' or Be a 'Pirate King'\n")
            if stage1_13 == "Fight Him" or stage1_13 == "fight him" or stage1_13 == "fighthim":
                print("You ended up dying in the fight with Shanks! Game over!!\n")
            elif stage1_13 == "Pirate King" or stage1_13 == "pirate king" or stage1_13 == "pirateking":
                print("Shanks got impressed with your answer and gives you his Straw Hat! And you continue you Journey to be Pirate King\n")
                print("Next Part is coming soon!")
            else:
                print("Invalid Input! Game Over!")
        elif stage1_12 == "Betray" or stage1_12 == "betray":
            print("Navy Defeated you n Ended up in Prison Game over!!!")
        else:
            print("Invalid Input! Game Over!")
    else:
        print("Invalid Input! Game Over!!")

elif stage1 == "BlackBeard" or stage1 == "blackbeard":
    print("BlackBeard decided to be your partner, gets on board.")
    stage1_2 = input("Follow Blackbeard or Order BlackBread:\nChoose between Follow or Order: ")
    if stage1_2 == "Betray" or stage1_2 == "betray":
        print("You got caught by the Navy n sent to Impel Down! Game Over!")
    elif stage1_2 == "Order" or stage1_2 == "order":
        print("BlackBeard denies you n betrays you! Better Luck Next time! Game over!!!")
    else:
        print("Invalid Input! Game Over!!")

else:
    print("Invalid Input! Game Over!!")

