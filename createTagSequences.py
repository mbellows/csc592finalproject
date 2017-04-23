import nltk

#Open a file and return read file as string
def openNewText(someFileName):
    with open(someFileName, 'r+') as fileInput:
        newText = fileInput.read()

        return newText

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
    overallList = []
    for sents in someSentences:
        tokens = nltk.word_tokenize(sents)      #Sents converted to list of words.
        tagged = nltk.pos_tag(tokens)           #Words to word and POS tag pairs.

        tags = [tags[1] for tags in tagged]     #Just the tags.
        overallList.append(tags)
    return overallList


#Append tags to output file
#So if you keep running it without deleting output file, it'll append over and over
def writeTagsToFile(someListOfTagSequences):
    with open('allTagSequences.txt', 'a+') as fileDatabase:
        for sequence in someListOfTagSequences:
            if(checkForExistingPattern(sequence, fileDatabase) is False):
                for tag in sequence:
                    fileDatabase.write(tag + "\t")        #Export the tags (separated here by a tab)
                fileDatabase.write("\n")                  #Every sentence's tag sequence will start on a new line


#Will be used to check for a match or check for duplicates
#Given ONE sequence of patterns and a file, checks to see if there is a match
def checkForExistingPattern(somePattern, fileData):
    fileData.seek(0)                #Resets cursor to beginning of file
    lines = fileData.readlines()    #Reads all lines of file

    for line in lines:
        line = line.split("\t")     #Split string of POS back into list of POS
        line = line[:-1]            #Strips off random '\n' that gets added?
        if(somePattern == line):
            return True             #If match, jump out of loop and return True
    return False                    #If never a match, return False


#Opens up the current file and sorts alphabetically. 
def sortFile(fileName):
    fileData = open(fileName, 'r+')
    lines = fileData.readlines()
    fileData.seek(0)
    lines.sort()
    for line in lines:
        fileData.write(line)


def gradeSummary(listOfSummarySentences):
    with open('allTagSequences.txt', 'r') as fileDatabase:
        score = 0
        numSeqs = 0
        for sequence in listOfSummarySentences:
            numSeqs += 1                                                        #Keeps track of total sentences
            if(checkForExistingPattern(sequence, fileDatabase) is True):
                score += 1                                                      #If real sentence, score increases
        
        print(score/numSeqs)

#Main function
def main():

    #Open a file and import the text in for our "database"
    importSentence = openNewText("shortSents.txt")

    #If you want to use the hard coded test sentence
    #just replace the importSentence parameter below with testSentence
    testSentence = useTestSentence();

    #Convert raw text into list of sentences.
    sentences = nltk.sent_tokenize(importSentence)

    #Convert the sentences to a list of tags
    listOfTags = convertToTags(sentences)

    #Will try to write add new sequences, if not already included
    writeTagsToFile(listOfTags)

    #Sort the specifice file by line.
    sortFile('allTagSequences.txt')

    #Check a sequence and responds with match or not
    #Currently just using hardcoded examples, but they will
    #be read in from one of the computerized summeries
    gradeSummary([['PRP', 'MD', 'VB', 'IN', 'PRP', 'PRQ', '.'],['PRP', 'MD', 'VB', 'IN', 'PRP', '.']])    #Bad Grammar (Made up 'PRQ')
    gradeSummary([['PRP', 'MD', 'VB', 'IN', 'PRP', '.']])	    #Existing Grammar

    #Open the new sentences, tokenize it, convert it to just tokens
    #newSentence = openNewSentence("newSentence.txt")
    #sentencesToCheck = nltk.sent_tokenize(importSentence)
    #convertToTags(sentencesToCheck)


#Start the program
main()
