data = open('input2').readlines()

match_2 = []
match_3 = []


def check():
    r1 = 0
    r2 = 0
    for line in data:
        tmp1,tmp2 = checkline(line)
        r1 += tmp1
        r2 += tmp2
    print("r1: {} r2: {} sum: {}".format(r1,r2, r1*r2))

def checkline(line):
    rval1 = 0
    rval2 = 0
    for letter in line:
        cnt = 0
        for test in line:
            if letter == test:
                cnt+=1
        if cnt == 2:
            print(letter)
            rval1 = 1
        if cnt == 3:
            print(letter)
            rval2 = 1
    print(line)
    return (rval1, rval2)

check()
