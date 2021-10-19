with open('test.txt') as f:
    lines=f.readlines()

bag_colors=["shiny gold"]                                   #bags containing colors
bags_dict={}                                      #bag_colors that has been searched
bags_count=0                                                 #sum of counts

def bagsToDict(bagsList):
    bag_contains={}
    for line in bagsList:
        if "no other bags." in line:
            continue
        elif "bags." in line:
            line=line.replace(" bags.","")
        elif "bag." in line:
            line=line.replace(" bag.","")
        elif "bags" in line:
            line=line.replace(" bags","")
        else:
            line=line.replace(" bag","")
        temp=line.split(" ",1)
        bag_contains[temp[1]]=int(temp[0])
    return bag_contains

for line in lines:
    line=line.rstrip() 
    split_statement=line.split(" bags contain ")
    bags_within=split_statement[1].split(", ")
    bags_dict[split_statement[0]]=bagsToDict(bags_within)
print(bags_dict)

def bagsCount(bags_dict):
    count=0
    print(bags_dict)
    if (type(bags_dict) is dict):
        for key in bags_dict:
            if not bags_dict[key]:
                print(bags_dict)
                return int(1)
            else: 
                count= count + (int(bags_dict[key])*bagsCount(bags_dict[key]))
    else:
        return int(bags_dict)
    return count

# bags_count=bagsCount(bags_dict["shiny gold"])


# exit("\nShiny Gold bag contains a total of {} bags".format(bags_count))

#bags_color.append("shiny gold")
#for line in lines
#   break it down and save each line into a dictionery key-pair.
#   key:main_bag_color, value:another dictionary set of bag_color:numbers inside the main_bag_color
#
#   search for dictionary with key:"shiny gold"
#       for key in dictionary:
#           search again for dictionary set from each key:pair
#
#