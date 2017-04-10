import nltk

#Import/read text file to text variable. I got Pride and Prejudice from Project Gutenberg and 
#put it in "pandp.txt" so we can test it out. Is this the best way to go about it?



#Raw text from file.
text = """It is a truth universally acknowledged, that a single man in possession
of a good fortune, must be in want of a wife.

However little known the feelings or views of such a man may be on his
first entering a neighbourhood, this truth is so well fixed in the minds
of the surrounding families, that he is considered the rightful property
of some one or other of their daughters.
"""

#Convert raw text into list of sentences.
sentences = nltk.sent_tokenize(text)


#Converting sentences into POS tags.
for sents in sentences:
    tokens = nltk.word_tokenize(sents)      #Sents converted to list of words.
    tagged = nltk.pos_tag(tokens)           #Words to word and POS tag pairs.

    tags = [tags[1] for tags in tagged]     #Just the tags.
    print (tags)                            #Should export each one to file.




