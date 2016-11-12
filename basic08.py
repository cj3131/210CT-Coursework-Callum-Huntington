vowels = ["a","e","i","o","u"]
newstring = ""
sentence = input("Enter the string to de-vowel: ")



def removeVowels(originalString, vowelList):

    if not originalString:
        return "" #originalString
    
    elif originalString[0] in vowelList:
        return removeVowels(originalString[1:], vowelList)
        
    # so originalString[0] must not be in vowelList:
    return (originalString[0] + removeVowels(originalString[1:], vowelList))



newstring = removeVowels(sentence, vowels)
print(newstring)
