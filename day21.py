from collections import defaultdict
import re
m= lambda s: re.findall(r'\d+',s)
with open('data/test/21.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/21.in') as f:
    lines = [  line.strip() for line in f]

def roll_dice(pos,dice,num_dice):
    dice+=1
    num_dice+=1
    if dice > 100:
        dice=1
    pos+=dice

    return pos,dice,num_dice

    

def part1(v):
    pos_j1=int(m(v[0])[1])
    pos_j2=int(m(v[1])[1])
    dice=0
    num_dice=0
    d=defaultdict(int)
    dpos=dict()
    dpos[1]=pos_j1
    dpos[0]=pos_j2
    j1=1
    i=0
    while True :
        i+=1
        for _ in range(3):
            dpos[j1],dice,num_dice=roll_dice(dpos[j1],dice,num_dice)
            dpos[j1]%=10
            if dpos[j1]==0:
                dpos[j1]=10
        d[j1]+=dpos[j1]
        if d[j1]>=1000:
            print(d,num_dice)
            return d[(j1+1)%2]*num_dice
        j1+=1
        j1%=2
    return 0

def part2(v):
    return 0

print("part1 test output",part1(testlines))
print("part1 my output",part1(lines))
# print("part2 test output",part2(testlines))
# print("part2 my output",part2(lines))