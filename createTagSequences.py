import nltk

#Import/read text file to text variable. I got Pride and Prejudice from Project Gutenberg and 
#put it in "pandp.txt" so we can test it out. Is this the best way to go about it?

#Open a file and return read file as string
def openNewSentence(someFileName):
	with open(someFileName, 'r+') as fileInput:
		newSentence = fileInput.read()

		return newSentence

#If you want to use some hard-coded text to test
def useTestSentence():
	text = """It is a truth universally acknowledged, that a single man in possession
	of a good fortune, must be in want of a wife.

	However little known the feelings or views of such a man may be on his
	first entering a neighbourhood, this truth is so well fixed in the minds
	of the surrounding families, that he is considered the rightful property
	of some one or other of their daughters.
	"""

	return text

#Convert sentences to list of tags and then call write function
def convertToTags(someSentences):
	#Converting sentences into POS tags.
	for sents in someSentences:
		tokens = nltk.word_tokenize(sents)      #Sents converted to list of words.
		tagged = nltk.pos_tag(tokens)           #Words to word and POS tag pairs.

		tags = [tags[1] for tags in tagged]     #Just the tags.

		#Write tags to a file
		writeTagsToFile(tags)

#Append tags to output file
#So if you keep running it without deleting output file, it'll append over and over
def writeTagsToFile(someListOfTags):
	with open('allTagSequences.txt', 'a') as fileOutput:
		for tag in someListOfTags:
			fileOutput.write(tag + "\t")        #Export the tags (separated here by a tab)
		fileOutput.write("\n")                  #Every sentence's tag sequence will start on a new line


#Will be used to check for a match or check for duplicates
def checkForExistingPattern(somePatternOfTags):
	print("test")


#Main function
def main():
	#Open a file and import the text in
	importSentence = openNewSentence("randSents.txt")

	#If you want to use the hard coded test sentence
	#Just replace the importSentence parameter below with testSentence
	testSentence = useTestSentence();

	#Convert raw text into list of sentences.
	sentences = nltk.sent_tokenize(importSentence)

	#Convert the sentences to a list of tags
	convertToTags(sentences)

	

#Start the program
main()