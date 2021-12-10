#with open('data/test/10.test') as f:
with open('data/my_input/10.in') as f:
    lines = [  line.strip() for line in f]

DICTI={
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}

MATCH_DICTI={
    ")":"(",
    "]":"[",
    "}":"{",
    ">":"<"
}

def part1(v):
    count=0
    for i,j in enumerate(v):
        l=[]
        for ii,jj in enumerate(j):
            if l :
                if jj not in MATCH_DICTI.keys():
                    l.append(jj)
                elif  l[-1] not in MATCH_DICTI.keys() and l[-1]==MATCH_DICTI[jj]:
                    l.pop(-1)
                else :
                    count+=DICTI[jj]
                    break
            else:
                l.append(jj)
    return count

def reducest(st):
    stnew=st.replace("<>","").replace("()","").replace("{}","").replace("[]","")
    if st != stnew:
        return reducest(stnew)
    else:
        return st


DICTI2={
    ")":1,
    "]":2,
    "}":3,
    ">":4
}

MATCH_DICTI2={
    "(":")",
    "[":"]",
    "{":"}",
    "<":">"
}
def reversest(st):
    s=""
    for i,j in enumerate(st):
        if j in MATCH_DICTI2.keys():
            s+=MATCH_DICTI2[j]
    return s[::-1]
def countpoint(st):
    count=0
    for i,j in enumerate(st):
        count*=5
        count+=DICTI2[j]
    return count
def part2(v):    
    countlist=[]
    count=0
    discard=[]
    for i,j in enumerate(v):
        l=[]
        for ii,jj in enumerate(j):
            if l :
                if jj not in MATCH_DICTI.keys():
                    l.append(jj)
                elif  l[-1] not in MATCH_DICTI.keys() and l[-1]==MATCH_DICTI[jj]:
                    l.pop(-1)
                else :
                    discard.append(j)
                    count+=DICTI[jj]
                    break
            else:
                l.append(jj)
    
    for i,j in enumerate(v):
        if j not in discard:
            countlist.append(countpoint(reversest(reducest(j))))
    return sorted(countlist)[int(len(countlist)/2)]

print(part1(lines))
print(part2(lines))