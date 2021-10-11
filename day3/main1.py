with open('input.txt') as f:
    lines=f.readlines()

trees_encountered=0         #counting total trees encountered
position_index=0            #counting correct passwords according to password policy
move_horizontal=True        #boolean to check moving direction

#Function to convert a list to string using join()
def listToString(list):
    return ''.join(str(e) for e in list)

for line in lines:
    spaces=list(line.rstrip())
    if move_horizontal == True:
        position_index+=3
        position_index%=len(spaces)
        move_horizontal = not move_horizontal
    else:
        if spaces[position_index] == ".":
            spaces[position_index]="O"
        else:
            spaces[position_index]="X"
            trees_encountered+=1
        position_index+=3
        position_index%=len(spaces)
    print("{}".format(listToString(spaces)))


exit("\n Total Trees Encountered: {}".format(trees_encountered))