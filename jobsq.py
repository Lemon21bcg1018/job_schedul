job=[['a',15,2],['b',10,4],['c',35,4],['d',30,1]]
m=3


def shorter(job):
    end=len(job)
    for jobs in range(0,end):
        for x in range(jobs,end):
            if (job[jobs][1])<(job[x][1]):
                temp=job[jobs]
                job[jobs]=job[x]
                job[x]=temp
            else:
                continue
    return(job)

def sche(job):
    shorter(job)
    res=['n']*m
    i=1

    for x in job:

        if x[2]>=m:
            p=m-1
        else:
            p=x[2]-1
                
        for y in range (p,-1,-1):
            if res[y] == 'n':
                res[y]=x[0]
                break
            else:
                continue

    return res

print(sche(job))

