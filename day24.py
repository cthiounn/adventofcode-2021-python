import functools
with open('data/my_input/24.in') as f:
    lines = [  line.strip() for line in f]


@functools.lru_cache(maxsize=None)
def runprog(mp,starti):
    

    for jj in range(9,0,-1):
        d=dict()    
        d['x']=0
        d['y']=0
        d['z']=int(mp)
        d['w']=jj
        for i,j in enumerate(lines):
            if i  < starti:
                continue
            op, v1,*v2 = j.split()
            if op=="inp":
                # for jj in range(9,0,-1):
                    # d[v1]=jj
                    # st1=""
                    # st1+=str(d['x'])+"-"
                    # st1+=str(d['y'])+"-"
                    # st1+="0-0-"
                st1=str(d['z'])
                    # st1+="0"
                    #st1+=str(d['w'])

                b, st2 =runprog(st1,i+1)
                if b:
                    return True,jj+st2
                break
            elif op=="mul":
                v2=v2[0]
                if v2.lstrip('-').isnumeric():
                    d[v1]*=int(v2)
                else:
                    d[v1]*=d[v2]
            elif op=="add":
                v2=v2[0]

                if v2.lstrip('-').isnumeric():
                    d[v1]+=int(v2)
                else:
                    d[v1]+=d[v2]
            elif op=="mod":
                v2=v2[0]
                
                if v2.lstrip('-').isnumeric():
                    
                    d[v1]%=int(v2)
                    
                else:
                    d[v1]%=d[v2]
            elif op=="div":
                v2=v2[0]

                if v2.lstrip('-').isnumeric():
                    d[v1]//=int(v2)
                    
                else:
                    d[v1]//=d[v2]
            elif op=="eql":
                v2=v2[0]

                if v2.lstrip('-').isnumeric():
                    d[v1]= 1 if d[v1]==int(v2) else 0
                else:
                    d[v1]= 1 if d[v1]==d[v2] else 0 
        
        if d["z"]==1:
            return True,jj
    return False,None
def part1(v):
    return runprog("0",0)

def part2(v):
    return 0

print(part1(lines))
print(part2(lines))