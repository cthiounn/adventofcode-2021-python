import re
with open('data/my_input/2.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    depth=0
    f=0
    for line in vlines:
        op, num =(line.split())
        if op =='forward':
            f+=int(num)
        elif op == 'up' :
            depth-=int(num)
        elif op == 'down' :
            depth+=int(num)
    return depth*f

def part2(vlines):
    depth=0
    f=0
    aim=0
    for line in vlines:
        op, num =(line.split())
        if op =='forward':
            f+=int(num)
            depth+=aim*int(num)
        elif op == 'up' :
            aim-=int(num)
        elif op == 'down' :
            aim+=int(num)
    return depth*f

print(part1(lines))
print(part2(lines))