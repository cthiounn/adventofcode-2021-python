import re
m= lambda s: re.findall(r'-?\d+',s)
from collections import Counter

with open('data/test/19.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/19.in') as f:
    lines = [  line.strip() for line in f]

def euclidian_dist(p,q):
    x,y,z=p
    xx,yy,zz=q
    return (x-xx)**2+(y-yy)**2+(z-zz)**2

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
            sli.append(list(map(int,nums)))
    list_beacons.append(sli)

    metadict=dict()
    for index,beacon in enumerate(list_beacons):
        d=dict()
        for i,j in enumerate(beacon):
            for ii,jj in enumerate(beacon):
                d[(i,ii)]=euclidian_dist(j, jj)
        metadict[index]=d

    possible_match=[]
    for k,v in metadict.items():
        for kk,vv in metadict.items():
            if k>=kk:
                continue
            set1=(set([(k,v) for k,v in Counter(v.values()).items()]))
            set2=(set([(k,v) for k,v in Counter(vv.values()).items()]))
            # print(k,kk,len(set1&set2))

            if len(set1&set2)>=66:
                possible_match.append((k,kk))
    print(possible_match)
            
    # print(metadict)
    # print(len(list_beacons))
    return 0

def part2(v):
    return 0

print("part1 test output",part1(testlines))
# print("part1 my output",part1(lines))
# print("part2 test output",part2(testlines))
# print("part2 my output",part2(lines))