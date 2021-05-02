
def longestPalindromicSubstring(s):

    length = len(s)
    p1=0
    diff = length
    p2 = p1+diff

    while(p2 <= length and diff != 0):
        
        sub = s[p1:p2]
        
        if( sub == sub[::-1] ):
            return sub

        if(p2 == length):
            diff-=1
            p1=0
            p2=p1+diff
            continue
        
        p1+=1
        p2+=1

    return s

        
print(longestPalindromicSubstring("xyxracecart"))
