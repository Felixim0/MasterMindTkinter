from random import randint
actualNumbers=[randint(1,4),randint(1,4),randint(1,4),randint(1,4)]
while True:
    userNumbers=[]
    for i in range (4):
        userInput=input("Enter Your Guess:\n")
        userNumbers.append(userInput)
    print (' '.join(userNumbers))
    x = 0
    temp=[]
    while x < 4:
        if str(actualNumbers) == str(userNumbers):
            print("You Win")
        elif str(actualNumbers[x]) == str(userNumbers[x]):
            temp.append("*")
        elif (str(userNumbers[x]) == str(actualNumbers[0])) or (str(userNumbers[x]) == str(actualNumbers[1])) or (str(userNumbers[x]) == str(actualNumbers[2])) or (str(userNumbers[x]) == str(actualNumbers[3])):
            temp.append("/")
        else:
            temp.append(" ")
        x=x+1
    print (' '.join(temp))



            
    
