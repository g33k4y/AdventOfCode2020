with open('input.txt') as f:
    lines=f.readlines()

invalid_number=14360655                             #obtained from main1.py
list=[]                                             #effective preambles list to work with
contiguous_range=[]                                 #listing of the contiguous values that sums up to invalid_number
for i in range(0,len(lines)):
    if invalid_number==int(lines[i].strip()):
        break                                       #values after the invalid number can be skipped for calculation
    list.append(int(lines[i].strip()))

weakness=0                                          #weakness=smallest+largest

def findContiguous(list, value):
    global contiguous_range
    for x in range(0,len(list)):
        contiguous_sum=list[x]
        for y in range(x+1,len(list)):
            contiguous_sum+=list[y]
            if (contiguous_sum==invalid_number):
                for i in range(x,y+1):
                    contiguous_range.append(list[i])
                return True
            elif (contiguous_sum>invalid_number):
                break
    return False

if (findContiguous(list,invalid_number)):
    contiguous_range.sort()
    weakness=contiguous_range[0]+contiguous_range[len(contiguous_range)-1]
    print("List of Contiguous Range (Sorted): {}".format(contiguous_range))
    exit("Encryption Weakness Value: {}".format(weakness))

