import nltk

def lineCount():
    with open('allTagSequences.txt', 'r') as fileDatabase:
        fileDatabase.seek(0)                #Resets cursor to beginning of file
        lines = fileDatabase.read()    #Reads all lines of file
        sentences = nltk.sent_tokenize(lines)
        print(len(sentences))



lineCount()