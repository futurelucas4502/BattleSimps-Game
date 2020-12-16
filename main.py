from tkinter import *  # importing a gui library
import tkinter.messagebox as mb

# sadly this code is incomplete due to the fact i have to leave in less than 15 mins ill probably be gone by the time u read this
# this is v1 so very messy
# a v2 will be made after v1 is finished as it was fun to make XD

# Main user logic

global firstCoords  # create global variable for first button location
global lastCoords  # create global variable for second button location
global simps  # create global variable for battle simps (battleships)
# initialise variables with values so we can easily check if its the first point of the ship/simp or the second point
firstCoords = [-1, -1]
lastCoords = [-1, -1]  # read above
simps = [5, 4, 3, 3, 2]  # the ships/simps and their lengths


def firstButtonPress(x, y):
    global firstCoords
    print("wow")
    if (len(simps) > 0):
        # if we select a square thats already blue this will error out with an error box
        if (yourGrid[x][y].cget("bg") == "blue"):
            mb.showerror(
                "Error", "You can't do this your ships would be overlapping")
        else:
            firstCoords = [x, y]  # set first coordiantes
            # set coordinate blue to indicate start of simp/ship selection
            yourGrid[x][y].configure(bg="blue")


def lastButtonPress(x, y):
    global firstCoords
    print("such magic")
    if (firstCoords[0] == x and firstCoords[1]==y): # if in same place as first press
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white") # set to white as otherwise ship would be 1 long which is impossible
        firstCoords = [-1, -1] # reset firstCoords to prevent issues

    elif (yourGrid[x][y].cget("bg") == "blue"): # if spot already blue then prevent ship being placed as overlapping
        mb.showerror(
            "Error", "You can't do this your ships would be overlapping")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        firstCoords = [-1, -1]

    elif (firstCoords[0] == x): # if on same x coord as first button press good
        yourGrid[x][y].configure(bg="blue") # set blue
        firstCoords = [-1, -1] # reset firstCoords to allow for new ship

    elif (firstCoords[1] == y):
        yourGrid[x][y].configure(bg="blue")
        firstCoords = [-1, -1]

    else: # else diagonally
        mb.showerror("Error", "You can't place simps diagonally!")
        yourGrid[firstCoords[0]][firstCoords[1]].configure(bg="white")
        firstCoords = [-1, -1]


# Window creation etc
window = Tk()  # make a window
window.title("OWO - BattleSimps")  # game/window name
window.geometry('600x320')  # setup window size

top = Frame(window)
bottom = Frame(window)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, expand=True)

# the main battleships frame. relief = the style of the border for the frame
yourFrame = Frame(top, borderwidth=1, relief="solid", width=200, height=200)
yourFrame.pack(in_=top, side=LEFT, padx=10, pady=10)  # pack it into the window

wLbl = Label(
    top, text="ω", font=("Courier", 50))  # Label for the input box
wLbl.pack(in_=top, side=LEFT)


# the main battleships frame. relief = the style of the border for the frame
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
