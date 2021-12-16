from collections import deque
from collections import defaultdict
import re


m= lambda s: re.findall(r'\d+',s)
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

def readsimple4(st):
    paquet_version=int(st[:3],base=2)
    type_id=int(st[3:6],base=2)
    rest=st[6:]
    st2=""
    for i in range(int(len(rest)/5)):
        st2+=rest[0+i*5:5+i*5][1:]
    return (paquet_version,type_id,int(st2,base=2))
def part1(v):
    st=""
    count=0
    d=dict()
    dd=defaultdict(int)
    li=[]
    for i,j in enumerate(v[0]):
        st+=(CODE[j])
    paquet_version=int(st[:3],base=2)
    type_id=int(st[3:6],base=2)
    print(paquet_version,type_id)
    if type_id!=4:
        length_type_id=st[6]
        if length_type_id=="0":
            howmuchreadbyte=int(st[7:7+15],base=2)
            rest=st[7+15:7+15+howmuchreadbyte]
            print(rest)
        elif length_type_id=="1":
            
            howmuchsubpaquet=int(st[7:7+11],base=2)
            print(howmuchsubpaquet)
            rest=(st[7+11:])
            for i in  range(howmuchsubpaquet):
                nextbyte=rest[i*11:11+i*11]
                print(readsimple4(nextbyte))

    else:
        rest=st[6:]
        st2=""
        for i in range(int(len(rest)/5)):
            st2+=rest[0+i*5:5+i*5][1:]
        print(int(st2,base=2))
        print(rest,len(rest))
    return count

def part2(v):
    return 0

print("part1 test output",part1(testlines))
#print("part1 my output",part1(lines))
print("part2 test output",part2(testlines))
print("part2 my output",part2(lines))