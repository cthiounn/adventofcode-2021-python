with open('data/my_input/1.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    num_increased=0
    old=int(vlines[0])
    for _,j in enumerate(vlines[1:]):
        if int(j)>old:
            num_increased+=1
        old=int(j)
    return num_increased

def part2(vlines):
    num_increased=0
    for i in range(len(vlines)):
        if i==0 or i >=len(vlines)-2:
            continue
        if sum(map(int,vlines[i-1:i+2])) <sum(map(int,vlines[i:i+3])):
            num_increased+=1
    return num_increased

print(part1(lines))
print(part2(lines))