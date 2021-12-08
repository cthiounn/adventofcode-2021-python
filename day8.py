with open('data/my_input/8.in') as f:
    lines = [  line.strip() for line in f]

def part1(v):
    count=0
    for i,j in enumerate(v):
        for _, jj in enumerate(j.split("|")[1].split()):
            if len(jj)==2 or len(jj)==3 or len(jj)==4 or len(jj)==7 :
                count+=1
    return count

def part2(v):
    count=0
    for i,j in enumerate(v):
        mydict=dict()
        invdic=dict()
        while len(mydict)!=10:
            for _,jj in enumerate(j.replace('|','').split()):
                if len(jj)==2:
                    mydict["".join(sorted(jj))]=1
                    invdic[1]=jj
                elif len(jj)==3:
                    mydict["".join(sorted(jj))]=7
                    invdic[7]=jj
                elif len(jj)==4:
                    mydict["".join(sorted(jj))]=4
                    invdic[4]=jj
                elif len(jj)==7:
                    mydict["".join(sorted(jj))]=8
                    invdic[8]=jj
                elif len(jj)==6 :
                    if 1 in invdic and len(set(jj)&set(invdic[1]))==1 :
                        mydict["".join(sorted(jj))]=6
                        invdic[6]=jj
                    elif 3 in invdic and len(set(jj)&set(invdic[3]))==5 :
                        mydict["".join(sorted(jj))]=9
                        invdic[9]=jj
                    elif 6 in invdic and 9 in invdic:
                        mydict["".join(sorted(jj))]=0
                        invdic[0]=jj
                elif len(jj)==5:
                    if 1 in invdic and len(set(jj)&set(invdic[1]))==2:
                        mydict["".join(sorted(jj))]=3
                        invdic[3]=jj
                    elif 6 in invdic and len(set(jj)&set(invdic[6]))==5:
                        mydict["".join(sorted(jj))]=5
                        invdic[5]=jj
                    else:
                    #elif 6 in invdic and len(set(jj)&set(invdic[6]))==4:
                        mydict["".join(sorted(jj))]=2
                        invdic[2]=jj
        st=""
        for _, jj in enumerate(j.split("|")[1].split()):
            st+=str(mydict["".join(sorted(jj))])
        
        count+=int(st)
    return count

print(part1(lines))
print(part2(lines))