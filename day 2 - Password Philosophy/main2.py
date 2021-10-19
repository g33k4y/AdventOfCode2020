with open('input.txt') as f:
    lines = f.readlines()

total_password_count=0      #counting total passwords in the text file
correct_password_count=0    #counting correct passwords according to password policy

print("Correcting total correct password according to provided password policy...")

for line in lines:
    total_password_count+=1
    first_split=line.split(": ")                #to separate password policy from password
    second_split=first_split[0].split(" ")      #to separate password policy into password's position and char
    third_split=second_split[0].split("-")      #to separate 1st and 2nd position of password char

    password=list(first_split[1].rstrip())  #store password as list
    check_char=second_split[1]              #store check_char
    first_pos=int(third_split[0])           #store first position
    second_pos=int(third_split[1])          #store second position

    if password[first_pos-1] == check_char:
        if password[second_pos-1] != check_char:
            correct_password_count+=1
    else:
        if password[second_pos-1] == check_char:
            correct_password_count+=1

exit("\nTotal CORRECT passwords counted: {}/{}".format(correct_password_count, total_password_count))