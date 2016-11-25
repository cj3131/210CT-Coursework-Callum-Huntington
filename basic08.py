"""
Write a recursive function (pseudocode and code) that removes
all vowels from a given string s. Input: "beautiful" Output: "btfl".

Pseudocode:

def REMOVE_VOWELS(original, vowels:
	if original = "":
		return
	else if original[0] in vowels:
		return REMOVE_VOWELS(original[1:], vowels)
	return original[0] + REMOVE_VOWELS(original[1:], vowels)

print REMOVE_VOWELS(word, vowelList)

"""
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
