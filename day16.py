from collections import deque
import numpy as np
with open('data/test/16.test') as f:
    testlines = [  line.strip() for line in f]
with open('data/my_input/16.in') as f:
    lines = [  line.strip() for line in f]


CODE={
"0" : "0000",
"1" : "0001",
"2" : "0010",
"3" : "0011",
"4" : "0100",
"5" : "0101",
"6" : "0110",
"7" : "0111",
"8" : "1000",
"9" : "1001",
"A" : "1010",
"B" : "1011",
"C" : "1100",
"D" : "1101",
"E" : "1110",
"F" : "1111",
}



def readst(st,i=0):
    li=[]
    count=0
    while st and (i==0 or count<i):
        count+=1
        
        pv,ti,st=st[:3],st[3:6],st[6:] 
        if pv:
            pv=int(pv,base=2)
        if ti:
            ti=int(ti,base=2)
        if ti==4:
            c=True
            finalst=""
            while c:
                f,four,st=st[0],st[1:5],st[5:]
                if f=="0":
                    c=False
                finalst+=four
            finalst=int(finalst,base=2)
            li.append((pv,ti,finalst))
        else:
            f,st=st[:1],st[1:]
            if f=="0":
                l,st=st[:15],st[15:]
                if l:
                    lsize=int(l,base=2)
                    tt,st=st[:lsize],st[lsize:]
                    li.append((pv,ti,None))
                    li.extend(readst(tt))
            elif f=="1":
                l,st=st[:11],st[11:]
                if l:
                    lsize=int(l,base=2)
                    li.append((pv,ti,None))
                    readst(st,lsize)
    return li




def part1(v):
    st=""
    for i,j in enumerate(v[0]):
        st+=(CODE[j])
    print(sum([k[0] for v,k in enumerate(readst(st))] ))

def applyoperation(o,v):
    if o =="SUM":
        return sum(v)
    elif o=="PROD":
        return np.prod(v)
    elif o=="MIN":
        return min(v)
    elif o=="MAX":
        return max(v)
    elif o=="GT":
        return v[0]>=v[1]
    elif o=="LT":
        return v[0]<=v[1]
    elif o=="EQ":
        return v[0]==v[1]
    return 0

# def resolveeqgtlt(li):
#     for i,j in enumerate(li):
#         if j in {"EQ","GT","LT"} and i+2<len(li) and type(li[i+1])==int and type(li[i+2])==int:
#             if j=="GT":
#                 return li[:i] +li[i+1]>=li[i+2] +li[i+2:]
#             elif j=="LT":
#                 return li[:i] +li[i+1]<=li[i+2] +li[i+2:]
#             elif j=="EQ":
#                 return li[:i] +li[i+1]==li[i+2] +li[i+2:]
#     return li

# def resolvesumprod(li):
#     countmode=False
#     count=0
#     countmul=1
#     sum=0
#     l=[]
#     resume=0
#     for i,j in enumerate(li):
        
#         if j in {"SUM","PROD"}:
#             countmode=True
#             if j =="SUM":
#                 sum=1
#             resume=i
#         else:
#             if countmode:
#                 if type(j)==int:
#                     count+=j
#                     countmul*=j
#                 else:
#                     if sum==1:
#                         print("here")
#                         return li[:resume]+ [count]+li[i+1:]
#                     else:
#                         return li[:resume]+[countmul]+li[i+1:]
#             else:
#                 l.append(j)
#     if countmode:
#         if sum:
#             return l+ [count]
        
#         else:
#             return l+ [countmul]
#     return li


# def resolve(li):
#     while len(li)!=1:
#         li=resolvesumprod(li)
#         li=resolveeqgtlt(li)
#     return li[0]


# def evaluate(v):
#     if len(v)==1:
#         return v[1]
#     i=0
#     operation=""
#     p=[]
#     ve=[]
#     while i< len(v):
#         print(p)
#         token=v[i]
#         p.append(token)
#         if token in {"EQ","LT","GT"} and v[i+1].isnumeric() and v[i+2].isnumeric():
#             li=[]
#             li.append(v[i+1])
#             li.append(v[i+2])
#             p.append(applyoperation(token, li))
#             i+=3
#         elif type(token)==str and token not in {"EQ","LT","GT"} :
#             if len(operation)==0:
#                 operation=token
#                 onevalue=True
#                 j=i
#                 i+=1
#             elif onevalue:
#                 p=p[:j]
#                 p.append(applyoperation(operation, ve))
#                 i+=1
#             else:
#                 i+=1
#         elif type(token)==int:
#             ve.append(token)
#             i+=1
#         else:
#             i+=1

# def evaluate(v):
#     if len(v)==1:
#         return v[0]
#     li=[]
#     ve=[]
#     count=0
#     operation=""
#     for i,j in enumerate(v):
#         print("J",j)
#         if j=="SUM":
            
#             li.append(applyoperation(operation,ve))
#             applyoperation(operation,ve)
#             operation=j
#             ve=[]

#         elif j=="PROD":
            
#             li.append(applyoperation(operation,ve))
#             operation=j
#             ve=[]
#         elif j=="MIN":
#             applyoperation(operation,ve)
#             operation=j
#             ve=[]
#         elif j=="MAX":
#             applyoperation(operation,ve)
#             operation=j
#             ve=[]
#         elif j=="GT":
#             if len(ve)==2:
#                 applyoperation(operation,ve)
#                 operation=j
#                 ve=[]
#         elif j=="LT":
#             if len(ve)==2:
#                 applyoperation(operation,ve)
#                 operation=j
#                 ve=[]
#         elif j=="EQ":
#             if len(ve)==2:
#                 applyoperation(operation,ve)
#                 operation=j
#                 ve=[]
#         else:
#             ve.append(j)
    
#     li.append(applyoperation(operation,ve))
#     print(li)
#     return count

# def resolve(ve):
#     v=[]
#     a=[]
#     for i,j in enumerate(ve[::-1]):
#         print(a)
#         if type(j)==int:
#             v.append(j)
#         elif j in {"EQ","LT","GT"}:
#             aa=a.pop()
#             bb=a.pop()
#             l=[]
#             l.append(bb)
#             l.append(aa)
#             x=applyoperation(j,l )
#             a.append(x)
#             v=[]
#         else:
#             a.append(applyoperation(j,v))
#             v=[]
    # return a[0]

def resolve(ve):
    l=deque(ve)
    a=[]
    while l:
        token=l.popleft()
        if token in {"EQ","LT","GT"}:
            a.append(token)


def part2(v):
    st=""
    operation=""
    count=0
    ve=[]
    for i,j in enumerate(v[0]):
        st+=(CODE[j])
    for _, e in enumerate(readst(st)):
        a,b,c=e 
        if b==0:
            operation="SUM"
            ve.append(operation)
        elif b==1:
            operation="PROD"
            ve.append(operation)
        elif b==2:
            operation="MIN"
            ve.append(operation)
        elif b==3:
            operation="MAX"
            ve.append(operation)
        elif b==5:
            operation="GT"
            ve.append(operation)
        elif b==6:
            operation="LT"
            ve.append(operation)
        elif b==7:
            operation="EQ"
            ve.append(operation)
        elif b==4:
            ve.append(c)
    print(resolve(ve))
    return resolve(ve)

#part1(["D2FE28"])
#part1(["38006F45291200"])
#part1(["EE00D40C823060"])
# part1(["8A004A801A8002F478"])
# part1(["620080001611562C8802118E34"])
# part1(["A0016C880162017C3686B18A3D4780"])
# part1(["C0015000016115A2E0802F182340"])
part1(lines)

# part2(["C200B40A82"])
# part2(["04005AC33890"])
# part2(["880086C3E88112"])
# part2(["CE00C43D881120"])
# part2(["D8005AC2A8F0"])
# part2(["F600BC2D8F"])
# part2(["9C005AC2F8F0"])
part2(["9C0141080250320F1802104A08"])
#part2(lines)