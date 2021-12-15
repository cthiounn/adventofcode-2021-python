import re
from collections import defaultdict

m= lambda s: re.findall(r'\d+',s)
with open('data/test/15.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/15.in') as f:
    lines = [  line.strip() for line in f]

def part1(v):
    st=""
    count=0
    d=dict()
    dd=dict()
    for i,j in enumerate(v):
        for ii,jj in enumerate(j):
            
            dd[(i,ii)]=int(jj,base=10)
            
    startpos=((0,0),0)
    endpos=(len(v)-1,len(v[0])-1)

    pointtoprocess=[]
    pointtoprocess.append(startpos)
    path=[]
    visited=set()
    while pointtoprocess:
        point=pointtoprocess.pop()
        skip=False
        x,y=point[0]
        weight=point[1]
        if point[0] in d:
            if d[point[0]]>=weight:
                d[point[0]]=weight
            else:
                skip=True
        else:
            d[point[0]]=weight
        
        if point[0]==endpos:
            path.append(weight)
         
        else:
            if not skip:
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if dx==dy==0:
                            continue
                        elif abs(dx)+abs(dy)>1:
                            continue
                        else:
                            if (x+dx,y+dy) in dd:
                                newweight=weight+dd[(x+dx,y+dy)]
                                if (x+dx,y+dy) in d and newweight<d[(x+dx,y+dy)]:
                                    pointtoprocess.append(((x+dx,y+dy),newweight))
                                    d[(x+dx,y+dy)]=newweight
                                elif (x+dx,y+dy) not in d :
                                    pointtoprocess.append(((x+dx,y+dy),newweight))
                                    d[(x+dx,y+dy)]=newweight
            
    
    return min(path)

def part2(v):
    return 0

print("part1 test output",part1(testlines))
print("part1 my output",part1(lines))
print("part2 test output",part2(testlines))
print("part2 my output",part2(lines))