import nltk

def lineCount(fileName):
    with open(fileName, 'rb') as fileDatabase:
        fileDatabase.seek(0)                #Resets cursor to beginning of file
        lines = fileDatabase.read().decode('utf8', 'ignore')    #Reads all lines of file
        sentences = nltk.sent_tokenize(lines)
        return(len(sentences))



##lineCount('allTagSequences.txt')