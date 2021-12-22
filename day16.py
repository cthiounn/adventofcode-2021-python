import math
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
    print(o,v)
    if o =="SUM":
        return sum(v)
    elif o=="PROD":
        return math.prod(v)
    elif o=="MIN":
        return min(v)
    elif o=="MAX":
        return max(v)
    elif o=="GT":
        return 1 if v[0]>v[1] else 0
    elif o=="LT":
        return 1 if v[0]<v[1] else 0
    elif o=="EQ":
        return 1 if v[0]==v[1] else 0
    return 0



def parse(st):

    pv,ti,st=st[:3],st[3:6],st[6:] 
    if pv:
        pv=int(pv,2)
    if ti:
        ti=int(ti,2)
    if ti==4:
        c=True
        finalst=""
        while c:
            f,four,st=st[0],st[1:5],st[5:]
            if f=="0":
                c=False
            finalst+=four
        finalst=int(finalst,2)
        return finalst,st
    else:
        v=[]
        f,st=st[:1],st[1:]
        if f=="0":
            l,st=st[:15],st[15:]
            if l:
                lsize=int(l,2)
                tt,st=st[:lsize],st[lsize:]
                while tt:
                    result,tt=parse(tt)
                    v.append(result)
        elif f=="1":
            l,st=st[:11],st[11:]
            if l:
                lsize=int(l,2)
                for _ in range(lsize):
                    result,st=parse(st)
                    v.append(result)
    operation=""    
    if ti==0:
        operation="SUM"

    elif ti==1:
        operation="PROD"

    elif ti==2:
        operation="MIN"

    elif ti==3:
        operation="MAX"

    elif ti==5:
        operation="GT"

    elif ti==6:
        operation="LT"

    elif ti==7:
        operation="EQ"
    
    result=applyoperation(operation,v)
    
    return result, st

def part2(v):
    st=""
    for i,j in enumerate(v[0]):
        st+=(CODE[j])
    
    return parse(st)[0]
        





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
# print(part2(["9C0141080250320F1802104A08"]))
print(part2(lines))