with open('data/my_input/7.in') as f:
    lines = [  line.strip() for line in f]

def part1(vl):
    maxl=max([abs(int(i)) for i in  vl[0].split(',')])
 
    
    minnn=maxl*10000
    for j in range(maxl):
        mm=sum([abs(int(i)-j) for i in  vl[0].split(',')])
        if mm<=minnn:
            minnn=mm
    return minnn

def part2(vl):
    maxl=max([abs(int(i)) for i in  vl[0].split(',')])
 
    
    minnn=maxl*100000
    for j in range(maxl):
        mm=sum([(abs(int(i)-j)+1)*(abs(int(i)-j))/2 for i in  vl[0].split(',')])
        if mm<=minnn:
            minnn=mm
        
    return int(minnn)

print(part1(lines))
print(part2(lines))