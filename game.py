import random
l=["rock","paper","scissor"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
      game start...
      1.yes
      2.no/exit
      '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input ('''
            1.rock
            2.paper
            3.scissor
             '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="paper"
            elif userinput==3:
                uchoice="scissor"
            cchoice=random.choice(l)
            print(uchoice)
            print(cchoice)
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("computer value",cchoice)
                print("user value",uchoice)
                print("game draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock"and cchoice=="scissor")or(uchoice=="paper"and cchoice=="rock")or(uchoice=="scissor"and cchoice=="paper"):
                print("computer value",cchoice)
                print("user value",uchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("computer value",cchoice)
                print("user value",uchoice)
                print("computer win")
                ccount=ucount+1
            if ucount==ccount:
                print("final game draw")
                print("user score",ucount)
                print("computer score",ccount)
            elif ucount>ccount:
                print("final game you win")
                print("user score",ucount)
                print("computer score",ccount)
            else:
                print("computer win the game")
                print("user score",ucount)
                print("computer score",ccount)
        else:
         break



