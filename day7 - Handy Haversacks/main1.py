with open('input.txt') as f:
    lines=f.readlines()

bag_colors=["shiny gold"]                                   #bags containing colors
bag_colors_searched=[]                                      #bag_colors that has been searched
bag_count=0                                                 #sum of counts

while (len(bag_colors) != 0):
    print("searching bags for {} bags...".format(bag_colors[0]))
    for line in lines:
        line=line.rstrip()  
        if line.startswith(bag_colors[0]):                  #skip if the line begins with the color currently searching
            continue
        elif (line.find(bag_colors[0])) != -1:              #count it if the rest of the line contains the color
            split_statement=line.split(" bags contain ")
            #prevent double counting using the if statement below
            if (bag_colors_searched.count(split_statement[0])) != 0 or (bag_colors.count(split_statement[0]) != 0):
                print("{} bags contain {} bags but color has already been counted".format(split_statement[0],bag_colors[0]))
                continue
            else:
                bag_colors.append(split_statement[0])
                print("{} bags contain {} bags".format(split_statement[0],bag_colors[0]))
                bag_count+=1
    bag_colors_searched.append(bag_colors[0])               #keep note of colors that's been searched
    bag_colors.pop(0)

exit("\nBags containing Shiny Gold bags: {}".format(bag_count))