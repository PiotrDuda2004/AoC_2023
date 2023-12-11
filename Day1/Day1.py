data = open('Day1Input.txt', 'r').read().split('\n')
sum = 0
for line in data:
    for key in line:
        if(key.isdigit()):
            first = key # Get first digit character
            break
    line = line[::-1] #reverse the whole string that we're working on
    for key in line:
        if(key.isdigit()):
                second = key #Get second digit character
                break
    sum +=int(first+second) 
print(sum)
