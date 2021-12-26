from functools import lru_cache
from functools import wraps
from collections import defaultdict
from collections import deque

import copy
with open('data/test/23.test') as f:
    testlines = [  line.strip() for line in f]

with open('data/my_input/23.in') as f:
    lines = [  line.strip() for line in f]

def test_sorted(d):
    return  d[(3,3)]==1 and d[(2,3)]==1 and d[(3,5)]==10 and d[(2,5)]==10 and d[(3,7)]==100 and d[(2,7)]==100 and d[(3,9)]==1000 and d[(2,9)]==1000

COST_MOVE={'A':1,'B':10,'C':100,'D':1000}

def reachable_places(start,d):
    reachable=set()
    queue=deque()
    queue.append(start)
    visited=set()
    while queue:
        node=queue.popleft()
        visited.add(node)
        x,y=node
        for i in range(-1,2):
            for j in range(-1,2):
                if i==j==0:
                    continue
                elif abs(i)+abs(j)>1:
                    continue
                else:
                    if (x+i,y+j) in d and d[(x+i,y+j)]==0:
                        reachable.add((x+i,y+j))
                        if (x+i,y+j) not in visited:
                            queue.append((x+i,y+j))
    return reachable

def get_frogs_from_pods(d):
    nd={k:v for k, v in d.items() if v in COST_MOVE.values() and k in SPAWN }
    if (3,3) in nd and nd[(3,3)]==1:
        if (2,3) in nd and nd[(2,3)]==1:
            del nd[(2,3)]
        del nd[(3,3)]


    if (3,5) in nd and nd[(3,5)]==10:
        if (2,5) in nd and nd[(2,5)]==10:
            del nd[(2,5)]
        del nd[(3,5)]

    if (3,7) in nd and nd[(3,7)]==100:
        if (2,7) in nd and nd[(2,7)]==100:
            del nd[(2,7)]
        del nd[(3,7)]

    if (3,9) in nd and nd[(3,9)]==1000:
        if (2,9) in nd and nd[(2,9)]==1000:
            del nd[(2,9)]
        del nd[(3,9)]


    return [(k,v) for k,v in nd.items()]

def string_representation(d):
    st=""
    minx=min([k[0] for k,v in d.items()])
    maxx=max([k[0] for k,v in d.items()])
    miny=min([k[1] for k,v in d.items()])
    maxy=max([k[1] for k,v in d.items()])
    
    for i in range(minx,maxx+1):
        for j in range(miny,maxy+1):
            if d[(i,j)]==1:
                st+='A'
            elif d[(i,j)]==10:
                st+='B'
            elif d[(i,j)]==100:
                st+='C'
            elif d[(i,j)]==1000:
                st+='D'
            elif d[(i,j)]==-1:
                st+='#'
            elif d[(i,j)]==0:
                st+='.'
        # st+='\n'
    # print("----")
    # print(st)
    return st

def read_dict(v):
    d=dict()
    for i,j in enumerate(v):
        for ii,jj in enumerate(j):
            if jj=="#":
                d[(i,ii)]=-1
            elif jj==".":
                d[(i,ii)]=0
            else:
                d[(i,ii)]=COST_MOVE[jj]
    return d



def move(d,c,m):

    li=[]
    
    frogs_can_return=getfroghome(d)
    frogs_from_pods=get_frogs_from_pods(d)
    # if a frog can return home, do it
    if frogs_can_return:
        dd=d.copy()
        li.append(movefroghome(dd,frogs_can_return,c,m))
    # else move a frog from a pod elsewhere
    else:
        for _, frog in enumerate(frogs_from_pods):
            #move outside
            (x,y),v=frog
            for _,(xt,yt) in enumerate(reachable_places((x,y), d)):
                if (xt,yt) in SPAWN:
                    continue
                else:
                    dd=d.copy()
                    dd[(xt,yt)]=v
                    dd[(x,y)]=0
                    cc=c+v*(abs(x-xt)+abs(y-yt))
                    li.append((dd,cc,m+1))
    return li




def part1(v):
    d=read_dict(v)
    cost=0
    minscore=16000
    nummovemax=20
    memo=dict()
    queue = list()
    queue.append((d,cost,0))

    while queue:
        print(len(queue))
        li=[]
        for _ , node in enumerate(queue):
            dn,cn,mn=node
            sdn=string_representation(dn)
            if test_sorted(dn):
                minscore=min(minscore,cn)
            elif sdn in memo and memo[sdn]<=cn:
                continue
            elif cn>=minscore:
                continue
            elif mn>=nummovemax:
                continue
            else:
                memo[sdn]=cn
                li.extend(move(dn,cn,mn))
        queue=[]
        for _,(dd,cc,mm) in enumerate(li):
            sdd=string_representation(dd)
            if sdd in memo and memo[sdd]<=cc:
                continue
            elif cc>=minscore:
                continue
            elif mm>=nummovemax:
                continue
            else:
                queue.append((dd,cc,mm))
        queue=sorted(queue,key=lambda x: x[1])

    return minscore

SPAWN={
    (3,3),
    (2,3),
    (3,5),
    (2,5),
    (3,7),
    (2,7),
    (3,9),
    (2,9),
    }

def getfroghome(d):
    nd={k:v for k, v in d.items() if v in COST_MOVE.values() }
    nd_outside={k:v for k, v in d.items() if v in COST_MOVE.values() if k not in SPAWN}
    
    for (x,y),v in nd_outside.items():
        list_of_reachables=reachable_places((x,y),d)
        if v==1:
            ypos=3
        elif v==10:
            ypos=5
        elif v==100:
            ypos=7
        elif v==1000:
            ypos=9
                        
        if (3,ypos) not in nd and (3,ypos) in list_of_reachables :
                return ((x,y),v)
        elif (3,ypos) in nd and nd[(3,ypos)]==v and (2,ypos) not in nd and (2,ypos) in list_of_reachables :
                return ((x,y),v)
    return None

def movefroghome(d,frog,nodecost,nummove):
    if frog is None:
        return d
    (x,y),v=frog
    list_of_reachables=reachable_places((x,y),d)
    if v==1:
        ypos=3
    elif v==10:
        ypos=5
    elif v==100:
        ypos=7
    elif v==1000:
        ypos=9
    
    nd={k:v for k, v in d.items() if v in COST_MOVE.values() }

    if (3,ypos) not in nd and (3,ypos) in list_of_reachables :
        xtarget=3        
    elif nd[(3,ypos)]==v and (2,ypos) not in nd and (2,ypos) in list_of_reachables :
        xtarget=2
    d[(x,y)]=0
    d[(xtarget,ypos)]=v
    return d , nodecost +v*(abs(x-xtarget)+abs(y-ypos)) , nummove+1


def part2(v):
    return 0

print(part1(lines))
# print(part1(testlines))
print(part2(lines))