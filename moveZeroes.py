
def moveZeroes(item):
    
    incr=0
    
    for index in range(len(item)):
        if (item[index] != 0):
            item[incr]=item[index]
            incr+=1

    for x in range(incr,len(item)):
        item[x]=0

    print(item)

moveZeroes([0,1,0,3,12,1212,121,0,99,0,2])