from collections import Counter
from collections import defaultdict

with open('data/my_input/6.in') as f:
#with open('data/test/6.test') as f:

    lines = [  line.strip() for line in f]

def part1(vl,days):
    lanterns =list(map(int,vl[0].split(",")))
    for i in range(days):
        newlanterns=list()
        newlanternstoadd=0
        for j,k in enumerate(lanterns):
            if k==0:
                newlanterns.append(6)
                newlanternstoadd+=1
            else:
                newlanterns.append(k-1)
        for _ in range(newlanternstoadd):
            newlanterns.append(8)
        lanterns=newlanterns
    #print(lanterns)
    return len(lanterns)

def part2(vl,days):
    lanterns =list(map(int,vl[0].split(",")))
    d=(dict(Counter(lanterns)))
    for i in range(days):
        newdict=defaultdict()
        for e in d.items():
            k,v = e
            if k ==0:
                if 6 in newdict:
                    newdict[6]+=v
                else:
                    newdict[6]=v
                if 8 in newdict:
                    newdict[8]+=v
                else:
                    newdict[8]=v
            else:
                if k-1 in newdict:
                    newdict[k-1]+=v
                else:
                    newdict[k-1]=v
        d=newdict
    return sum([v for k,v in d.items()])

print(part1(lines,80))
print(part2(lines,256))