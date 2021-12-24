with open('data/my_input/24.in') as f:
    lines = [  line.strip() for line in f]



def runprog(d,v,st):
    for i,j in enumerate(v):
        op, v1,*v2 = j.split()

        if op=="inp":
            for j in range(9,0,-1):
                d[v1]=j
                b, st2 =runprog(d.copy(),v[i+1:],st+str(j))
                if b:
                    
                    print(d,st)
                    return True,st2
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
        return True,st
    return False,st
def part1(v):
    
    d={
        'x':0,
        'y':0,
        'z':0,
        'w':0,
    }
    return runprog(d,v,"")
    # for i,j in enumerate(v):
    #     op, v1,*v2 = j.split()

    #     if op=="inp":
    #         d[v1]=1
    #         continue
    #     elif op=="mul":
    #         v2=v2[0]
    #         if v2.lstrip('-').isnumeric():
    #             d[v1]*=int(v2)
    #         else:
    #             d[v1]*=d[v2]
    #     elif op=="add":
    #         v2=v2[0]

    #         if v2.lstrip('-').isnumeric():
    #             d[v1]+=int(v2)
    #         else:
    #             d[v1]+=d[v2]
    #     elif op=="mod":
    #         v2=v2[0]
            
    #         if v2.lstrip('-').isnumeric():
    #             d[v1]%=int(v2)
    #         else:
    #             d[v1]%=d[v2]
    #     elif op=="div":
    #         v2=v2[0]

    #         if v2.lstrip('-').isnumeric():
    #             d[v1]//=int(v2)
    #         else:
    #             d[v1]//=d[v2]
    #     elif op=="eql":
    #         v2=v2[0]

    #         if v2.lstrip('-').isnumeric():
    #             d[v1]= 1 if d[v1]==int(v2) else 0
    #         else:
    #             d[v1]= 1 if d[v1]==d[v2] else 0 
    
    # if d["z"]==1:
    #     print("good")

    # return 0

def part2(v):
    return 0

print(part1(lines))
print(part2(lines))