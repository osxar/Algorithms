def validMountainArray(self, A):
        """
        :type arr: List[int]
        :rtype: bool
        """
        size=len(A)
        cnt=1
        
        if(size<3):
            return False
        for num in range(1,size):
            if(A[num]>A[num-1]):
                cnt +=1
            else:
                break
                
        if(cnt==size):
            return False
        
        for num in range(cnt,size):
            if(A[num]<A[num-1] and cnt>1):
                cnt+=1
            else:
                break
        
        if(cnt == size):
            return True
        else:
            return False