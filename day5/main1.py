with open('input.txt') as f:
    lines=f.readlines()

row=0                   #row variable
column=0                #column variable
highest_seat_ID=0       #highest seat ID

def findSeat(line, lower, upper):
    for char in line:
        if (char == "F" or char =="L"):
            upper=int((lower+upper-1)/2)
            if (len(line) == 1):        #end of list, return value
                return lower
            else:
                return findSeat(line[1:], lower, upper)
        else:
            lower=int((lower+upper+1)/2)
            if (len(line) == 1):        #end of list, return value
                return upper
            else:
                return findSeat(line[1:], lower, upper)
    
    
for line in lines:
    row=findSeat(line[0:7],0,127)
    column=findSeat(line[7:],0,7)
    seat_ID=row*8+column
    print("row: {}, column: {}, Seat ID: {}".format(row, column, seat_ID))
    if (seat_ID>highest_seat_ID) : highest_seat_ID=seat_ID

exit("\nHighest Seat ID: {}".format(highest_seat_ID))