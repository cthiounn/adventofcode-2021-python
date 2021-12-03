with open('data/my_input/3.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    n = len(vlines)
    le= len(vlines[0])
    f_str=''
    f_str2=''
    for j in range(le):
        compteur=0
        for _,jk in enumerate(vlines):
            if jk[j]=='1':
                compteur+=1
        if compteur < n/2 :
            f_str+='0'
            f_str2+='1'
        else:
            f_str+='1'
            f_str2+='0'

    print(int(f_str,2)*int(f_str2,2))

    return 0

def part2(vlines):

    l=vlines.copy()
    consideringposition=0
    while len(l)!=1:
        n = len(l)
        le= len(l[0])
        compteur=0
        for _,jk in enumerate(l):
            if jk[consideringposition]=='1':
                compteur+=1
        if compteur < n/2 :
            mostcommon='0'
        else:
            mostcommon='1'
        print(mostcommon)
        lee=[i for i in l if i[consideringposition:].startswith(mostcommon)]
        l=lee
        consideringposition+=1
    a= int(l[0],2)
    
    l=vlines.copy()
    consideringposition=0
    while len(l)!=1:
        n = len(l)
        le= len(l[0])
        compteur=0
        for _,jk in enumerate(l):
            if jk[consideringposition]=='1':
                compteur+=1
        if compteur < n/2 :
            mostcommon='1'
        else:
            mostcommon='0'
        lee=[i for i in l if i[consideringposition:].startswith(mostcommon)]
        l=lee
        consideringposition+=1
    b= int(l[0],2)
    print(a*b)


print(part1(lines))
print(part2(lines))