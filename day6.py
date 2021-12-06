import re
m= lambda s: re.findall(r'\d+',s)


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

def part2(vl):
    return 0

print(part1(lines,256))
print(part2(lines))