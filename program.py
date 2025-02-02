from nltk import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib.pyplot as plt
import numpy as np
import string
import math



'''

Part I - Formatting => Dividing the book into arrays of chapter titles, locations, and contents, as well as some data for easy access.

'''


f = open("hpmor.txt")
chapter_names = []  # List of strings
chapter_indices = []  # List of integers
chapters = []  # List of strings
complete_text = ""
words_complete = []  # List of strings
sentences_complete = []  # List of strings
sentence_words = []  # List of lists of strings
sentence_length_in_words = []  # List of integers
chapter_words = []  # List of lists of strings
chapter_sentences = []  # List of lists of strings
chapter_avg_word_length = [] # List of integers
chapter_lengths_words = []  # List of integers
chapter_lengths_sentences = []  # List of integers
norm_chapter_lengths_words = []  # List of floats
norm_chapter_lengths_sentences = []  # List of floats
chapter_word_length_cumulative = []  # List of integers
chapter_sentence_length_cumulative = []  # List of integers
positive_sentences = []  # List of integers
negative_sentences = []  # List of integers
keywords = ['death', 'science', 'space', 'rationality', 'human', 'bias', 'fallacy', 'error', 'plot', 'game', 'battle', 'Dark']


# Extracting chapter names

for i in range(122):
	s = f.readline()
	index = s.find(' ')
	length = len(s)
	chapter_names.append(s[index+1:length-1])


# Extracting starting indexes of each chapter 

text = f.read()
for i in chapter_names:
	index = text.find(i + "\n")
	chapter_indices.append(index)


# Separating barely formatted chapter texts

for i in range(len(chapter_indices)):
	first_index = chapter_indices[i]
	if(i != len(chapter_indices) - 1):
		last_index = chapter_indices[i+1]
		chapter_text = text[first_index:last_index]
	if(i == len(chapter_indices) - 1):
		chapter_text = text[first_index:]
	chapter_text = chapter_text[chapter_text.find('\n'):].replace('\n', ' ').replace('\r', '').replace('*', '')
	chapters.append(chapter_text.strip())
	complete_text = complete_text + chapter_text


# Tokenizing text into significant words and sentences (stored in words_complete and sentences_complete), 
# storing signficant words in each sentence in sentence_words and their number in sentence_length_in_words

words_complete = word_tokenize(complete_text)
sentences_complete = sent_tokenize(complete_text)
for i in sentences_complete:
	words_in_sentence = word_tokenize(i)
	sentence_words.append(words_in_sentence)
	sentence_length_in_words.append(len(words_in_sentence))
stop_words = corpus.stopwords.words('english')
punctuations = string.punctuation
words_complete = [word for word in words_complete if len(word) > 2]
words_complete = [word for word in words_complete if word.lower() not in stop_words]
for i in punctuations:
	words_complete = [word for word in words_complete if i not in word]


# Tokenizing each chapter's text into significant words and sentences (stored in chapter_words and chapter_sentences)
# storing number of words and sentences in chapter_lengths_words and chapter_lengths_sentences,
# and normalized number of words and sentences in norm_chapter_lengths_words and norm_chapter_lengths_sentences

for i in chapters:
	words = word_tokenize(i)
	sentences = sent_tokenize(i)
	words = [word for word in words if len(word) > 2]
	words = [word for word in words if word.lower() not in stop_words]
	for i in punctuations:
		words = [word for word in words if i not in word]
	chapter_avg_word_length.append(sum(map(len, words)) / len(words))
	chapter_words.append(words)
	chapter_sentences.append(sentences)
cumulative = 0
for i in chapter_words:
	chapter_lengths_words.append(len(i))
	cumulative = cumulative + len(i)
	chapter_word_length_cumulative.append(cumulative)
largest = max(chapter_lengths_words)
for i in chapter_lengths_words:
	norm_chapter_lengths_words.append(i/largest)
cumulative = 0
for i in chapter_sentences:
	chapter_lengths_sentences.append(len(i))
	cumulative = cumulative + len(i)
	chapter_sentence_length_cumulative.append(cumulative)
largest = max(chapter_lengths_sentences)
for i in chapter_lengths_sentences:
	norm_chapter_lengths_sentences.append(i/largest)



'''

Part II - Final Formatting

'''


# Numpy array for chapter numbers

chapter_numbers_axis = np.array(range(1, 123))


# Numpy arrays for number of words in each chapter, and number of sentences in each chapter

chapter_words_axis = np.array(chapter_lengths_words)
chapter_sentences_axis = np.array(chapter_lengths_sentences)


# Numpy arrays for normalized number of words in each chapter, and normalized number of sentences in each chapter (Method of Normalization:  Each number is divided by the max in list) 

norm_chapter_words_axis = np.array(norm_chapter_lengths_words)
norm_chapter_sentences_axis = np.array(norm_chapter_lengths_sentences)


# Numpy arrays for number of sentences in text, and number of words in each sentence

sentence_numbers_axis = np.array(range(1, len(sentence_words) + 1))
sentence_length_in_words_axis = np.array(sentence_length_in_words)


# Numpy arrays for most frequent words in the book, and their frequency count

fdist = FreqDist(words_complete).most_common(50)
freq_words_axis = np.array([i[0] for i in fdist])
freq_values_axis = np.array([i[1] for i in fdist])


# Numpy arrays for lengths of words in the book, and their frequencies

word_length_fdist = FreqDist(len(word) for word in words_complete).most_common(19)
word_length_axis = np.array([i[0] for i in word_length_fdist])
freq_word_length_axis = np.array([i[1] for i in word_length_fdist])


# Numpy array for average word length in each chapter

chapter_avg_word_length_axis = np.array(chapter_avg_word_length)



'''

Part III - Plotting

'''


def plot_words_sents_per_chapter():
	plt.figure(1)
	plt.plot(chapter_numbers_axis, chapter_words_axis, label = "Word Count")
	plt.plot(chapter_numbers_axis, chapter_sentences_axis, label = "Sentence Count")
	plt.xlabel('Chapters')
	plt.ylabel('Number')
	plt.title("Count of Words and Sentences in Each Chapter")
	plt.legend()

def plot_norm_words_sents_per_chapter():
	plt.figure(2)
	plt.plot(chapter_numbers_axis, norm_chapter_words_axis, label = "Normalized Word Count")
	plt.plot(chapter_numbers_axis, norm_chapter_sentences_axis, label = "Normalized Sentence Count")
	plt.xlabel('Chapters')
	plt.ylabel('Number')
	plt.title("Normalized Count of Words and Sentences in Each Chapter")
	plt.legend()

def plot_words_per_sentence():
	plt.figure(3)
	plt.plot(sentence_numbers_axis, sentence_length_in_words_axis)
	plt.xlabel('Sentences')
	plt.ylabel('No. of Words')
	plt.title("Count of Words Per Sentence")

def plot_word_frequencies():
	plt.figure(4)
	plt.barh(freq_words_axis, freq_values_axis)
	plt.xlabel('Frequency')
	plt.ylabel('Word')
	plt.title("Most Common Words")

def plot_chapter_word_frequency(no):
	chapter_fdist = FreqDist(chapter_words[no - 1]).most_common(20)
	chapter_freq_words_axis = np.array([i[0] for i in chapter_fdist])
	chapter_freq_values_axis = np.array([i[1] for i in chapter_fdist])
	plt.figure()
	plt.barh(chapter_freq_words_axis, chapter_freq_values_axis)
	plt.xlabel('Frequency')
	plt.ylabel('Word')
	plt.title("Most Common Words in Chapter {}: {}".format(no, chapter_names[no-1]))

def plot_word_length_frequency():
	plt.figure(5)
	plt.bar(word_length_axis, freq_word_length_axis)
	plt.xlabel('Word Length')
	plt.ylabel('Frequency')
	plt.title("Frequency Distribution of Word Lengths")

def plot_avg_word_length():
	plt.figure(6)
	plt.plot(chapter_numbers_axis, chapter_avg_word_length_axis)
	plt.xlabel('Chapters')
	plt.ylabel('Average Word Length')
	plt.title('Distribution of Average Word Length across Chapters')

def plot_dispersion_keywords(words):
	keywords_axes = {}
	keywords_indices_axes = {}
	plt.figure(7)
	for word in words:
		keywords_indices_axes[word] = [i for i in range(len(words_complete)) if words_complete[i] == word]
		keywords_axes[word] = [word] * len(keywords_indices_axes[word])
		plt.scatter(keywords_indices_axes[word], keywords_axes[word], marker = '|', color='#1f77b4')
	for chapter in range(0, 122, 5):
		plt.axvline(chapter_word_length_cumulative[chapter], color='#E56967', linestyle='dotted', linewidth=1)
	plt.xlabel('Position')
	plt.ylabel('Word')
	plt.title('Dispersion Plot of Keyword Positions in the Book')

def plot_dispersion_sentiments(chapter):
	positive_sentences = []
	negative_sentences = []
	if chapter == 0:
		begin = 0
		end = chapter_sentence_length_cumulative[chapter]
	else:
		begin = chapter_sentence_length_cumulative[chapter - 1]
		end = chapter_sentence_length_cumulative[chapter]
	for sentence in range(begin, end):
		sentence_blob = TextBlob(sentences_complete[sentence], analyzer=NaiveBayesAnalyzer())
		if sentence_blob.sentiment.p_pos > 0.5:
			positive_sentences.append(sentence)
		else:
			negative_sentences.append(sentence)
	positive_sentences_locations_axis = np.array(positive_sentences)
	negative_sentences_locations_axis = np.array(negative_sentences)
	positive_sentences_axis = ["Positive Sentences"] * len(positive_sentences)
	negative_sentences_axis = ["Negative Sentences"] * len(negative_sentences)
	plt.figure(figsize=(15.0, 5.0))
	plt.scatter(positive_sentences_locations_axis, positive_sentences_axis, marker = '|', color='#1f77b4')
	plt.scatter(negative_sentences_locations_axis, negative_sentences_axis, marker = '|', color='#1f77b4')
	plt.xlabel('Position')
	plt.ylabel('Sentiment')
	plt.title('Dispersion Plot of Positive and Negative Sentences in the Book')
	name = "Chapter " + str(chapter+1) + " - " + chapter_names[chapter] + ".png"
	plt.savefig(name)
	plt.close()



'''

Part IV - Usage

'''


keep_going = True

while keep_going:
	print("Which of the following plots would you like to see?")
	print("1. Distribution of Words and Sentences per Chapter")
	print("2. Normalized Distribution of Words and Sentences per Chapter")
	print("3. Distribution of Words per Sentence")
	print("4. Distribution of the Most Common Words and their Frequencies")
	print("5. Distribution of the Most Common Words and their Frequencies in Each Chapter")
	print("6. Distribution of Word Lengths and their Frequencies")
	print("7. Distribution of Average Word Length across Chapters")
	print("8. Dispersion of Keyword Positions")
	print("9. Sentiment Analysis of Each Chapter (The graph will be saved to the folder)")
	print("10. Exit the program")
	print("If you have multiple choices, enter them separated by comma, or if a range, the first number and the last number separated by a hyphen.")
	print("Example: To choose 1 and 4, give the input '1,4' and to choose all of them, choose '1-9'.  To exit, give just '10'.  All without the quotes, obviously.")
	functions = [plot_words_sents_per_chapter, plot_norm_words_sents_per_chapter, plot_words_per_sentence, plot_word_frequencies, plot_chapter_word_frequency, 
				 plot_word_length_frequency, plot_avg_word_length, plot_dispersion_keywords, plot_dispersion_sentiments]

	while True:
		choice = input()
		chosen = []

		if choice == "10":
			keep_going = False
			break
		if len(choice) == 1:
			if not choice.isnumeric():
				print("Enter valid input, you blithering moron.")
				continue
			chosen = [functions[int(choice) - 1]]
		elif len(choice) == 3:
			if not choice[0].isnumeric() or choice[1] not in ',-' or not choice[2].isnumeric():
				print("Enter valid input, you blithering moron.")
				continue
			if choice[1] == ',':
				chosen = [functions[int(choice[0]) - 1], functions[int(choice[2]) - 1]]
			else:
				chosen = [functions[i] for i in range(int(choice[0]) - 1, int(choice[2]))]
		elif len(choice) % 2 == 1:
			flag = 0
			for i in range(0, len(choice) - 2, 2):
				if not choice[i].isnumeric() or choice[i + 1] != ',':
					flag = 1
				chosen.append(functions[int(choice[i]) - 1])
				chosen.append(functions[int(choice[i + 2]) - 1])
			if flag == 1:
				print("Enter valid input, you blithering moron.")
				continue
			if not choice[-1].isnumeric():
				print("Enter valid input, you blithering moron.")
				continue
		else:
			print("Enter valid input, you blithering moron.")
			continue
		break

	if plot_chapter_word_frequency in chosen:
		print("On which chapter would you like the distribution of most common words and their frequencies?")
		while True:
			chapter = input()
			if not chapter.isnumeric() or int(chapter) < 1 or int(chapter) > 122:
				print("Try again, you gibbering dullard.")
				continue
			break
		plot_chapter_word_frequency(int(chapter))
		chosen.remove(plot_chapter_word_frequency)

	if plot_dispersion_sentiments in chosen:
		print("On which chapter would you like the sentiment analysis dispersion? Because it takes a while to generate it for a given chapter, you're limited to one per go.")
		while True:
			chapter = input()
			if not chapter.isnumeric() or int(chapter) < 1 or int(chapter) > 122:
				print("Try again, you gibbering dullard.")
				continue
			break
		plot_dispersion_sentiments(int(chapter) - 1)
		chosen.remove(plot_dispersion_sentiments)

	for function in chosen:
		function()

	plt.show()



'''

Part V - Testing Section (This part's just to make it easier to debug the plotting functions)

'''

'''

plot_words_sents_per_chapter()
plot_norm_words_sents_per_chapter()
plot_words_per_sentence()
plot_word_frequencies()
plot_chapter_word_frequency(45)
plot_word_length_frequency()
plot_avg_word_length()
plot_dispersion_keywords(keywords)
for i in range(122):
	plot_dispersion_sentiments(i)  

plt.show()

'''