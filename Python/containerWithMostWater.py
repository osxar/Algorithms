
def containerWithMostWater(array):
    
    sieze = len(array)-1

    if(sieze<1):
        return False

    waterCalculation = {}
    pointer=0
    runner=1

    while(pointer<sieze):

        length = min(array[pointer],array[runner])
        width = abs(pointer-runner)

        waterCalculation[length*width]= [pointer,runner]

        runner+=1

        if(runner==sieze+1 and pointer!=sieze-1):
            pointer+=1
            runner=pointer+1
        
        if(pointer==(sieze-1) and runner==sieze+1):
            break

    maxVolume=0
    
    for key in waterCalculation:
        if(int(key)>maxVolume):
            maxVolume=int(key)
    
    return waterCalculation[maxVolume]


array = [1,8,6,2,9,4]
array2 = [7,1,2,3,9]
print(containerWithMostWater(array2))