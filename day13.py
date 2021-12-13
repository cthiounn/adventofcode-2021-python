import re
from collections import defaultdict

m= lambda s: re.findall(r'\d+',s)
with open('data/test/13.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/13.in') as f:
    lines = [  line.strip() for line in f]

def part1(v):
    ddict=defaultdict(int)
    l=[]
    for i,j in enumerate(v):
        if len(m(j))==2:
            a,b=m(j)
            a=int(a)
            b=int(b)
            ddict[(a,b)]=1
        if len(m(j))==1:
            l.append(j)
    
    firstinstruction=l[0]
    def fold(ddict,firstinstruction):
        newddict=defaultdict(int)
        pos=int(m(firstinstruction)[0])
        if "x=" in firstinstruction:
            for i in ddict.items():
                a,_=i
                x,y=a
                if x >=pos:
                    x-=pos
                    x=pos-x
                newddict[(x,y)]=1
        elif "y=" in firstinstruction:
            for i in ddict.items():
                a,_=i
                x,y=a
                if y >=pos:
                    y-=pos
                    y=pos-y
                newddict[(x,y)]=1
        return newddict

    return len(fold(ddict,firstinstruction))

def printdic(d):
    li=(sorted([i[0] for i in d.items()]))
    for j in range(50):
        st=""
        for i in range(50):
            if (i,j) in li:
                st+='#'
            else:
                st+=' '
        print(st)


def part2(v):    
    ddict=defaultdict(int)
    l=[]
    for i,j in enumerate(v):
        if len(m(j))==2:
            a,b=m(j)
            a=int(a)
            b=int(b)
            ddict[(a,b)]=1
        if len(m(j))==1:
            l.append(j)
    
    def fold(ddict,firstinstruction):
        newddict=defaultdict(int)
        pos=int(m(firstinstruction)[0])
        if "x=" in firstinstruction:
            for i in ddict.items():
                a,_=i
                x,y=a
                if x >=pos:
                    x-=pos
                    x=pos-x
                newddict[(x,y)]=1
        elif "y=" in firstinstruction:
            for i in ddict.items():
                a,_=i
                x,y=a
                if y >=pos:
                    y-=pos
                    y=pos-y
                newddict[(x,y)]=1
    
    
        return newddict

    for _, ll in enumerate(l):
        ddict=fold(ddict,ll)
    
    printdic(ddict)
    return 0

print("part1 test output",part1(testlines))
print("part1 my output",part1(lines))
print("part2 test output",part2(testlines))
print("part2 my output",part2(lines))