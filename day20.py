from collections import defaultdict
with open('data/my_input/20.in') as f:
    lines = [  line.strip() for line in f]


def getminmax(l):
    minx=min([i[0] for _,i in enumerate(l)])
    maxx=max([i[0] for _,i in enumerate(l)])
    miny=min([i[1] for _,i in enumerate(l)])
    maxy=max([i[1] for _,i in enumerate(l)])
    return minx,maxx,miny,maxy

def part1(v):
    firstline=v[0]
    d=defaultdict(int)
    for i,j in enumerate(firstline):
        d[i]= 1 if j=="#" else 0

    
    image=defaultdict(int)
    for i,j in enumerate(v[2:]):
        for ii,jj in enumerate(j):
            image[(i,ii)]=1 if jj=="#" else 0  

    
    
    minx,maxx,miny,maxy= getminmax(image.keys())
    
    newdict=defaultdict(int)
    for xi in range(minx-1,maxx+2):
        for yi in range(miny-1,maxy+2):
            xi1=xi-1
            xi11=xi+1
            yi1=yi-1
            yi11=yi+1
            st=str(image[(xi1,yi1)])+str(image[(xi1,yi)])+ str(image[(xi1,yi11)]) + str(image[(xi,yi1)])+str(image[(xi,yi)])+ str(image[(xi,yi11)]) + str(image[(xi11,yi1)])+str(image[(xi11,yi)])+ str(image[(xi11,yi11)])
            newdict[(xi,yi)]=d[int(st,base=2)]
    

    image=newdict
    image.default_factory = lambda: 1
    minx,maxx,miny,maxy= getminmax(image.keys())
    
    newdict=defaultdict(int)
    for xi in range(minx-1,maxx+2):
        for yi in range(miny-1,maxy+2):
            xi1=xi-1
            xi11=xi+1
            yi1=yi-1
            yi11=yi+1
            st=str(image[(xi1,yi1)])+str(image[(xi1,yi)])+ str(image[(xi1,yi11)]) + str(image[(xi,yi1)])+str(image[(xi,yi)])+ str(image[(xi,yi11)]) + str(image[(xi11,yi1)])+str(image[(xi11,yi)])+ str(image[(xi11,yi11)])
            newdict[(xi,yi)]=d[int(st,base=2)]
    
    return sum(newdict.values())

def part2(v):
    firstline=v[0]
    d=defaultdict(int)
    for i,j in enumerate(firstline):
        d[i]= 1 if j=="#" else 0

    
    image=defaultdict(int)
    for i,j in enumerate(v[2:]):
        for ii,jj in enumerate(j):
            image[(i,ii)]=1 if jj=="#" else 0  

    
    for _ in range(25):

        minx,maxx,miny,maxy= getminmax(image.keys())
        
        newdict=defaultdict(int)
        for xi in range(minx-1,maxx+2):
            for yi in range(miny-1,maxy+2):
                xi1=xi-1
                xi11=xi+1
                yi1=yi-1
                yi11=yi+1
                st=str(image[(xi1,yi1)])+str(image[(xi1,yi)])+ str(image[(xi1,yi11)]) + str(image[(xi,yi1)])+str(image[(xi,yi)])+ str(image[(xi,yi11)]) + str(image[(xi11,yi1)])+str(image[(xi11,yi)])+ str(image[(xi11,yi11)])
                newdict[(xi,yi)]=d[int(st,base=2)]
        

        image=newdict
        image.default_factory = lambda: 1
        minx,maxx,miny,maxy= getminmax(image.keys())
        
        newdict=defaultdict(int)
        for xi in range(minx-1,maxx+2):
            for yi in range(miny-1,maxy+2):
                xi1=xi-1
                xi11=xi+1
                yi1=yi-1
                yi11=yi+1
                st=str(image[(xi1,yi1)])+str(image[(xi1,yi)])+ str(image[(xi1,yi11)]) + str(image[(xi,yi1)])+str(image[(xi,yi)])+ str(image[(xi,yi11)]) + str(image[(xi11,yi1)])+str(image[(xi11,yi)])+ str(image[(xi11,yi11)])
                newdict[(xi,yi)]=d[int(st,base=2)]
        image=newdict    
    
    return sum(newdict.values())

print(part1(lines))
print(part2(lines))