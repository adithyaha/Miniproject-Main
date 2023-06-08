# importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Input text - to summarize
text = """
A word counter is a tool that helps you to count the number of words in a document. Word counters can be used for a variety of purposes, such as tracking the progress of a writing project, ensuring that a document meets a specific word count requirement, or comparing the word counts of different documents.

There are a number of different word counters available online and as software applications. Some word counters are free to use, while others require a subscription fee.

To use a word counter, simply type or paste the text that you want to count into the word counter. The word counter will then display the number of words in the document.

Word counters can be a valuable tool for writers, editors, and students. By using a word counter, you can ensure that your documents are accurate and meet the requirements of your writing projects.

Here are some additional tips for using a word counter effectively:

Use a word counter to track your progress on a writing project. This can help you to stay on track and ensure that you are meeting your deadlines.
Use a word counter to ensure that a document meets a specific word count requirement. This is important for documents such as essays, reports, and articles.
Use a word counter to compare the word counts of different documents. This can be helpful for research purposes or for comparing the effectiveness of different writing styles.
By following these tips, you can use a word counter to improve your writing and to ensure that your documents are accurate and meet the requirements of your writing projects.

Here are some of the benefits of using a word counter:

Accuracy: Word counters are very accurate and can count the number of words in a document with a high degree of precision.
Ease of use: Word counters are very easy to use and can be used by anyone, regardless of their level of computer expertise.
Versatility: Word counters can be used for a variety of purposes, such as tracking the progress of a writing project, ensuring that a document meets a specific word count requirement, or comparing the word counts of different documents.
Free: There are a number of free word counters available online, making them accessible to everyone.
If you are looking for a way to count the number of words in a document, a word counter is a great option. Word counters are accurate, easy to use, and versatile, making them a valuable tool for writers, editors, and students.

 """

# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue
	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
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
print(summary)
