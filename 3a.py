from parse import parse
data = open('input3').readlines()


class Map:
    def __init__(self):
        self.map = []
        for x in range(1000):
            self.map.append([0]*1000)
    def overlap(self, line):
        overlaps = False
        for x in range(line.x, line.x+line.w):
            for y in range(line.y, line.y+line.l):
                if self.map[x][y] > 1:
                    overlaps = True
        return overlaps

class Line:
    def __init__(self, id, x, y, w, l):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.l = int(l)
    def __repr__(self):
        return "#{} @ {},{}: {}x{}".format(self.id, self.x, self.y, self.w , self.l)

def scan(line):
    res = parse("#{} @ {},{}: {}x{}", line)
    return Line(res[0], res[1], res[2], res[3], res[4])
    # #<id> @ <x>,<y>: <W>x<L>

Lines = []

for line in data:
    Lines.append(scan(line))

m = Map()

for l in Lines:
    #print("Checking {}".format(l))
    nw = 0
    while nw < l.w:
        nh = 0
        while nh < l.l:
            #print("Setting {},{} to {} +1".format(l.x+nw, l.y+nh, m.map[l.x+nw][l.y+nh]))
            m.map[l.x+nw][l.y+nh] += 1
            nh += 1
        nw += 1


cnt = 0
for x in range(1000):
    for y in range(1000):
        if m.map[x][y] > 1:
            cnt += 1
print(cnt)


for l in Lines:
    if not m.overlap(l):
        print(l)
