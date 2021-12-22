from collections import defaultdict
import re
with open('data/my_input/22.in') as f:
    lines = [  line.strip() for line in f]

def part1(v):
    d=defaultdict(int)
    for i,j in enumerate(v):
        turn=0
        if "on" in j :
            turn=1
        
        m= lambda s: re.findall(r'-?\d+',s)
        ignore=False
        xmin,xmax,ymin,ymax,zmin,zmax=list(map(int,m(j)))
        if xmin<-50 or xmax>50 or ymin<-50 or ymax>50 or zmin<-50 or zmax>50:
            ignore=True

        if not ignore:
            for k in range(xmin,xmax+1):
                for l in range(ymin,ymax+1):
                    for m in range(zmin,zmax+1):
                        if turn==1:
                            d[(k,l,m)]=turn
                        else:
                            d[(k,l,m)]=turn
                            del d[(k,l,m)]
    return sum(d.values())

def part2(vlines):
    return 0

print(part1(lines))
print(part2(lines))