import re
from collections import defaultdict
from collections import Counter

m= lambda s: re.findall(r'-?\d+',s)


with open('data/test/17.test') as f:
	testlines = [  line.strip() for line in f]
with open('data/my_input/17.in') as f:
	lines = [  line.strip() for line in f]


def shoot(v,rx,ry):
	vx,vy=v
	x=0
	y=0
	li=[]
	allypos=set()
	for _ in range(1000):
		x+=vx
		y+=vy
		allypos.add(y)
		vy-=1
		if vx>0:
		   vx-=1
		elif vx < 0 :
			vx+=1
		if x in rx and y in ry:
			li.append((x,y))
	return max(allypos),li

def part1(v):
	x1,x2,y1,y2=list(map(int,(m(v[0]))))
	rx=range(x1,x2+1)
	ry=range(y1,y2+1)
	start=(0,0)
	maxypos=list()
	
	for i in range(0,x2+1):
		for j in range(-400,400):
			maxy,l=(shoot((i,j),rx,ry))
			if l:
				maxypos.append(maxy)
	return max(maxypos),len(maxypos)

def part2(v):
	return 0

print("part1 test output",part1(testlines))
print("part1 my output",part1(lines))
print("part2 test output",part2(testlines))
print("part2 my output",part2(lines))