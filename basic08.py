"""
Q8: Write a recursive function (pseudocode and code) that removes
all vowels from a given string s. Input: "beautiful" Output: "btfl".

This program terminates when the user has entered a word or sentence and the copy without
vowels has been returned.

Any input is valid here, since anything can be represented as a string. The only thing 
that needs to be removed is vowels.

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
newString = ""
sentence = input("Enter the string to de-vowel: ")

def removeVowels(originalString, vowelList):

    if not originalString: #originalString is empty, so we are finished.
        return ""
    elif originalString[0] in vowelList: # if the first character of the string is a vowel, we will ignore it,
        return removeVowels(originalString[1:], vowelList) # and continue with the rest of the string
    return (originalString[0] + removeVowels(originalString[1:], vowelList)) # The first character is not a vowel,
                                                                             # so add it to the string to be returned

newString = removeVowels(sentence, vowels)
print(newString)
