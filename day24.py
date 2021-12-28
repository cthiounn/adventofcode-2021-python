from collections import deque
import functools
with open('data/my_input/24.in') as f:
    lines = [  line.strip() for line in f]


@functools.lru_cache(maxsize=None)
def runprog(mp,starti):
    for jj in range(9,0,-1):
        d=dict()    
        d['x']=0
        d['y']=0
        d['z']=mp
        d['w']=jj
        for i,j in enumerate(lines[starti:]):
            op, v1,*v2 = j.split()
            if op=="inp":
                b, st2 =runprog(d['z'],starti+i+1)
                if b:
                    return True,str(jj)+st2
                break
            else:
                v2=v2[0]
                if v2.lstrip('-').isnumeric():
                    value=int(v2)
                else:
                    value=d[v2]
            
                if op=="mul":
                    d[v1]*=value
                elif op=="add":
                    d[v1]+=value
                elif op=="mod":        
                    d[v1]%=value
                elif op=="div":
                    d[v1]//=value
                elif op=="eql":
                    d[v1]= 1 if d[v1]==value else 0
        
        if d["z"]==0:
            return True,str(jj)
    return False,None
def part1(v):
    return runprog(0,1)


@functools.lru_cache(maxsize=None)
def runprog2(mp,starti):
    for jj in range(1,10):
        d=dict()    
        d['x']=0
        d['y']=0
        d['z']=mp
        d['w']=jj
        has_break=False
        for i,j in enumerate(lines[starti:]):
            op, v1,*v2 = j.split()
            if op=="inp":
                b, st2 =runprog2(d['z'],starti+i+1)
                
                if b:
                    return True,str(jj)+st2
                has_break=True
                break
            else:
                v2=v2[0]
                if v2.lstrip('-').isnumeric():
                    value=int(v2)
                else:
                    value=d[v2]
            
                if op=="mul":
                    d[v1]*=value
                elif op=="add":
                    d[v1]+=value
                elif op=="mod":        
                    d[v1]%=value
                elif op=="div":
                    d[v1]//=value
                elif op=="eql":
                    d[v1]= 1 if d[v1]==value else 0
        
        if d["z"]==0 and not has_break:
            return True,str(jj)
    return False,None
def part2(v):
    return runprog2(0,1)


def test(v,num):
    queue=deque()
    for i,j in enumerate(num):
        queue.append(j)
    d=dict()    
    d['x']=0
    d['y']=0
    d['z']=0
    d['w']=0
    for i,j in enumerate(v):
        print(d)
        op, v1,*v2 = j.split()
        if op=="inp":
            d['w']=int(queue.popleft())
        else:
            v2=v2[0]
            if v2.lstrip('-').isnumeric():
                value=int(v2)
            else:
                value=d[v2]
        
            if op=="mul":
                d[v1]*=value
            elif op=="add":
                d[v1]+=value
            elif op=="mod":        
                d[v1]%=value
            elif op=="div":
                d[v1]//=value
            elif op=="eql":
                d[v1]= 1 if d[v1]==value else 0
    print(d['z'])

# test(lines,"51131616112781")

# test(lines,"52793949489991")
# print(part1(lines))
print(part2(lines))