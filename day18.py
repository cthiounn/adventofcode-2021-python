import math
import re
from collections import defaultdict
from collections import Counter
import ast
m= lambda s: re.findall(r'-?\d+',s)


with open('data/test/18.test') as f:
	testlines = [  line.strip() for line in f]
with open('data/my_input/18.in') as f:
    lines = [  line.strip() for line in f]

def traduct(st):
    depth=0
    a=[]
    for i,j in enumerate(st):
        if j =='[':
            depth+=1
        elif j==']':
            depth-=1
        elif j==",":
            continue
        else:
            a.append((depth,int(j)))
    return (a)

# def revtraduct(a):
#     st=""
#     depth=0
#     for i,j in enumerate(a):
#         d,n=j
#         while depth!=d:
#             if depth<d:
#                 depth+=1
#                 st+="["
#             elif depth>d:
#                 depth-=1
#                 st+="]"
#                 if depth==d:
#                     st+="],["
#         st+=str(n)
#         if i!=len(a)-1:
#             st+=','
        
        
#     while depth!=0:
#         st+=']'
#         depth-=1
#     st=st.replace(',,',',')
#     st=(re.sub(",(]+)",r"\1,",st))
#     st=(re.sub("(\d+),(\d+),(\d+),(\d+)",r"\1,\2],[\3,\4",st))
    
#     st=st.replace(',,',',')
    
#     st=(re.sub("(\d+),(\d+),(\d+),(\d+)",r"\1,\2],[\3,\4",st))
#     return st


def explodest(st):
    print(st)
    a=traduct(st)
    print(a)
    return explode(a)

# def rev(a):
#     d=0
#     st=""
#     p,n=a[0]
#     for _ in range(p):
#         st+="["
#         d+=1
#     st+=str(n)
#     for i,j in enumerate(a[1:]):
#         dd,n=j
#         if dd==d:
#             if st[-2]==",":
#                 st+="],["


def explode(a):
    hasdistributeleft,hasdistributeright = False,False
    newli=[]
    todistribute=False
    alreadysplitonce=False
    for i,j in enumerate(a):

        depth,num=j
        if num>9 and not alreadysplitonce:
            numa=math.floor(num/2)
            numb=math.ceil(num/2)
            newli.append((depth+1,numa))
            newli.append((depth+1,numb))
            alreadysplitonce=True
        elif depth>=5:
            if not hasdistributeleft:
                if i-1>=0:
                    prec=newli.pop()
                    dprec,nprec=prec
                    nprec+=num
                    newli.append((dprec,nprec))
                    if dprec!=4:
                        newli.append((4,0))
                else:
                    newli.append((4,0))
                hasdistributeleft=True
                
            elif not hasdistributeright:
                if i+1<len(a):
                    todistribute=True
                    numtodistribute=num
                else:
                    newli.append((4,0))
                hasdistributeright=True
                
            else:

                    newli.append(j)
        
        else:
            if todistribute:
                    d,n=j
                    n+=numtodistribute
                    if d!=4:
                        newli.append((4,0))
                    newli.append((d,n))
                    todistribute=False
            else:
                newli.append(j)
    if a==newli:
        return a
    return explode(newli)

# explodest("[[[[[9,8],1],2],3],4]")
# revtraduct(explodest("[[[[[9,8],1],2],3],4]"))
# explodest("[7,[6,[5,[4,[3,2]]]]]")
# revtraduct(explodest("[7,[6,[5,[4,[3,2]]]]]"))
# explodest("[[6,[5,[4,[3,2]]]],1]")
# revtraduct(explodest("[[6,[5,[4,[3,2]]]],1]"))
# explodest("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
# print(revtraduct(explodest("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"))=="[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
# explodest("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
# explodest("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")


def resolvemagnitude(st):
    a=st
    a= a.replace("]",")")
    a= a.replace("[","(")
    a= a.replace(",","*3+2*")
    return eval(a)
#print(resolvemagnitude("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"))

def up(ll):
    l=[]
    for i,j in enumerate(ll):
        a,b=j
        l.append((a+1,b))
    return l

def calculate(a):
    l=[]
    next=False
    maxm=max([k[0] for v,k in enumerate(a)])
    for i,j in enumerate(a):
        d,n=j
        if i+1 < len(a):
            dd,nn=a[i+1]
            if d==dd==maxm:
                l.append((d-1,3*n+2*nn))
                next=True
            elif next:
                next=False
            else:
                l.append(j)
        else:
            l.append(j)
    print(l)
    if l==a:
        return a
    return calculate(l)

def magnitude(x):
  while len(x) > 1:
    print(x)
    for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(x, x[1:])):
      if depth1 != depth2: continue
      val = num1 * 3 + num2 * 2
      x = x[:i]+[( depth1-1,val)]+x[i+2:]
      break
  return x[0][0]

def part1(v):
    l=v[0]
    l=traduct(l)
    for i,j in enumerate(v[1:]):
        tj=traduct(j)
        l=up(l)
        l.extend(up(tj))
        print("B",l)
        l=explode(l)
        print("A",l)
    a=magnitude(l)
    return a

# def part1(v):
#     l=v[0]
#     for i,j in enumerate(v[1:]):
#         print(l,j)
#         l=revtraduct(explodest("["+l+","+j+"]"))
        
#     return resolvemagnitude(l)

def part2(v):
    return 0

#print("part1 test output",part1(testlines))
print("part1 my output",part1(lines))
# print("part2 test output",part2(testlines))
# print("part2 my output",part2(lines))