with open('input.txt') as f:
    lines=f.readlines()

accum=0                             #Accumulator Value
pointer=0                           #to indicate which instruction to run next

line=lines[0].strip()

while (line!="repeated"):
    statement=line.split(" ")
    lines[pointer]="repeated"
    if (statement[0] == "acc"):
        accum+=int(statement[1])
        pointer+=1
    elif (statement[0] == "jmp"):
        pointer+=int(statement[1])
    elif (statement[0] == "nop"):
        pointer+=1
    line=lines[pointer].strip()

exit("\nAccumulator Value: {}".format(accum))