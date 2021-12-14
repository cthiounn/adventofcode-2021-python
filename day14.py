import re
from collections import defaultdict
from collections import Counter

m= lambda s: re.findall(r'\d+',s)
with open('data/test/14.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/14.in') as f:
    lines = [  line.strip() for line in f]

def part1(v,loop):
    d=dict()
    l=list()
    input=v[0]
    for i,j in enumerate(v[2:]):
        a,b,c = j.split()
        d[a]=c
    for i in range(loop):
        newinput=""
        size=len(input)
        for j in range(1,size):
            pair=input[j-1]+input[j]
            if pair in d:
                newinput+=input[j-1]+d[pair]
            else:
                newinput+=input[j-1]
        newinput+=input[size-1]
        input=newinput
    return max([v for k,v in Counter(input).items()])-min([v for k,v in Counter(input).items()])

def part2(v,loop):
    d=dict()
    comptdict=defaultdict(int)
    
    input=v[0]
    for i,j in enumerate(v[2:]):
        a,b,c = j.split()
        d[a]=c

    size=len(input)
    l=list()
    for k in range(1,size):
        l.append(input[k-1]+input[k])
    for _,j in enumerate(l):
        comptdict[j]+=1

    for _ in range(loop-1):
        newcomptdict=defaultdict(int)
        for k,v in comptdict.items():
            pair1=k[0]+d[k]
            pair2=d[k]+k[1]

            newcomptdict[pair1]+=v
            newcomptdict[pair2]+=v
        comptdict=newcomptdict

    countletter=defaultdict(int)
    for k,v in comptdict.items():
        countletter[k[0]]+=v
        countletter[d[k]]+=v
    for _,j in enumerate(input):
        countletter[j]+=1
    for _,j in enumerate(input[1:-1]):
        countletter[j]-=1
    return  max([v for k,v in countletter.items()])-min([v for k,v in  countletter.items()]) 

print("part1 test output",part1(testlines,10))
print("part1 my output",part1(lines,10))
print("part1 test output",part2(testlines,40)) 
print("part1 my output",part2(lines,40)) 