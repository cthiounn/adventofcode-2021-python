import re
from collections import defaultdict
from collections import Counter

m= lambda s: re.findall(r'\d+',s)
with open('data/test/14.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/14.in') as f:
    lines = [  line.strip() for line in f]

def part1(v,loop):
    st=""
    count=0
    d=dict()
    invdic=dict()
    dd=defaultdict(int)
    l=list()
    input=v[0]
    for i,j in enumerate(v[2:]):
        a,b,c = j.split()
        d[a]=c
        invdic[c]=a

    print(d)
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
    print([v for k,v in Counter(input).items()])
    return max([v for k,v in Counter(input).items()])-min([v for k,v in Counter(input).items()])

def part2(v,loop):
    return 0

print("part1 test output",part1(testlines,10))
print("part1 my output",part1(lines,10))
print("part1 test output",part2(testlines,40))
print("part1 my output",part2(lines,40))