
boardBegin = [  [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "] ]
x = boardBegin

def printBoard(x):
        
    print(f'''
     ___________
    | {x[0][0]} | {x[0][1]} | {x[0][2]} |
    |___|___|___|
    | {x[1][0]} | {x[1][1]} | {x[1][2]} |
    |___|___|___|
    | {x[2][0]} | {x[2][1]} | {x[2][2]} |
    |___|___|___|
''')

def chooseSpace(x):
    choiceRow = input('Which row would You Like to place your piece? \n(awnser "Top", "Middle" or "Bottom")\n').lower
    choiceCulum = input('Which culum would You Like to place your piece? \n(awnser "Left", "Middle" or "Right")\n').lower
    if choiceRow == "top":
        choiceRow = 0
    elif choiceRow == "Middle":
        choiceRow = 1
    else:
        choiceRow = 2

        

printBoard(x)
chooseSpace(x)
