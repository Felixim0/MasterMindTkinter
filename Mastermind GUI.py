from tkinter import *
from time import sleep
import random
from random import randint
import sys
import os
root=Tk()
colours=["red","white","blue","green","yellow","black"]
backgroundImage = PhotoImage(file="./environment/background.gif")
backgroundLabel = Label (root, image=backgroundImage)
backgroundLabel.grid(row=0,column=0,columnspan=8)
actualNumbers=[randint(0,5),randint(0,5),randint(0,5),randint(0,5)]
#actualNumbers=[0,0,1,5]
global submitRow, buttonsRow,win, actualColours
actualColours=[]
win=False
buttonsRow = 1
submitRow = 1

print("""
Black is right colour right place
White is right colour wrong place""")

for x in range (0,4):
    if actualNumbers[x] == 0:
        actualColours.append(colours[0])
    elif actualNumbers[x] == 1:
        actualColours.append(colours[1])
    elif actualNumbers[x] == 2:
        actualColours.append(colours[2])    
    elif actualNumbers[x] == 3:
        actualColours.append(colours[3])
    elif actualNumbers[x] == 4:
        actualColours.append(colours[4])
    elif actualNumbers[x] == 5:
        actualColours.append(colours[5])
        
print(str(actualColours) + "\n")

def giveClues(row,white,black):
    root.label = []
    i = 0
    q = 0
    whiteImage = PhotoImage(file="./environment/whiteReturn.gif")
    blackImage = PhotoImage(file="./environment/blackReturn.gif")
    for w in range (0,white):
        root.label.append(Label(root, text="White", image=whiteImage))
        root.label[i].grid(column=i, row=row-1)
        
        i = i + 1
    for b in range (0,black):
        root.label.append(Label(root, text="Black", image=blackImage))
        root.label[i].grid(column=i, row=row-1)
        
        i = i + 1
    whiteImage.image = whiteImage
    blackImage.image = blackImage


def userChosenColours():
    temp = []
    for i in range (0,4):
        temp.append(root.button[i].cget('bg'))
    return (temp)

def computerChosenColours():
    global actualColours
    a = actualColours[:]
    return (a)

def returnCounters(buttonsRow):
    global win, blackCounter,whiteCounter,actualColours
    
    blackCounter = 0
    whiteCounter = 0

    tempArrayOfActualColours = (computerChosenColours())
    totalArrayOfUserInputs = (userChosenColours())

    if totalArrayOfUserInputs == tempArrayOfActualColours:
        print("You Win")
        win=True

    if win==False:
        for i in range (0,4):
            if totalArrayOfUserInputs[i] == tempArrayOfActualColours[i]:
                blackCounter=blackCounter+1
                totalArrayOfUserInputs[i] = "noCompare"
                tempArrayOfActualColours[i] = "noCompare"

        for i in range(0,4):
            if (totalArrayOfUserInputs[i] in tempArrayOfActualColours) and (totalArrayOfUserInputs[i] != "noCompare"):
                whiteCounter=whiteCounter+1
                totalArrayOfUserInputs[i] = "noCompare"
                tempArrayOfActualColours[i] = "noCompare"                
#
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def submit():
    global submitRow, buttonsRow, whiteCounter, blackCounter
    submitRow=submitRow+1
    
    returnCounters(buttonsRow)
    if win == False:
        giveClues(submitRow, whiteCounter, blackCounter)
        submitButton.grid(column=0,row=submitRow)
        makeButtons(buttonsRow)
    elif win == True:
        giveClues(submitRow, whiteCounter, blackCounter)
        submitButton.grid(column=0,row=submitRow)
        submitButton.configure(text = "Play Again",command=restart_program)

def color_change(i,button):

    currentColour = (root.button[i].cget('bg'))
    if currentColour == colours[0]:
       c = 1
    elif currentColour == colours[1]:
        c = 2
    elif currentColour == colours[2]:
        c = 3
    elif currentColour == colours[3]:
        c = 4
    elif currentColour == colours[4]:
        c = 5
    elif currentColour == colours[5]:
        c = 0
    root.button[i].configure(bg = colours[c])

submitButton = Button(root,text="Submit",command=submit)
submitButton.grid(column=0,row=submitRow,columnspan=4)
    
def makeButtons(row):
    global buttonsRow
    buttonsRow = buttonsRow + 1
    root.button = []
    for i in range(0,4):
        root.button.append(Button(root,bg="red", text="     ",command=lambda i=i:color_change(i,"0")))
        root.button[i].grid(column=i+4, row=row)

makeButtons(buttonsRow)
root.title("Master Mind")
root.mainloop()




            
    
