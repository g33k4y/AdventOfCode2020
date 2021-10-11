with open('input.txt') as f:
    lines=f.readlines()
lines.append("\n")

passport_data={}                                                #check Passport data
required_fields=["byr","iyr","eyr","hgt","hcl","ecl","pid"]     #store required passport fields
valid_passport_count=0                                          #count total number of valid passports
total_passports=0


for line in lines:
    line=line.rstrip()
    if len(line) != 0 :
        line=line.split(" ")
        for key_pair in line:                                   #storing passport data in a dictionary
            passport_data[key_pair[0:3]]=key_pair[4:]
    else:
        total_passports+=1
        for field in required_fields:
            if passport_data.get(field, "missing") == "missing":    #check for missing fields
                print("Field Missing in Passport {}".format(total_passports))
                break
            if field == required_fields[len(required_fields)-1]:
                valid_passport_count+=1
        passport_data.clear()


exit("\nTotal Valid Passports: {}/{}".format(valid_passport_count,total_passports))