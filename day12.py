with open('data/test/12.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/12.in') as f:
    lines = [  line.strip() for line in f]

def part1(v):
    d=dict()
    se=set()
    lowerse=set()
    for i,j in enumerate(v):
        a,b= j.split("-")
        d[(a,b)]=1
        se.add(a)
        se.add(b)
        if a.islower():
            lowerse.add(a)
        if b.islower():
            lowerse.add(b)
    currentnode=['start,']
    allpossibleways=set()
    while currentnode:
        cncs=currentnode.pop()
        cn=cncs.split(",")[-2]
        possiblematches=[k[0] for k in d.keys() if k[1]==cn]
        possiblematches.extend([k[1] for k in d.keys() if k[0]==cn])
        for i,j in enumerate(possiblematches):
            if j=='end':
                allpossibleways.add(cncs+j)
            elif j.islower() and j not in cncs:
                currentnode.append(cncs+j+",")
            elif j.isupper():
                currentnode.append(cncs+j+",")
    return len(allpossibleways)

def usedjoker(s,se):
    for i,j in enumerate(se):
        if s.count(j+',') >=2:
            return True
    return False
def part2(v):
    d=dict()
    se=set()
    lowerse=set()
    count=0
    for i,j in enumerate(v):
        a,b= j.split("-")
        d[(a,b)]=1
        se.add(a)
        se.add(b)
        if a.islower():
            lowerse.add(a)
            
        if b.islower():
            lowerse.add(b)
    currentnode=['start,']
    allpossibleways=set()
    visited_lower=set()
    while currentnode:
        cncs=currentnode.pop()
        cn=cncs.split(",")[-2]
        possiblematches=[k[0] for k in d.keys() if k[1]==cn]
        possiblematches.extend([k[1] for k in d.keys() if k[0]==cn])
        for i,j in enumerate(possiblematches):
            if j=='end':
                allpossibleways.add(cncs+j)
            elif j.islower() and j !='start' :
                if not usedjoker(cncs,lowerse) :
                    currentnode.append(cncs+j+",")
                elif cncs.count(j)<1:
                    currentnode.append(cncs+j+",")
            elif j.isupper():
                currentnode.append(cncs+j+",")
    return len(allpossibleways)

print("part1 test output",part1(testlines))
print("part1 my output",part1(lines))
print("part2 test output",part2(testlines))
print("part2 my output",part2(lines))