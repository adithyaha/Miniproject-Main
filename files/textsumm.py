import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import datetime
# Check if 'summary.txt' file exists
if os.path.isfile('summary.txt'):
    # If it exists, remove the file
    os.remove('summary.txt')
    
# Get the current date
current_date = datetime.datetime.now().strftime('%Y%m%d')

# Read the text from the file
notes_filename = current_date + '_notes.txt'



# Read the text from the file
with open('files/'+ notes_filename, 'r') as file:
    text = file.read()

# Rest of the code remains the same

# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Creating a frequency table to keep the score of each word
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Creating a dictionary to keep the score of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text
average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence

# Save the summary to the 'summary.txt' file
with open('files/summary.txt', 'w') as file:
    file.write(summary)
