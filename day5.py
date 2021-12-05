import re 

m= lambda s: re.findall(r'\d+',s)


with open('data/my_input/5.in') as f:
    lines = [  m(line.strip()) for line in f]

d=dict()
def part1(vlines):
    for _,j in enumerate(vlines):
        x,y,x_,y_=j
        x=int(x)
        x_=int(x_)
        y=int(y)
        y_=int(y_)
        if x==x_:
            if y>y_:
                y,y_=y_,y
            for jj in range(y,y_+1):
                if  (x,jj) in d:
                    d[(x,jj)]+=1
                else:
                    d[(x,jj)]=1
        elif y==y_:
            if x>x_:
                x,x_=x_,x
            for jj in range(x,x_+1):
                if  (jj,y) in d:
                    d[(jj,y)]+=1
                else:
                    d[(jj,y)]=1
    return sum([1 for k,v in d.items() if int(v)>=2])

def part2(vlines):
    d=dict()
    for _,j in enumerate(vlines):
        x,y,x_,y_=j
        x=int(x)
        x_=int(x_)
        y=int(y)
        y_=int(y_)
        if x==x_:
            if y>y_:
                y,y_=y_,y
            for jj in range(y,y_+1):
                if  (x,jj) in d:
                    d[(x,jj)]+=1
                else:
                    d[(x,jj)]=1
        elif y==y_:
            if x>x_:
                x,x_=x_,x
            for jj in range(x,x_+1):
                if  (jj,y) in d:
                    d[(jj,y)]+=1
                else:
                    d[(jj,y)]=1
        else:
            
            if  (x,y) in d:
                d[(x,y)]+=1
            else:
                d[(x,y)]=1
            while x!=x_ and y!=y_ :
                _x=(x_-x)/abs(x-x_)
                _y=(y_-y)/abs(y-y_)
                coef=int(abs((y-y_)/(x-x_)))
                x+=coef*((_x > 0) - (_x < 0))
                y+=coef*((_y > 0) - (_y < 0))
                
                if  (x,y) in d:
                    d[(x,y)]+=1
                else:
                    d[(x,y)]=1
    return sum([1 for k,v in d.items() if int(v)>=2])

print(part1(lines))
print(part2(lines))