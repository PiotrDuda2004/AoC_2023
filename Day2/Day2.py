data = open('Day2Input.txt', 'r').read().split('\n')
trueList = []
gameInfoList = []

for line in data:
    gameInfo = line.split(":")[0]
    
    gameInfoList.append(int(gameInfo.split(" ")[1]))
    gameInfo = int(gameInfo.split(" ")[1])
    line = line.split(":")[1]
    line = line.replace (";",",")
    line = line.split(",")
    line = [word[1:].split(" ") for word in line] #List modification completed
    trueList.append(list(set([ gameInfo for x in line if x[1]=="red" and int(x[0])>12  or  x[1]=="green" and int(x[0])>13 or x[1]=="blue" and int(x[0])>14]))) #Finding out which game is not possible 
    


trueList = [item for item in gameInfoList if item not in [item for sublist in trueList for item in sublist]] #Substrating the possible game list with not possible
print(sum(trueList))




