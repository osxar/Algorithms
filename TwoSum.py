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
print(two_sum(nums,value))