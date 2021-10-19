with open('input.txt') as f:
    lines = f.readlines()

total_password_count=0      #counting total passwords in the text file
correct_password_count=0    #counting correct passwords according to password policy

print("Correcting total correct password according to provided password policy...")

for line in lines:
    total_password_count+=1
    first_split=line.split(": ")                #to separate password policy from password
    second_split=first_split[0].split(" ")      #to separate password policy into password's limit and char
    third_split=second_split[0].split("-")      #to separate lower and upper limit of password char

    password=list(first_split[1].rstrip())  #store password as list
    check_char=second_split[1]              #store check_char
    lower_limit=int(third_split[0])         #store lower limit as integer
    upper_limit=int(third_split[1])         #store upper limit as integer

    same_char_count=0

    for next_char in password:
        if next_char == check_char:
            same_char_count+=1

    if same_char_count >= lower_limit and same_char_count <= upper_limit:
        correct_password_count+=1
        # print("password: {} is ok!".format(first_split[1].rstrip()))

exit("\nTotal CORRECT passwords counted: {}/{}".format(correct_password_count, total_password_count))