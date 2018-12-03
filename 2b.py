data = open('input2b').readlines()

match_2 = []
match_3 = []
def almost(line1, line2, p=False):
    fail = 0
    for x in range(len(line1)):
        if line1[x] != line2[x]:
            fail += 1
            if p:
                print("x: {} lin: {}".format(x, line1[:x]+line1[x+1:]))

    return fail


for line in data:
    for otherline in data:
        t = almost(line, otherline)
        if t == 1:
            print("T: {} line: {}otherline: {}".format(t, line, otherline))
            almost(line, otherline, True)


