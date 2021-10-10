#main python script to run

print("Looking for two values that add up to 2020 in specified text file...\n")

#reading lines in textfile
with open('input1.txt') as f:
    lines = f.readlines()

for x in lines:
    first = int(x)
    for y in lines:
        second = int(y)
        if (first+second) == 2020:
            print("Values found!")
            print("The first number: {}".format(first))
            print("The second number: {}".format(second))
            exit("The value of first*second number: {}".format(first*second))
exit("No answer. Something is not right.")