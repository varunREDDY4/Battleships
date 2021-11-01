"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["no_of_rows"]=10
    data["no_of_cols"]=10
    data["boardsize"]=500
    data["cellsize"]=data["boardsize"]/data["no_of_cols"]
    data["no_of_ships_comp"]=5
    data["no_of_ships_user"]=5
    data["comp_board"]=emptyGrid(data["no_of_rows"],data["no_of_cols"])
    data["user_board"]=emptyGrid(data["no_of_rows"],data["no_of_cols"])
    # data["comp_board"]=addShips(data["comp_board"],data["no_of_ships_comp"])
    data["temp_ship"]=[ ] 
    data["user_ship"] = 0
    data["winner"] = None
    data["max_no_turns"] = 50 
    data["current_no_turns"] = 0

    return


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
   
    
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    
    grid =[]
    for i in range(rows):
        # an empty list is created
        boardString=[]
        for j in range(cols):
            boardString.append(1)
        grid.append(boardString)
    return grid

    


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    rows=random.randint(1,8)
    cols=random.randint(1,8)
    edge=random.randint(0,1)
    createShip=[]
    if edge == 0:
        for i in range(rows-1,rows+2):
            createShip.append([i,cols])
    else:
        for j in range(cols-1,cols+2):
            createShip.append([j,rows])
    return createShip
    


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in ship:
        if grid[i[0]][i[1]]!=EMPTY_UNCLICKED:
            return False
    return True
    


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    ship_count=0
    while(ship_count<numShips):
        ship=createShip()
        if checkShip(grid,ship):
            for i in ship:
                grid[i[0]][i[1]] = SHIP_UNCLICKED
            ship_count+=1
        # print("add ships is executing")
    return grid
    


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    x = data["cellsize"]
    for row in range(data["no_of_rows"]):
        for col in range(data["no_of_cols"]):
            if grid[row][col] == SHIP_UNCLICKED:
                canvas.create_rectangle(x*col,x*row,x*(col+1),x*(row+1),fill="yellow")
            elif grid[row][col] == EMPTY_UNCLICKED:
                canvas.create_rectangle(x*col,x*row,x*(col+1),x*(row+1),fill="blue")
            elif grid[row][col] == SHIP_CLICKED:
                canvas.create_rectangle(x*col,x*row,x*(col+1),x*(row+1),fill="red")
            elif grid[row][col] == EMPTY_CLICKED:
                canvas.create_rectangle(x*col,x*row,x*(col+1),x*(row+1),fill="white")
            if grid[row][col] == SHIP_UNCLICKED and showShips == False:
                canvas.create_rectangle(x*col,x*row,x*(col+1),x*(row+1),fill="blue")
    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    if ship[0][1] == ship[1][1] == ship[2][1]:
        if ship[0][0]+1 == ship[1][0] == ship[2][0]-1:
            return True 
    return False
    
    


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    if ship[0][0] == ship[1][0] == ship[2][0]:
        if ship[0][1]+1 == ship[1][1]  == ship[2][1]-1:
            return TRUE
    return False
    
    


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    x= int(event.x/data["cellsize"])
    y= int(event.y/data["cellsize"])
    return [y,x]
    


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    x = data["cellsize"]
    for i in range(len(ship)):
        y=(ship[i])
        canvas.create_rectangle(x*(y[1]),x*(y[0]),x*(y[1]+1),x*(y[0]+1),fill="white")
    
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if checkShip(grid,ship):
        if isVertical(ship) or isHorizontal(ship):
            return True
    return False
    


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["user_board"], data["temp_ship"]):
        for i in data["temp_ship"]:
            data["user_board"][i[0]][i[1]] = SHIP_UNCLICKED
        data["user_ship"] +=1
    else:
        print("ship is not valid")
    data["temp_ship"] = []

    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["user_ship"] == 5:
            return
    if[row,col] in data["temp_ship"]:
        return
    data["temp_ship"].append([row,col])

    if len(data["temp_ship"]) ==3:
        placeShip(data)
    if data["user_ship"] == 5:
        print("you can start the game")
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    x=board[row][col]
    if x == SHIP_UNCLICKED:
        x = SHIP_CLICKED
    elif x == EMPTY_UNCLICKED:
        x = EMPTY_CLICKED
    board[row][col] = x
    if isGameOver(board):
        data["winner"] = player
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if data["comp_board"][row][col] == SHIP_CLICKED or data["comp_board"][row][col] == EMPTY_CLICKED:
        return
    else:
        updateBoard(data,data["comp_board"],row,col,"user")
        # print(row,col)
    event = getComputerGuess(data["user_board"])
    print(event)
    updateBoard(data,data["user_board"],event[0],event[1],"comp")
    data["current_no_turns"] +=1
    if data["current_no_turns"] == data["max_no_turns"]:
        data["winner"] = "draw"
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    row=random.randint(0,9)
    col=random.randint(0,9)
    while board[row][col] == SHIP_CLICKED or board[row][col] == EMPTY_CLICKED:
        row=random.randint(0,9)
        col=random.randint(0,9)
    print(board[row][col])
    if board[row][col] == EMPTY_UNCLICKED or board[row][col] == SHIP_UNCLICKED:
        return[row,col]
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
     return


    


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return

    


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    # runSimulation(500, 500)
