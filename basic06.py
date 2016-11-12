sentence = input("Enter the sentence to be reversed: ")
newsentence = []
word = ""
splitsentence = sentence.split()

while splitsentence != []:
	word = splitsentence.pop()
	newsentence.append(word)

print(newsentence)