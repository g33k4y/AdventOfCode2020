with open('input.txt') as f:
    lines=f.readlines()

row=0                   #row variable
column=0                #column variable
seatList=[]             #seat ID Listing

def findSeat(line, lower, upper):
    for char in line:
        if (char == "F" or char =="L"):
            upper=int((lower+upper-1)/2)
            if (len(line) == 1):
                return lower
            else:
                return findSeat(line[1:], lower, upper)
        else:
            lower=int((lower+upper+1)/2)
            if (len(line) == 1):
                return upper
            else:
                return findSeat(line[1:], lower, upper)

for line in lines:
    row=findSeat(line[0:7],0,127)
    column=findSeat(line[7:],0,7)
    seatList.append(int(row*8+column))

seatList.sort()
print("Searching for my seat...")
for i in range(1,len(seatList)-1):
    if (seatList[i]-seatList[i-1] == 2):
        exit("My Seat ID: {}".format(seatList[i]-1))
exit("My Seat ID is not found")