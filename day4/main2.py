import string

with open('input.txt') as f:
    lines=f.readlines()
lines.append("\n")

passport_data={}                                                #check Passport data
required_fields=["byr","iyr","eyr","hgt","hcl","ecl","pid"]     #store required passport fields
valid_passport_count=0                                          #count total number of valid passports
total_passports=0                                               #count total number of passports

#Function to check Birth Year
def byrCheck(byr):
    if int(byr) >= 1920 and int(byr) <= 2002:
        return True
    else:
        return False

#Function to check Issue Year
def iyrCheck(iyr):
    if int(iyr) >= 2010 and int(iyr) <= 2020:
        return True
    else:
        return False

#Function to check Expiration Year
def eyrCheck(eyr):
    if int(eyr) >= 2020 and int(eyr) <= 2030:
        return True
    else:
        return False

#Function to check Height
def hgtCheck(hgt):
    if (hgt[-2:] == "cm"):
        if (len(hgt) != 5 or hgt[0:3].isdigit() == False):
            return False
        elif int(hgt[0:3]) >= 150 and int(hgt[0:3]) <= 193:
            return True
        else:
            return False
    elif (hgt[-2:] == "in"):
        if (len(hgt) != 4 or hgt[0:2].isdigit() == False):
            return False
        elif int(hgt[0:2]) >= 59 and int(hgt[0:2]) <= 76:
            return True
        else:
            return False
    else:
        return False
    
#Function to check Hair Color
def hclCheck(hcl):
    if (hcl[0] != "#"):
        return False
    elif (len(hcl) != 7):
        return False
    else:
        hcl=hcl[1:]
        return isHex(hcl)

#Function to check if string is hexadecimal
def isHex(s):
    return set(s).issubset(string.hexdigits)

#Function to check Eye Color
def eclCheck(ecl):
    eye_color=["amb","blu","brn","gry","grn","hzl","oth"]
    if (len(ecl) != 3):
        return False
    else:
        for color in eye_color:
            if ecl == color:
                return True
        return False

#Function to check Passport ID
def pidCheck(pid):
    if (len(pid) != 9):
        return False
    else:
        return pid.isdigit()

for line in lines:
    line=line.rstrip()
    if len(line) != 0 :
        line=line.split(" ")
        for key_pair in line:                                       #storing passport data in a dictionary
            passport_data[key_pair[0:3]]=key_pair[4:]
    else:
        total_passports+=1
        for field in required_fields:
            if passport_data.get(field, "missing") == "missing":    #check for missing fields
                print("Field \"{}\" Missing in Passport {}".format(field, total_passports))
                break
            elif field == "byr":                                    #check for birth year validation
                if byrCheck(passport_data.get(field)) == False:
                    print("Passport {} contains invalid {}".format(total_passports,field))
                    break
            elif field == "iyr":                                    #check for issue year validation
                if iyrCheck(passport_data.get(field)) == False:
                    print("Passport {} contains invalid {}".format(total_passports,field))
                    break
            elif field == "eyr":                                    #check for expiration year validation
                if eyrCheck(passport_data.get(field)) == False:
                    print("Passport {} contains invalid {}".format(total_passports,field))
                    break
            elif field == "hgt":                                    #check for height validation
                if hgtCheck(passport_data.get(field)) == False:
                    print("Passport {} contains invalid {}".format(total_passports,field))
                    break
            elif field == "hcl":                                    #check for hair color validation
                if hclCheck(passport_data.get(field)) == False:
                    print("Passport {} contains invalid {}".format(total_passports,field))
                    break
            elif field == "ecl":                                    #check for eye color validation
                if eclCheck(passport_data.get(field)) == False:
                    print("Passport {} contains invalid {}".format(total_passports,field))
                    break
            elif field == "pid":                                    #check for passport ID validation
                if pidCheck(passport_data.get(field)) == False:
                    print("Passport {} contains invalid {}".format(total_passports,field))
                    break
            if field == required_fields[len(required_fields)-1]:
                valid_passport_count+=1
        passport_data.clear()

exit("\nTotal Valid Passports: {}/{}".format(valid_passport_count,total_passports))