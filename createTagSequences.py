import nltk
import bisect
from lineCount import lineCount

#Open a file and return read file as string
def openNewText(someFileName):
    with open(someFileName, 'rb+') as fileInput:
        newText = fileInput.read().decode('utf8', 'ignore')

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
    count = 0
    for sents in someSentences:
        count += 1
        tokens = nltk.word_tokenize(sents)      #Sents converted to list of words.
        tagged = nltk.pos_tag(tokens)           #Words to word and POS tag pairs.

        tags = [tags[1] for tags in tagged]     #Just the tags.
        overallList.append(tags)
    print('Count: ' str(count))
    return overallList


#Append tags to output file
#So if you keep running it without deleting output file, it'll append over and over
def writeTagsToFile(someListOfTagSequences):
    with open('allTagSequences.txt', 'a+') as fileDatabase:
        someListOfTagSequences.sort()
        temp = [someListOfTagSequences[i] for i in range(len(someListOfTagSequences)) if i == 0 or someListOfTagSequences[i] != someListOfTagSequences[i-1]]
        for sequence in temp:
            if(checkForExistingPattern(sequence, fileDatabase) is False):
                for tag in sequence:
                    fileDatabase.write(tag + "\t")        #Export the tags (separated here by a tab)
                fileDatabase.write("\n")                  #Every sentence's tag sequence will start on a new line


#Will be used to check for a match or check for duplicates
#Given ONE sequence of patterns and a file, checks to see if there is a match
def checkForExistingPattern(somePattern, fileData):
    fileData.seek(0)                #Resets cursor to beginning of file
    lines = fileData.readlines()    #Reads all lines of file

    #Convert list to string to compare with file
    tempString = ''
    for tag in somePattern:     
        tempString = tempString + tag + "\t"       

    tempString = tempString + "\n"  #In order to match the newline character at the end of each line

    position = bisect.bisect(lines, tempString)     #Does the actual binary searching, and returns where it should go
    
    if(len(lines)==0):
        return False                                #If nothing in file yet, return False
    else:
        if(tempString == lines[position-1]):        #Checks to see if it already exists
            return True
    return False                                    #If never a match, return False


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
        grades = []
        for sequence in listOfSummarySentences:
            numSeqs += 1                                                        #Keeps track of total sentences
            if(checkForExistingPattern(sequence, fileDatabase) is True):        #If real sentence, score increases
                score += 1 
                grades.append(1)
            else:
                grades.append(0)                                                     
        
        print(score/numSeqs)
        print(grades)

#Main function
#Option 1 - Add grammatically correct sentences to database, type file name
#Option 2 - Grade a summary, type file name of summary
#Option 3 - Get break down of a sentence, type in sentence
def main():
    option = -1
    
    while option not in {1, 2 ,3}:
        option = input('Enter:\n 1 to import new sentences into the database.\n 2 to grade a summary.\n 3 to get a breakdown of a custom sentence.\n')
        try:
            option = int(option)
        except ValueError:
            print('That is not a number')

    if option == 1:
        sentencesToAddFile = input('Please type the file name of the new sentences you would like to add to the database: \n')
        print('Number of lines in ' + sentencesToAddFile + ': ' + str(lineCount(sentencesToAddFile)))

        #Open a file and import the text in for our "database"
        importSentence = openNewText(sentencesToAddFile)

        #Convert raw text into list of sentences.
        sentences = nltk.sent_tokenize(importSentence)

        #Convert the sentences to a list of tags
        listOfTags = convertToTags(sentences)

        #Will try to write add new sequences, if not already included
        writeTagsToFile(listOfTags)

        #Sort the specifice file by line.
        sortFile('allTagSequences.txt')

        print('Number of lines in allTagSequences.txt: ' + str(lineCount('allTagSequences.txt')))
        print('Number of lines in allTagSequences.txt: ' + str(sum(1 for line in open('allTagSequences.txt'))))
        
    elif option == 2:
        summaryFile = input('Please type the file name of the summary that you would like to have graded: \n')

        #Check a sequence and responds with match or not
        #Currently just using hardcoded examples, but they will
        #be read in from one of the computerized summeries
        #gradeSummary([['PRP', 'MD', 'VB', 'IN', 'PRP', 'PRQ', '.'],['PRP', 'MD', 'VB', 'IN', 'PRP', '.']])    #Bad Grammar (Made up 'PRQ')
        #gradeSummary([['PRP', 'MD', 'VB', 'IN', 'PRP', '.']])	    #Existing Grammar

        gradeSummary(convertToTags(nltk.sent_tokenize(openNewText(summaryFile))))
    elif option == 3:
        with open('allTagSequences.txt', 'r+') as fileDatabase:
            sentenceToBreakdown = input('Please type the sentence in that you would like to have broken down: \n')
            #Open the new sentences, tokenize it, convert it to just tokens
            sentenceToCheck = nltk.sent_tokenize(sentenceToBreakdown)
            listOfTags = convertToTags(sentenceToCheck)
            print(convertToTags(sentenceToCheck))
            for sequence in listOfTags:
                doesItExist = checkForExistingPattern(sequence, fileDatabase)
                print('Is sequence already in database: ' + str(doesItExist))
    

#Start the program
main()
