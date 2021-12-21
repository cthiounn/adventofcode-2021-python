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
    while True :
        for _ in range(3):
            dpos[j1],dice,num_dice=roll_dice(dpos[j1],dice,num_dice)
            dpos[j1]%=10
            if dpos[j1]==0:
                dpos[j1]=10
        d[j1]+=dpos[j1]
        if d[j1]>=1000:
            return d[(j1+1)%2]*num_dice
        j1+=1
        j1%=2
    return 0



def part2(v):
    pos_j1=int(m(v[0])[1])
    pos_j2=int(m(v[1])[1])
    d=defaultdict(int)
    d[(pos_j1,pos_j2,0,0)]=1
    
    j1=1
    win=defaultdict(int)
    ii=0
    while d :
        newd=defaultdict(int)
        for _,key in enumerate(d.keys()):
            pos1,pos2,score1,score2=key
            for i in range(1,4):
                for j in range(1,4):
                    for l in range(1,4):
                        if j1==1:
                            newpos=i+j+l+pos1
                        else:
                            newpos=i+j+l+pos2
                        newpos%=10
                        if newpos==0:
                            newpos=10
                        if j1==1:
                            newscore=score1+newpos
                            
                            if newscore>=21:
                                win[j1]+=d[key]
                            else:
                                newd[(newpos,pos2,newscore,score2)]+=d[key]
                        else:
                            newscore=score2+newpos

                            if newscore>=21:
                                win[j1]+=d[key]
                            else:
                                newd[(pos1,newpos,score1,newscore)]+=d[key]
        d=newd
        #Change player
        j1+=1
        j1%=2
    return max(win.values())


print("part1 test output",part1(testlines))
print("part1 my output",part1(lines))
print("part2 test output",part2(testlines))
print("part2 my output",part2(lines))