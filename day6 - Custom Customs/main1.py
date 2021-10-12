with open('input.txt') as f:
    lines=f.readlines()
lines.append("\n")

yes_list=[]                                     #row variable
sum_counts=0                                    #sum of counts
group_no=1                                      #Group Number

def findChar(char, question_string):
    if question_string.find(char) != -1:
        return False
    else:
        return True
    
for line in lines:
    line=line.rstrip()                          #remove "\n"
    for char in line:
        if (findChar(char,str(yes_list))):      #search for char in yes_list
            yes_list.append(char)
    if (line == ""):
        print("Total \"Yes\" in Group {}: {}".format(group_no,len(yes_list)))    
        group_no+=1                     
        sum_counts+=len(yes_list)
        yes_list.clear()

exit("\nSum of total counts from all groups: {}".format(sum_counts))