with open('input.txt') as f:
    lines=f.readlines()

preamble_range=25                                   #to state how many values as preamble
preambles=[]                                        #preambles listing
for i in range(0,len(lines)):
    lines[i]=int(lines[i].strip())
    if i < preamble_range:
        preambles.append(lines[i])

xmas_value=0                                        #the first xmas value without the right property

def searchProperty(list, value):
    for x in list:
        for y in list:
            if (x == y):
                continue
            elif (value == (x+y)):
                return True
    return False

for a in range(preamble_range,len(lines)):
    if (searchProperty(preambles,lines[a])):        
        preambles.pop(0)                            #if value is valid, add into preambles list
        preambles.append(lines[a])                  #and pop the first value off the list
    else:
        xmas_value=lines[a]
        print("List of preamble values: {}".format(preambles))
        exit("First XMAS Value without the right property: {}".format(xmas_value))

exit("No solution found")