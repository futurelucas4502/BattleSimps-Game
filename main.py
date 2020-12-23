from tkinter import *  # importing the gui library
import tkinter.messagebox as mb

# Main user logic

global firstCoords  # create global variable for first button location
global simps  # create global variable for battle simps
global overlap # create a global variable to check if things overlap
global bIsSimpAvaliable
# initialise variables with values so we can easily check if its the first point of the simp or the second point
firstCoords = [-1, -1]
simps = [5, 4, 3, 3, 2]  # the simps and their lengths
overlap = False
bIsSimpAvaliable = False


def firstButtonPress(x, y):
    global firstCoords
    if (len(simps) > 0):
        # if we select a square thats already blue this will error out with an error box
        if (yourGrid[x][y].cget("bg") == "blue"):
            mb.showerror(
                "Error", "You can't do this your simps would be overlapping")
        else:
            firstCoords = [x, y]  # set first coordiantes
            # set coordinate blue to indicate start of simp selection
            yourGrid[x][y].configure(bg="blue")


def lastButtonPress(x, y):
    global firstCoords
    if (firstCoords[0] == x and firstCoords[1] == y):  # if in same place as first press
        # set to white as otherwise simp would be 1 long which is impossible
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        firstCoords = [-1, -1]  # reset firstCoords to prevent issues

    # if spot already blue then prevent simp being placed as overlapping
    elif (yourGrid[x][y].cget("bg") == "blue"):
        mb.showerror(
            "Error", "You can't do this your simps would be overlapping")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        firstCoords = [-1, -1]

    elif (firstCoords[0] == x):  # if on same x coord as first button press good
        # since its on the same x coord we need to look at the y length and coords
        # if its less than 5 and greater than 0 its a valid simp with firstCoords below
        if (firstCoords[1] - y < 5 and firstCoords[1] - y > 0):
            yourGrid[x][y].configure(bg="blue")  # set blue
            firstCoordsBelow(x, y)
        # elif its greater than -5 and less than 0 then its a valid simp with firstCoords above
        elif (firstCoords[1] - y > -5 and firstCoords[1] - y < 0):
            yourGrid[x][y].configure(bg="blue")  # set blue
            firstCoordsAbove(x, y)
        else:  # it's more than 5 so we need to reset the firstcoords to white
            yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        # reset firstCoords to allow for new simp no matter what
        firstCoords = [-1, -1]

    elif (firstCoords[1] == y):  # if on same y coord as first button that was pressed
        # since its on the same y coord we need to look at the x length and coords
        # if its less than 5 and greater than 0 its a valid simp with firstCoords on the right
        if (firstCoords[0] - x < 5 and firstCoords[0] - x > 0):
            yourGrid[x][y].configure(bg="blue")  # set blue
            firstCoordsRight(x, y)
        # elif its greater than -5 and less than 0 then its a valid simp with firstCoords on the left
        elif (firstCoords[0] - x > -5 and firstCoords[0] - x < 0):
            yourGrid[x][y].configure(bg="blue")  # set blue
            firstCoordsLeft(x, y)
        else:  # it's more than 5 so we need to reset the firstcoords to white
            yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        firstCoords = [-1, -1]  # always reset the firstCoords!

    else:  # else diagonally
        mb.showerror("Error", "You can't place simps diagonally!")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        firstCoords = [-1, -1]


# Place simp logic


def firstCoordsLeft(x, y):
    print("in firstCoordsLeft function")
    global firstCoords
    global overlap
    global bIsSimpAvaliable
    # distance between the two and is less than 0 so has to be converted to a positive
    distance = -(firstCoords[0] - x)
    tempx = x
    for i in range(distance-1):  # loop the distance and check if any of the things would overlap without colouring them and if they do set Overlap to True
        tempx -= 1
        if(yourGrid[tempx][y].cget("bg") == "blue"):
            overlap = True
    
    for i in range(len(simps)):  # for each simp
        if (distance+1 == simps[i]):
            bIsSimpAvaliable = True

    if (overlap == False and bIsSimpAvaliable == True):
        simps.remove(distance+1)
        for i in range(distance-1):  # loop the distance
            x -= 1
            yourGrid[x][y].configure(bg="blue")  # set blue

    elif (overlap == True):
        mb.showerror(
            "Error", "You can't do this your simps would be overlapping")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        yourGrid[x][y].configure(bg="white")

    elif (bIsSimpAvaliable == False):
        mb.showerror(
            "Error", "You can't do this you've placed all the simps that are this length")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        yourGrid[x][y].configure(bg="white")

    overlap = False
    bIsSimpAvaliable = False


def firstCoordsAbove(x, y):
    print("in firstCoordsAbove function")
    global firstCoords
    global overlap
    global bIsSimpAvaliable
    # distance between the two and is less than 0 so has to be converted to a positive
    distance = -(firstCoords[1] - y)
    tempy = y
    for i in range(distance-1):  # loop the distance and check if any of the things would overlap without colouring them and if they do set Overlap to True
        tempy -= 1
        if(yourGrid[x][tempy].cget("bg") == "blue"):
            overlap = True
    
    for i in range(len(simps)):  # for each simp
        if (distance+1 == simps[i]):
            bIsSimpAvaliable = True

    if (overlap == False and bIsSimpAvaliable == True):  # if overlap == False
        simps.remove(distance+1)
        for i in range(distance-1):  # loop the distance
            y -= 1
            yourGrid[x][y].configure(bg="blue")  # set blue
    
    elif (overlap == True):
        mb.showerror(
            "Error", "You can't do this your simps would be overlapping")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        yourGrid[x][y].configure(bg="white")

    elif (bIsSimpAvaliable == False):
        mb.showerror(
            "Error", "You can't do this you've placed all the simps that are this length")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        yourGrid[x][y].configure(bg="white")

    overlap = False
    bIsSimpAvaliable = False


def firstCoordsBelow(x, y):
    print("in firstCoordsBelow function")
    global firstCoords
    global overlap
    global bIsSimpAvaliable
    # distance between the two and is greater than 0 :)
    distance = firstCoords[1] - y
    tempy = y
    for i in range(distance-1):  # loop the distance
        tempy += 1
        if(yourGrid[x][tempy].cget("bg") == "blue"):
            overlap = True

    for i in range(len(simps)):  # for each simp
        if (distance+1 == simps[i]):
            bIsSimpAvaliable = True

    if (overlap == False and bIsSimpAvaliable == True):  # if overlap == False
        simps.remove(distance+1)
        for i in range(distance-1):  # loop the distance
            y += 1
            yourGrid[x][y].configure(bg="blue")  # set blue

    elif (overlap == True):
        mb.showerror(
            "Error", "You can't do this your simps would be overlapping")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        yourGrid[x][y].configure(bg="white")

    elif (bIsSimpAvaliable == False):
        mb.showerror(
            "Error", "You can't do this you've placed all the simps that are this length")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        yourGrid[x][y].configure(bg="white")
    
    overlap = False
    bIsSimpAvaliable = False


def firstCoordsRight(x, y):
    print("in firstCoordsRight function")
    global firstCoords
    global overlap
    global bIsSimpAvaliable
    # distance between the two and is greater than 0 :)
    distance = firstCoords[0] - x
    tempx = x
    for i in range(distance-1):  # loop the distance
        tempx += 1
        if(yourGrid[tempx][y].cget("bg") == "blue"):
            overlap = True
    
    for i in range(len(simps)):  # for each simp
        if (distance+1 == simps[i]):
            bIsSimpAvaliable = True

    if (overlap == False and bIsSimpAvaliable == True):  # if overlap == False
        simps.remove(distance+1)
        for i in range(distance-1):  # loop the distance
            x += 1
            yourGrid[x][y].configure(bg="blue")  # set blue

    elif (overlap == True):
        mb.showerror(
            "Error", "You can't do this your simps would be overlapping")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        yourGrid[x][y].configure(bg="white")

    elif (bIsSimpAvaliable == False):
        mb.showerror(
            "Error", "You can't do this you've placed all the simps that are this length")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        yourGrid[x][y].configure(bg="white")

    overlap = False
    bIsSimpAvaliable = False


# Window creation etc
window = Tk()  # make a window
window.title("OWO - BattleSimps")  # game/window name
window.geometry('600x320')  # setup window size

top = Frame(window)
bottom = Frame(window)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, expand=True)

# the main battlesimps frame. relief = the style of the border for the frame
yourFrame = Frame(top, borderwidth=1, relief="solid", width=200, height=200)
yourFrame.pack(in_=top, side=LEFT, padx=10, pady=10)  # pack it into the window

wLbl = Label(
    top, text="ω", font=("Courier", 50))  # Label for the input box
wLbl.pack(in_=top, side=LEFT)


# the main battlesimps frame. relief = the style of the border for the frame
trackingFrame = Frame(top, borderwidth=1,
                      relief="solid", width=200, height=200)
trackingFrame.pack(in_=top, side=RIGHT, padx=10,
                   pady=10)  # pack it into the window

yourGrid = [[Button() for a in range(10)]
            for b in range(10)]  # predefine variable array size and types
for x in range(10):  # create x axis
    for y in range(10):  # create y axis
        yourGrid[x][y] = Button(
            yourFrame, width=2, height=1, command=lambda x=x, y=y: firstButtonPress(x, y) if firstCoords == [-1, -1] else lastButtonPress(x, y), bg="white")  # add buttons to array
        yourGrid[x][y].grid(column=x, row=y)  # add array to grid

trackingGrid = [[a for a in range(10)] for b in range(10)]
for x in range(10):
    for y in range(10):
        trackingGrid[x][y] = Button(
            trackingFrame, width=2, height=1, bg="white")
        trackingGrid[x][y].grid(column=x, row=y)

gridCoordsLbl = Label(
    bottom, text="Score: 0")  # Label for score
gridCoordsLbl.pack()

window.mainloop()  # mainwindow loop a blocking process to keep the window open
