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

# def readsimple4(st):
#     paquet_version=int(st[:3],base=2)
#     type_id=int(st[3:6],base=2)
#     rest=st[6:]
#     st2=""
#     for i in range(int(len(rest)/5)):
#         st2+=rest[0+i*5:5+i*5][1:]
#     return (paquet_version,type_id,int(st2,base=2))

def readsimple4(st):
    li=list()
    while st:
        paquet_version,st=st[:3],st[3:]
        type_id,st=st[:3],st[3:]
        paquet_version=int(paquet_version,base=2)
        type_id=int(type_id,base=2)
        c=True
        finalst=""
        while c:
            f,four,st=st[0],st[1:5],st[5:]
            if f=="0":
                c=False
            finalst+=four
        li.append((paquet_version,type_id,int(finalst,base=2)))
    return li

def readsimple44(st,num):
    li=list()
    i=0
    while i<num:
        i+=1
        paquet_version,st=st[:3],st[3:]
        type_id,st=st[:3],st[3:]
        paquet_version=int(paquet_version,base=2)
        type_id=int(type_id,base=2)
        c=True
        finalst=""
        while c:
            f,four,st=st[0],st[1:5],st[5:]
            if f=="0":
                c=False
            finalst+=four
        li.append((paquet_version,type_id,int(finalst,base=2)))
    return li

def part1(v):
    st=""
    count=0
    for i,j in enumerate(v[0]):
        st+=(CODE[j])
    
    paquet_version,st=st[:3],st[3:]
    type_id,st=st[:3],st[3:]
    paquet_version=int(paquet_version,base=2)
    type_id=int(type_id,base=2)
    count+=paquet_version
    if type_id!=4:
        f,st=st[0],st[1:]
        if f=="0":
            l,st=st[:15],st[15:]
            
            lsize=(int(l,base=2))
            st=st[:lsize]
            li=readsimple4(st)
            count+=sum([k[0] for v,k in enumerate(li)])
            print(li)
        elif f=="1":
            l,st=st[:11],st[11:]
            lsize=(int(l,base=2))
            li=readsimple44(st,lsize)
            count+=sum([k[0] for v,k in enumerate(li)])
            print(li)

    else:
        c=True
        finalst=""
        while c:
            f,four,st=st[0],st[1:5],st[5:]
            if f=="0":
                c=False
            finalst+=four
        print(int(finalst,base=2))
    
    
    return count

def part2(v):
    return 0

print("part1 test output",part1(testlines))
print("part1 my output",part1(lines))
print("part2 test output",part2(testlines))
print("part2 my output",part2(lines))