def dob_digit():
    dob = input("Please input your birthday in the format YYYYMMDD: ")
    tot = str(int(dob[0:4]) + int(dob[4:7]) + int(dob[7:]))
    while len(tot) > 1:
        new_tot = 0
        for i in range(len(tot)):
            new_tot += int(tot[i])
        tot = str(new_tot)
    print(int(tot))

dob_digit()
