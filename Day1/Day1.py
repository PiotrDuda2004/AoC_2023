data = open('Day1Input.txt', 'r').read().split('\n')
for line in data:
    for key in line:
        if(key.isdigit()):
            first = key
            print(first)
            
            