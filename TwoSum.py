    
"""
Given an array of integrs nums and an integer target, return the index position of the 
two numbers such that they add up to target.

-Each input would have exactly one solution, and you may not use the same element twice.
- You can return the answer in any order.

"""


def two_sum(item,target):

    sieze = len(item)    
    true_index = 0
    
    for index in range(sieze*sieze):
        
        if((index!=0) & (index%sieze==0)):
            true_index += 1
            
        if( (item[index%sieze]+item[true_index]==target) & ((index%sieze)!=(true_index)) ):
            return index%sieze,true_index
      
     
nums = [2,7,11,15]
value = 9
# print(two_sum(nums,value))


def sumsum(array,value):
    
    sieze = len(array)-1

    if(sieze<1):
        return False

    pointer=0
    runner=1

    while(pointer<sieze):

        if(array[pointer]+array[runner]==value):
            return pointer,runner
        else:
            runner+=1

        if(runner==sieze+1 and pointer!=sieze-1):
            pointer+=1
            runner=pointer+1
        
        if(pointer==(sieze-1) and runner==sieze+1):
            break

    return False

print(sumsum(nums,value))


"""
Optimal Solution, using Hash table (i.e objects)

"""


def two_sum_optm(array,value):
    remainder={}
    seize=len(array)

    for index in (seize):
        
        if array[index] in remainder:
            return index, remainder[array[index]]
        else:
            remainder[value-array[index]]=index

print(two_sum_optm(nums,value))