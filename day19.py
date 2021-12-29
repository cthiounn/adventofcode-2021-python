import re
m= lambda s: re.findall(r'-?\d+',s)
from collections import Counter
from collections import deque

with open('data/test/19.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/19.in') as f:
    lines = [  line.strip() for line in f]

ROTATIONS2={
lambda p : (p[0], p[1], p[2]),
lambda p : (p[0], -p[2], p[1]),
lambda p : (p[0], -p[1], -p[2]),
lambda p : (p[0], p[2], -p[1]),
lambda p : (-p[0], -p[1], p[2]),
lambda p : (-p[0], -p[2], -p[1]),
lambda p : (-p[0], p[1], -p[2]),
lambda p : (-p[0], p[2], p[1]),
lambda p : (p[1], p[0], -p[2]),
lambda p : (p[1], -p[0], p[2]),
lambda p : (p[1], p[2], p[0]),
lambda p : (p[1], -p[2], -p[0]),
lambda p : (-p[1], p[0], p[2]),
lambda p : (-p[1], -p[0], -p[2]),
lambda p : (-p[1], -p[2], p[0]),
lambda p : (-p[1], p[2], -p[0]),
lambda p : (p[2], p[0], p[1]),
lambda p : (p[2], -p[0], -p[1]),
lambda p : (p[2], -p[1], p[0]),
lambda p : (p[2], p[1], -p[0]),
lambda p : (-p[2], p[0], -p[1]),
lambda p : (-p[2], -p[0], p[1]),
lambda p : (-p[2], p[1], p[0]),
lambda p : (-p[2], -p[1], -p[0])
}

def man_dist(p,q):
    x,y,z=p
    xx,yy,zz=q
    return abs(x-xx)+abs(y-yy)+abs(z-zz)

def move(b,p):
    x,y,z=p
    return [ (x+xx,y+yy,z+zz) for _,(xx,yy,zz) in enumerate(b)]

def test_beacon(a,b):
    result=Counter((xx - x, yy - y, zz - z) for (x,y,z) in a for (xx,yy,zz) in b ).most_common(1)
    if result[0][1]>=12 :
        return result[0][0],move(a,result[0][0])
    return None,None
def part1(v):
    list_beacons=[]
    sli=[]
    for i,j in enumerate(v):
        nums=(m(j))
        if len(nums)==1:
            sli=[]
        elif len(nums)==0:
            list_beacons.append(sli)
        else:
            sli.append(tuple(map(int,nums)))
    list_beacons.append(sli)
    
    first=set(list_beacons[0])
    queue=deque()
    for _ , i in enumerate(list_beacons[1:]):
        queue.append(i)

    scanners=[(0,0,0)]
    while queue :
        found=False
        testbeacon=queue.popleft()
        for _, j in enumerate(ROTATIONS2):
            newbeacon= list(map(j,testbeacon))
            scannerpos, newcoordinates=test_beacon(newbeacon,first)

            if scannerpos:
                first|=set(newcoordinates)
                scanners.append(scannerpos)
                found=True
                break
        if not found:
            queue.append(testbeacon)
    return len(first) ,max([man_dist(p, q) for _,p in enumerate(scanners) for _,q in enumerate(scanners)])


print("part1 test output",part1(testlines))
print("part1 my output",part1(lines))