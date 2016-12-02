"""
Write the pseudocode and code for a function that reverses the words in a sentence.
Input: "This is awesome"   Output: "awesome is This".   Give the Big O notation.

Pseudocode:

sentence <-- n
for word in sentence:
	newSentence.append(sentence(-word))
print newSentence

Time complexity O(N). A longer sentence means more pop/append operations.
"""
sentence = input("Enter the sentence to be reversed: ")
newsentence = []
word = ""
splitsentence = sentence.split() # Separates a string into a list, with spaces " " as the separator

# Pop a word off from the end of the sentence, and add it to the end of the new list.
while splitsentence != []:
	word = splitsentence.pop()
	newsentence.append(word)

print(newsentence)