import re
m= lambda s: re.findall(r'-?\d+',s)

with open('data/test/19.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/19.in') as f:
    lines = [  line.strip() for line in f]

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
    print(list_beacons[0])
    print(len(list_beacons))
    return 0

def part2(v):
    return 0

print("part1 test output",part1(testlines))
# print("part1 my output",part1(lines))
# print("part2 test output",part2(testlines))
# print("part2 my output",part2(lines))