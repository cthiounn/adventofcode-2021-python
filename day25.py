
with open('data/test/25.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/25.in') as f:
    lines = [  line.strip() for line in f]


def move(d,east=1):
    
    maxx=max([k[0] for k in d.keys()])
    minx=min([k[0] for k in d.keys()])
    maxy=max([k[1] for k in d.keys()])
    miny=min([k[1] for k in d.keys()])

    newd=dict()
    for j in range(miny,maxy+1):
        jnext=j+1
        jnext%=maxy+1
        for i in range(minx,maxx+1):
            inext=i+1
            inext%=maxx+1

            if d[(i,j)]==1 and east==1: 
                if d[(i,jnext)]==0:
                    newd[(i,j)]=0
                    newd[(i,jnext)]=d[(i,j)]
                else:
                    newd[(i,j)]=d[(i,j)]
            elif d[(i,j)]==2 and east==0:
                if d[(inext,j)]==0:
                    newd[(i,j)]=0
                    newd[(inext,j)]=d[(i,j)]
                else:
                    newd[(i,j)]=d[(i,j)]
            else:
                if (i,j) not in newd:
                    newd[(i,j)]=d[(i,j)]
    return newd

def part1(v):
    d=dict()
    for i,j in enumerate(v):
        for ii, jj in enumerate(j):
            if jj==">":
                d[(i,ii)]=1
            elif jj=="v":
                d[(i,ii)]=2
            else:
                d[(i,ii)]=0
    
    l=d.copy()
    i=0
    while True:
        old=l.copy()
        l=move(l,1)
        l=move(l,0)
        i+=1
        if old==l:
            break
    return i

print(part1(testlines))
print(part1(lines))