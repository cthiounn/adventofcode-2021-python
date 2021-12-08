from collections import Counter
import re
from collections import defaultdict

m= lambda s: re.findall(r'\d+',s)

LAMBDA={
    "acedgfb": 8,
"cdfbe": 5,
"gcdfa": 2,
"fbcad": 3,
"dab": 7,
"cefabd": 9,
"cdfgeb": 6,
"eafb": 4,
"cagedb": 0,
"ab": 1,
"cdfeb": 5,
"fcadb": 3,
"cdfeb": 5,
"cdbaf": 3
}
LAMDA2=dict()
for i,j in enumerate(LAMBDA.items()):
    LAMDA2["".join(sorted(j[0]))]=j[1]
with open('data/test/8.test') as f:
#with open('data/my_input/8.in') as f:
    lines = [  line.strip() for line in f]

def part1(v):
    count=0
    for i,j in enumerate(v):
        for _, jj in enumerate(j.split("|")[1].split()):
            if len(jj)==2 or len(jj)==3 or len(jj)==4 or len(jj)==7 :
                count+=1
    return count

def part2(v):
    count=0
    for i,j in enumerate(v):
        mydict=dict()
        for _,jj in enumerate(j.replace('|','').split()):
            if len(jj)==2:
                mydict["".join(sorted(jj))]=1
            elif len(jj)==3:
                mydict["".join(sorted(jj))]=7
            elif len(jj)==4:
                mydict["".join(sorted(jj))]=4
            elif len(jj)==7:
                mydict["".join(sorted(jj))]=8
            print(mydict)
    return count

print(part1(lines))
print(part2(lines))