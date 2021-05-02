
def reverseString(array):
    p1=0
    p2=len(array)-1

    while(p1<p2):
        temp = array[p1]
        array[p1],array[p2] = array[p2], array[p1]
        p1+=1
        p2-=1

    return array

print(reverseString(['s','h','u','b','h','a','m'])) 

