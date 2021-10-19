with open('input.txt') as f:
    lines=f.readlines()

for i in range(0,len(lines)):
    lines[i]=int(lines[i].strip())

adapters=lines.copy()
adapters.append(0)
adapters.sort()
diff_one=0                                      #to count 1-jolt differences
diff_two=0                                      #to count 2-jolt differences
diff_three=1                                    #to count 3-jolt differences. device has a built-in adapter rated 3 jolts higher than highest-rated adapter
                                                


for x in range(1,len(adapters)):
    if (adapters[x]-adapters[x-1]==0):
        continue
    elif (adapters[x]-adapters[x-1]==1):
        diff_one+=1
    elif (adapters[x]-adapters[x-1]==2):
        diff_two+=1
    elif (adapters[x]-adapters[x-1]==3):
        diff_three+=1
  
        

exit("1-jolt diff * 3-jolt diff = {}".format(diff_three*diff_one))