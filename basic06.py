"""
Write the pseudocode and code for a function that reverses the words in a sentence.
Input: "This is awesome"   Output: "awesome is This".   Give the Big O notation.

Pseudocode:

sentence <-- n
for word in sentence:
	newSentence.append(sentence(-word))
print newSentence

"""
sentence = input("Enter the sentence to be reversed: ")
newsentence = []
word = ""
splitsentence = sentence.split()

while splitsentence != []:
	word = splitsentence.pop()
	newsentence.append(word)

print(newsentence)