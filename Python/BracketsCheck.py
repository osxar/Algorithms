

def bracketsCheck(s):
    totalBracket = {"{":"}","[":"]","(":")"}

    stack = []

    for brk in s:

        if(brk in totalBracket):
            stack.append(brk)
        else:

            val = stack.pop()
        
            if(brk != totalBracket[val]):
                return False

    return len(stack) == 0 

s = '{[()]}'

print(bracketsCheck(s))