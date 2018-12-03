
data = open('input1').readlines()

s = 0
freqs = []

found = False

while not found:
    for x in data:
        s += int(x)
        if s in freqs:
            print(s)
            found = True
            break
        freqs.append(s)
