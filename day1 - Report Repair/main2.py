#main python script to run

print("Looking for three values that add up to 2020 in specified text file...\n")

#reading lines in textfile
with open('input.txt') as f:
    lines = f.readlines()

for x in lines:
    first = int(x)
    for y in lines:
        second = int(y)
        for z in lines:
            third = int(z)
            if (first+second+third) == 2020:
                print("Values found!")
                print("The first number: {}".format(first))
                print("The second number: {}".format(second))
                print("The thid number: {}".format(third))
                exit("The value of first*second*third number: {}".format(first*second*third))
exit("No answer. Something is not right.")