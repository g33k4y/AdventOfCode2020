with open('input.txt') as f:
    lines=f.readlines()

#Function to convert a list to string using join()
def listToString(list):
    return ''.join(str(e) for e in list)

#Function to traverse the slope given right and down 
def countTreesEncountered(lines, right, down):
    trees_encountered=0         #counting total trees encountered
    position_index=0            #counting correct passwords according to password policy
    move_horizontal=True        #boolean to check moving direction
    down_count=1

    for line in lines:
        spaces=list(line.rstrip())
        if move_horizontal == True:
            position_index+=right
            position_index%=len(spaces)
            move_horizontal = not move_horizontal
        else:
            if down_count%down == 0:
                down_count=1
                if spaces[position_index] == ".":
                    spaces[position_index]="O"
                else:
                    spaces[position_index]="X"
                    trees_encountered+=1
            else: 
                down_count+=1
                # print("{}".format(listToString(spaces)))
                continue;
            position_index+=right
            position_index%=len(spaces)
        # print("{}".format(listToString(spaces)))
    return trees_encountered

trees=[]
total=1
trees.append(countTreesEncountered(lines,1,1))
trees.append(countTreesEncountered(lines,3,1))
trees.append(countTreesEncountered(lines,5,1))
trees.append(countTreesEncountered(lines,7,1))
trees.append(countTreesEncountered(lines,1,2))
print("Traversing Slope at right 1, down 1, total trees encountered: {}".format(trees[0]))
print("Traversing Slope at right 3, down 1, total trees encountered: {}".format(trees[1]))
print("Traversing Slope at right 5, down 1, total trees encountered: {}".format(trees[2]))
print("Traversing Slope at right 7, down 1, total trees encountered: {}".format(trees[3]))
print("Traversing Slope at right 1, down 2, total trees encountered: {}".format(trees[4]))

for trees_count in trees:
    total*=trees_count

exit("Total Trees Encountered multipled together: {}".format(total))