from collections import defaultdict
import re
with open('data/my_input/22.in') as f:
    lines = [  line.strip() for line in f]

def part1(v):
    d=defaultdict(int)
    for i,j in enumerate(v):
        turn=0
        if "on" in j :
            turn=1
        
        m= lambda s: re.findall(r'-?\d+',s)
        ignore=False
        xmin,xmax,ymin,ymax,zmin,zmax=list(map(int,m(j)))
        if xmin<-50 or xmax>50 or ymin<-50 or ymax>50 or zmin<-50 or zmax>50:
            ignore=True

        if not ignore:
            for k in range(xmin,xmax+1):
                for l in range(ymin,ymax+1):
                    for m in range(zmin,zmax+1):
                        if turn==1:
                            d[(k,l,m)]=turn
                        else:
                            d[(k,l,m)]=turn
                            del d[(k,l,m)]
    return sum(d.values())


def operation(l,cube,add):
    (xmin,xmax,ymin,ymax,zmin,zmax)=cube
    li=[]
    for i,j in enumerate(l):
        (xmin1,xmax1,ymin1,ymax1,zmin1,zmax1)=j
        notintersect= xmax<xmin1 or xmax1 <xmin or  ymax<ymin1 or ymax1 <ymin or zmax<zmin1 or zmax1 <zmin 
        if notintersect :
            li.append(j)
        else:
            if xmin > xmin1:
                li.append((xmin1, xmin-1, ymin1, ymax1, zmin1, zmax1))
            if xmax < xmax1:
                li.append((xmax+1, xmax1, ymin1, ymax1, zmin1, zmax1))

            if ymin > ymin1:
                li.append((max(xmin,xmin1),min(xmax,xmax1),ymin1, ymin-1, zmin1, zmax1))
            if ymax < ymax1:
                li.append((max(xmin,xmin1),min(xmax,xmax1),ymax+1, ymax1, zmin1, zmax1))

            if zmin > zmin1:
                li.append((max(xmin,xmin1),min(xmax,xmax1),max(ymin,ymin1),min(ymax,ymax1), zmin1, zmin -1 ))
            if zmax < zmax1:
                li.append((max(xmin,xmin1),min(xmax,xmax1),max(ymin,ymin1),min(ymax,ymax1), zmax+1, zmax1 ))
    if add==1:
        li.append(cube)
    return li

def part2(v):
    list_of_cubes=[]
    for i,j in enumerate(v):
        d=defaultdict(int)
        turn=0
        if "on" in j :
            turn=1
        m= lambda s: re.findall(r'-?\d+',s)
        xmin,xmax,ymin,ymax,zmin,zmax=list(map(int,m(j)))
        list_of_cubes=operation(list_of_cubes,(xmin,xmax,ymin,ymax,zmin,zmax),turn)

    count=0
    for _,cube in enumerate(list_of_cubes):
        a,b,c,d,e,f=cube
        count+= (b-a+1)*(d-c+1)*(f-e+1)

    return count
        

print(part1(lines))
print(part2(lines))