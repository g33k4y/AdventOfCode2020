with open('input.txt') as f:
    lines=f.readlines()

for x in range(0, len(lines)):
    lines[x]=lines[x].strip()

accum=0                             #Accumulator Value
pointer=0                           #to indicate which instruction to run next

def checkProgram(instructions, pointer):
    global accum                    #referencing to global variable
    accum=0                         #resetting value to 0 at each function call
    instruction=instructions[0].strip()
    while (instruction!="repeated"):
        statement=instruction.split(" ")
        instructions[pointer]="repeated"
        if (statement[0] == "acc"):
            accum+=int(statement[1])
            pointer+=1
        elif (statement[0] == "jmp"):
            pointer+=int(statement[1])
        elif (statement[0] == "nop"):
            pointer+=1
        if (pointer==len(instructions)):
            return True             #if programme manages to run to the end, it works
        elif (pointer < 0 or pointer > len(instructions)):
            return False            #if pointer goes to far below or beyond the set of instructions, it fails
        instruction=instructions[pointer].strip()
    return False

for i in range(0, len(lines)):
    instruct=lines[i].strip()
    tempList=lines.copy()
    if (instruct[0:3] == "acc"):
        continue
    elif (instruct[0:3] == "nop"):
        tempList[i]=tempList[i].replace("nop","jmp")
        if (checkProgram(tempList,0)):
            exit("Correct Accumulator Value: {}".format(accum))
    elif (instruct[0:3] == "jmp"):
        tempList[i]=tempList[i].replace("jmp","nop")
        if (checkProgram(tempList,0)):
            exit("Correct Accumulator Value: {}".format(accum))

exit("Solution not found")