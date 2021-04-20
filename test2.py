# def partitionArray(k, numbers):

#     store_unique = set()

#     for i in range(len(numbers)):

#         if(k>1):
#             for m in range(i+1, len(numbers), k-1):
#                 temp = numbers[m:m+k-1]
#                 temp.append(numbers[i])

#                 if ( (len(temp) == len(set(temp))) and (len(temp) == k ) ) :
#                     temp.sort()
#                     store_unique.add(tuple(temp))

#     return 'Yes' if len(store_unique)>=k else 'No'


def triplet(d,t):
    end=len(d)
    start=1
    count=0

    for i in range(start,end):
        for m in range(i+1,end):
            print(d[0],d[i],d[m])
            if ( (d[0] + d[i] +d[m] <= t ) and (d[i] != d[m]) ):
                count += 1

    return count


# print(triplet([1,2,3,4,5],8))


def bs(array, value):
    mid = len(array)//2
    p1 = 0
    p2 = len(array)


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'perfectTeam' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING skills as parameter.
#

def perfectTeam(skills):
    # Write your code here
    
    teams={}
    
    for i in skills:     
        teams[i]=teams.get(i,0)+1
        
    if(len(teams)!=5):
        return 0
    
    min_value = teams['p']
    
    for val in teams.values():
        
        if(val<min_value):
            min_value=val
    return min_value
    
if __name__ == '__main__':








#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'meanderingArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY unsorted as parameter.
#

def meanderingArray(unsorted):
    # Write your code here
    
    sortedArray = sorted(unsorted)
    final=[]
    p1=0
    p2=len(sortedArray)-1
    
    while(p1<=p2):
        
        if(p1==p2):
            final.append(sortedArray[p1])
            break
        final.append(sortedArray[p2])
        final.append(sortedArray[p1])
        p1+=1
        p2-=1
    
    return final
    
    

if __name__ == '__main__':






#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the triplets function below.
def triplets(t, d):

    sortArray = sorted(d)
    count=0
    
    print(sortArray)
    
    if(len(sortArray)<2):
        return 0
    
    p1max=len(sortArray)-3
    p2max=len(sortArray)-2
    p3max=len(sortArray)-1
    
    p1=0
    p2=1
    p3=2
    
    while(p1!=p1max or p2!=p2max or p3!=p3max):
        
      
        
        if(sortArray[p1]+sortArray[p2]+sortArray[p3]<=t):
            count+=1
            
        if(p3==p3max and p2==p2max and p1!=p1max):
            p1+=1
            p2=p1+1
            p3=p2+1    
        elif(p3==p3max and p2!=p2max):
            p2+=1
            p3=p2+1
        else:
            p3+=1
            
    if(sortArray[p1]+sortArray[p2]+sortArray[p3]<=t):
            count+=1
            
    return count
        
    

if __name__ == '__main__':
    
    
 def triplets(t, d):

    sortArray = sorted(d)
    count=0
    
    print(sortArray)
    
    if(len(sortArray)<2):
        return 0
    
    p1max=len(sortArray)-3
    p2max=len(sortArray)-2
    p3max=len(sortArray)-1
    
    p1=0
    p2=1
    p3=2
    
    while(p1!=p1max or p2!=p2max or p3!=p3max):
        
      
        
        if(sortArray[p1]+sortArray[p2]+sortArray[p3]<=t):
            count+=1
            
        if(p3==p3max and p2==p2max and p1!=p1max):
            p1+=1
            p2=p1+1
            p3=p2+1    
        elif(p3==p3max and p2!=p2max):
            p2+=1
            p3=p2+1
        else:
            p3+=1
            
    if(sortArray[p1]+sortArray[p2]+sortArray[p3]<=t):
            count+=1
            
    return count



















    def triplets(t,d):
    d.sort()
    count = 0
    for i in reversed(range(len(d))):
        if i == 1:
            break
        # print('check', d[i])
        sum_to_search = t - d[i]
        # print('sum',sum_to_search)
        p1 = 0
        p2 = 1
        p2_max = i-1
        p1_max = i-2
        while(p1 <= p1_max):
            if(p2 == p2_max+1):
                p1+=1
                p2 = p1 + 1
                continue
            if(d[p1]+d[p2] <=sum_to_search):
                count +=1
            p2+=1
    # print('Print', count)
    return count



def triplets(t, d):

    sortArray = sorted(d)
    count=0
    p1 = len(d)
    p2 = len(d)-1
    p3 = len(d)-2
    
    for i in range(0,p3):
        if(t-sortArray[i]<0):
            break
        for j in range(1,p2):
            if(t-sortArray[i]-sortArray[k]<0):
                break
            for k in range(2,p1):
                if(sortArray[i]+sortArray[j]+sortArray[k]<=t):
                    count+=1
                else:
                    break
            
    return count