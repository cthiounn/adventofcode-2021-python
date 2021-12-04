
with open('data/my_input/4.in') as f:
    lines = [  line.strip() for line in f]
    bingonumber=lines[0]



def completedgrid(g):
    for i,j in enumerate(g):
        if len(''.join(j).strip())==0:
            return True
    for i in range(len(g)):
        vertical=""
        for _,j in enumerate(g):
            vertical+=j[i]
        if len(vertical.strip())==0:
            return True
    return False





grid=[]
newgrid=[]
for i,j in enumerate(lines[1:]):
    if len(j.strip())==0:
        grid.append(newgrid)
        newgrid=[]
    else:
        newgrid.append(j.split())
grid.append(newgrid)

def crossnumber(number,grid):
    for i,j in enumerate(grid):
        for k,l in enumerate(j):
            if l==number:
                grid[i][k]=""
                return 0

def sumgrid(grid):
    somme=0
    for i,j in enumerate(grid):
        for k,l in enumerate(j):
            if len(l.strip())!=0:
                somme+=int(l)
    return somme
def part1and2():
    completed=[]
    for _,number in enumerate(bingonumber.split(",")):
        for i,gr in enumerate(grid):
            crossnumber(number, gr)
            if completedgrid(gr) and gr not in completed:
                if len(completed)==0:
                    print("part1:",int(number)*sumgrid(gr))
                
                completed.append(gr)
                if len(completed)==len(grid[1:]):
                    print("part2:",int(number)*sumgrid(gr))

                
    return 0

part1and2()