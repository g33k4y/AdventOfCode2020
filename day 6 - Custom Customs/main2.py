with open('input.txt') as f:
    lines=f.readlines()
lines.append("\n")

question_list=[]
for i in range(97,123):
    question_list.append(chr(i))                #26 questions from a-z

group_yes_list=[]                               #list of questions answered yes from each member in the group (duplicative)
members_in_group=0                              #Count number of members in each group
all_yes_question_counts=0                       #count number of questions everyone answered Yes in each group
sum_counts_all_group=0                          #sum of all_yes_question_counts from all groups
group_no=1                                      #Group Number

#Function to check if everyone answered yes for a question type
#if there are 5 members in one group, there should be 5 counts in answer_list
def countChar(char, answer_list, members_in_group):
    if answer_list.count(char) == members_in_group:
        return True
    else:
        return False
    
for line in lines:
    line=line.rstrip()                          #remove "\n"
    if (line == ""):
        for char in question_list:              #for each question, check if everyone answered yes
            if (countChar(char,group_yes_list, members_in_group)):
                all_yes_question_counts+=1
        print("Total number of questions everyone answered \"Yes\" in Group {}: {}".format(group_no,all_yes_question_counts))  
        group_no+=1
        sum_counts_all_group+=all_yes_question_counts
        group_yes_list.clear()                  #reset variable for new group
        all_yes_question_counts=0
        members_in_group=0
    else:                                       #append every questions answered yes into one list for a group
        members_in_group+=1
        for char in line:
            group_yes_list.append(char)


exit("\nSum of number of questions to which everyone answered \"Yes\" from all groups: {}".format(sum_counts_all_group))