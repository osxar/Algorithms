

def detectCapital(word):
    
    firstLetter = word[0]
    remainingWord = word[1:]
    result = True

    if (len(word)==1):
        return True
 
    if(firstLetter.isupper()):
        if (not remainingWord.isupper() and not remainingWord.islower()):
            result = False
    else:
        if(not remainingWord.islower()):
            result = False

    return result

print(detectCapital("HEllo"))


