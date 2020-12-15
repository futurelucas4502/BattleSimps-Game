from tkinter import *  # importing a gui library
import tkinter.messagebox as mb

# sadly this code is incomplete due to the fact i have to leave in less than 15 mins ill probably be gone by the time u read this
# this is v1 so very messy
# a v2 will be made after v1 is finished as it was fun to make XD

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

global firstCoords  # create global variable for first button location
global lastCoords  # create global variable for second button location
global simps  # create global variable for battle simps (battleships)
# initialise variables with values so we can easily check if its the first point of the ship/simp or the second point
firstCoords = [-1, -1]
lastCoords = [-1, -1]  # read above
simps = [5, 4, 3, 3, 2]  # the ships/simps and their lengths


def btnPressed(x, y):
    # add the global variable to the scope of the function so its not undeifned (python = gae)
    global firstCoords
    global lastCoords  # read above
    if (firstCoords == [-1, -1]):  # if first coordinates are -1,-1 aka not set yet then
        if (len(simps) > 0):
            # if one of the places our ship is going to be is blue then overlap error
            if (yourGrid[x][y].cget("bg") == "blue"):
                mb.showerror(
                    "Error", "You can't do this your ships would be overlapping")
                overlap = True
            firstCoords = [x, y]  # set first coordiantes
            # set coordinate blue to indicate start of simp/ship selection
            yourGrid[x][y].configure(bg="blue")
    elif (lastCoords == [-1, -1]):  # if last coordinates are 0,0 aka not set yet then
        # if its on the same x coordinate aka in a straight line on the x axis then
        if (firstCoords[0] == x):
            # set last coordinates for end of the ship/simp
            lastCoords = [x, y]
            # if firstpoint - secondpoint is positive then (firstpoint - secondpoint = distance between 2 points) the reason we check y is beacuse x is the same so no point
            # lastcoord is above firstcoord in y axis
            if (firstCoords[1] - lastCoords[1] > 0):

                for i in range(len(simps)):  # for each simp
                    # if the distance between the 2 is less than 5 its a valid ship
                    if (firstCoords[1] - lastCoords[1] < 5):
                        # if the distance +1 aka the length of the selected coords is the same as the current simp
                        if (firstCoords[1] - lastCoords[1] + 1 == simps[i]):
                            overlap = False  # set overlap to false every check
                            # copy the array into a new array so u now are able to edit it without affecting the other array
                            lastCoordsCheck = lastCoords.copy()
                            # loop until all the coords between the 2 selected first and last coords have been checked to see if they're coloured blue
                            while lastCoordsCheck != firstCoords and lastCoordsCheck[1] < 10 and lastCoordsCheck[1] > -1:
                                lastCoordsCheck[1] += 1
                                # if one of the places our ship is going to be is blue then overlap error
                                if (yourGrid[x][lastCoordsCheck[1]].cget("bg") == "blue"):
                                    mb.showerror(
                                        "Error", "You can't do this your ships would be overlapping")
                                    overlap = True
                            if (overlap == True):
                                break
                            # remove the simp that is the same size as the ship size selected
                            simps.remove(firstCoords[1] - lastCoords[1] + 1)
                            # colour the lastcoord selected
                            yourGrid[x][y].configure(bg="blue")
                            while lastCoords != firstCoords:  # loop until all the coords between the 2 selected first and last coords have been coloured blue
                                lastCoords[1] += 1
                                yourGrid[x][lastCoords[1]].configure(
                                    bg="blue")
                            break  # stop the for loop when the simp index has been found so if its 3 we don't remove the 2 3 sized simps/ships

                        else:  # else its longer than any possible ships so undo the first coords selection
                            yourGrid[firstCoords[0]][firstCoords[1]
                                                     ].configure(bg="white")
                # reset variables
                firstCoords = [-1, -1]
                lastCoords = [-1, -1]

            # lastcoord is below firstcoords in y axis
            elif (lastCoords[1] - firstCoords[1] > 0):
                for i in range(len(simps)):
                    if (lastCoords[1] - firstCoords[1] < 5):
                        if (lastCoords[1] - firstCoords[1] + 1 == simps[i]):
                            overlap = False
                            lastCoordsCheck = lastCoords.copy()
                            while lastCoordsCheck != firstCoords and lastCoordsCheck[1] < 10 and lastCoordsCheck[1] > -1:
                                lastCoordsCheck[1] -= 1
                                if (yourGrid[x][lastCoordsCheck[1]+1].cget("bg") == "blue"):
                                    mb.showerror(
                                        "Error", "You can't do this your ships would be overlapping")
                                    overlap = True
                            if (overlap == True):
                                break
                            simps.remove(lastCoords[1] - firstCoords[1] + 1)
                            yourGrid[x][y].configure(bg="blue")
                            while lastCoords != firstCoords:
                                lastCoords[1] -= 1
                                yourGrid[x][lastCoords[1]].configure(bg="blue")
                            break
                        else:
                            yourGrid[firstCoords[0]][firstCoords[1]
                                                     ].configure(bg="white")
                firstCoords = [-1, -1]
                lastCoords = [-1, -1]

            else:  # they clicked the same square twice
                yourGrid[firstCoords[0]][firstCoords[1]
                                         ].configure(bg="white")
                firstCoords = [-1, -1]
                lastCoords = [-1, -1]

        elif (firstCoords[1] == y):

            # set last coordinates for end of the ship/simp
            lastCoords = [x, y]
            # if firstpoint - secondpoint is positive then (firstpoint - secondpoint = distance between 2 points) the reason we check y is beacuse x is the same so no point
            # lastcoord is to the left of firstcoords in x axis
            if (firstCoords[0] - lastCoords[0] > 0):

                for i in range(len(simps)):  # for each simp
                    # if the distance between the 2 is less than 5 its a valid ship
                    if (firstCoords[0] - lastCoords[0] < 5):
                        # if the distance +1 aka the length of the selected coords is the same as the current simp
                        if (firstCoords[0] - lastCoords[0] + 1 == simps[i]):
                            overlap = False  # set overlap to false every check
                            # copy the array into a new array so u now are able to edit it without affecting the other array
                            lastCoordsCheck = lastCoords.copy()
                            # loop until all the coords between the 2 selected first and last coords have been checked to see if they're coloured blue
                            while lastCoordsCheck != firstCoords and lastCoordsCheck[0] < 10 and lastCoordsCheck[0] > -1:
                                lastCoordsCheck[0] -= 1

                                # if one of the places our ship is going to be is blue then overlap error
                                if (yourGrid[lastCoordsCheck[0]+1][y].cget("bg") == "blue"):
                                    mb.showerror(
                                        "Error", "You can't do this your ships would be overlapping")
                                    overlap = True
                            if (overlap == True):
                                break
                            # remove the simp that is the same size as the ship size selected
                            simps.remove(firstCoords[0] - lastCoords[0] + 1)
                            # colour the lastcoord selected
                            yourGrid[x][y].configure(bg="blue")
                            while lastCoords != firstCoords:  # loop until all the coords between the 2 selected first and last coords have been coloured blue
                                lastCoords[0] += 1
                                yourGrid[lastCoords[0]][y].configure(
                                    bg="blue")
                            break  # stop the for loop when the simp index has been found so if its 3 we don't remove the 2 3 sized simps/ships

                        else:  # else its longer than any possible ships so undo the first coords selection
                            yourGrid[firstCoords[0]][firstCoords[1]
                                                     ].configure(bg="white")
                # reset variables
                firstCoords = [-1, -1]
                lastCoords = [-1, -1]

            # lastcoord is to the right of firstcoords in x axis
            elif (lastCoords[0] - firstCoords[0] > 0):
                for i in range(len(simps)):
                    if (lastCoords[0] - firstCoords[0] < 5):
                        if (lastCoords[0] - firstCoords[0] + 1 == simps[i]):
                            overlap = False
                            lastCoordsCheck = lastCoords.copy()
                            while lastCoordsCheck != firstCoords and lastCoordsCheck[0] < 10 and lastCoordsCheck[0] > -1:
                                lastCoordsCheck[0] += 1
                                if (yourGrid[lastCoordsCheck[0]-1][y].cget("bg") == "blue"):
                                    mb.showerror(
                                        "Error", "You can't do this your ships would be overlapping")
                                    overlap = True
                            if (overlap == True):
                                break
                            simps.remove(lastCoords[0] - firstCoords[0] + 1)
                            yourGrid[x][y].configure(bg="blue")
                            while lastCoords != firstCoords:
                                lastCoords[0] -= 1
                                yourGrid[lastCoords[0]][y].configure(bg="blue")
                            break
                        else:
                            yourGrid[firstCoords[0]][firstCoords[1]
                                                     ].configure(bg="white")
                firstCoords = [-1, -1]
                lastCoords = [-1, -1]

        else:
            mb.showerror(
                "Error", "You can't place ships diagonally you fucking monke")


yourGrid = [[Button() for a in range(10)]
            for b in range(10)]  # predefine variable array size and types
for x in range(10):  # create x axis
    for y in range(10):  # create y axis
        yourGrid[x][y] = Button(
            yourFrame, width=2, height=1, command=lambda x=x, y=y: btnPressed(x, y), bg="white")  # add buttons to array
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
