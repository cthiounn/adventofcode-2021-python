#with open('data/my_input/9.in') as f:
with open('data/test/9.test') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    d=dict()
    for i,j in enumerate(vlines):
        for ii,jj in enumerate(j):
            d[(i,ii)]=int(jj)
    count=0
    for k,v in d.items():
        i,j = k
        min=1
        if (i+1,j) in d and d[(i+1,j)]<=v:
            min=0
        if (i-1,j) in d and d[(i-1,j)]<=v:
            min=0
        if (i,j+1) in d and d[(i,j+1)]<=v:
            min=0
        if (i,j-1) in d and d[(i,j-1)]<=v:
            min=0
        if min:
            count+=1 +v
    return count

def crawl_and_count(jj,d):
    bassin_visited=set()
    bassin_to_crawl=[]
    bassin_to_crawl.append(jj)
    while bassin_to_crawl:
        p=bassin_to_crawl.pop()
        i,j=p
        bassin_visited.append(p)
        if (i+1,j)  in d and d[(i+1,j)]!=9 and (i+1,j) not in bassin_visited:
            bassin_to_crawl.append((i+1,j))
        if (i-1,j)  in d and d[(i-1,j)]!=9 and (i-1,j) not in bassin_visited:
            bassin_to_crawl.append((i-1,j))
        if (i,j+1)  in d and d[(i,j+1)]!=9 and (i,j+1) not in bassin_visited:
            bassin_to_crawl.append((i,j+1))
        if (i,j-1)  in d and d[(i,j-1)]!=9 and (i,j-1) not in bassin_visited:
            bassin_to_crawl.append((i,j-1))
    print(bassin_visited)
    return len(bassin_visited)
def part2(vlines):
    d=dict()
    for i,j in enumerate(vlines):
        for ii,jj in enumerate(j):
            d[(i,ii)]=int(jj)
    count=1
    lowest_points=list()
    for k,v in d.items():
        i,j = k
        min=1
        if (i+1,j) in d and d[(i+1,j)]<=v:
            min=0
        if (i-1,j) in d and d[(i-1,j)]<=v:
            min=0
        if (i,j+1) in d and d[(i,j+1)]<=v:
            min=0
        if (i,j-1) in d and d[(i,j-1)]<=v:
            min=0
        if min:
            lowest_points.append(k)
    for i,j in enumerate(lowest_points):
        print(crawl_and_count(j,d))
        count*=crawl_and_count(j,d)
    return count

print(part1(lines))
print(part2(lines))