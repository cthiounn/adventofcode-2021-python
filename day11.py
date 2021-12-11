with open('data/test/11.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/11.in') as f:
    lines = [  line.strip() for line in f]

def popall9(d):
    count=0
    while (max([v for k,v in d.items()]))>9:
        for k,v in enumerate(d.items()):
                c,value=v
                x,y=c
                if value>9:
                    count+=1
                    d[(x,y)]=0
                    for di in range(-1,2):
                        for dj in range(-1,2):
                            if di==dj==0:
                                continue
                            if (x+di,y+dj) in d and d[(x+di,y+dj)]>0:
                                d[(x+di,y+dj)]+=1
    return count

def part1(v,step):
    d=dict()
    count=0
    for i,j in enumerate(v):
        for ii,jj in enumerate(j):
            d[(i,ii)]=int(jj)
    for i in range(step):
        for k,v in enumerate(d.items()):
            c,value=v
            newvalue=value+1
            x,y=c
            d[(x,y)]=newvalue
        count+=popall9(d)
    return count

def part2(v):
    d=dict()
    count=0
    for i,j in enumerate(v):
        for ii,jj in enumerate(j):
            d[(i,ii)]=int(jj)
    step = 0

    while max([v for k,v in d.items()])!=0:
        step+=1
        for k,v in enumerate(d.items()):
            c,value=v
            newvalue=value+1
            x,y=c
            d[(x,y)]=newvalue
        count+=popall9(d)
    return step

print("part1 test output",part1(testlines,100))
print("part1 my output",part1(lines,100))
print("part2 test output",part2(testlines))
print("part2 my output",part2(lines))