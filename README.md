# The Methods of Rationality:  What You Don't See

Harry Potter and the Methods of Rationality by Eliezer Yudkowsky is the best book I've ever read.  So naturally, it's the one that I was going to use for analysis.

I look at the following things:

* [The number of words and sentences in each chapter](#number-of-words-and-sentences-per-chapter)
* [The normalized number of words and sentences in each chapter](#normalized-number-of-words-and-sentences-per-chapter)
* [The number of words in each sentence](#number-of-words-per-sentence)
* [The most common words and their frequencies](#most-common-words)
* [The most common words and their frequencies in each chapter](#most-common-words-per-chapter)
* [Frequencies of word lengths](#frequencies-of-word-lengths)
* [Average word lengths across chapters](#average-word-length-per-chapter)
* [Relative positions and dispersion of keywords](#disperson-of-keywords)
* [Relative positions and dispersion of positive and negative sentences - Sentiment Analysis](#sentiment-analysis)


### Number of Words and Sentences per Chapter

![Count of Words and Sentences in Each Chapter]( "Count of Words and Sentences in Each Chapter")

Chapter lengths vary dramatically, with some chapters approacing the 10k word cap, and others trailing behind with less than a thousand words (and chapters like 99 representing a significant outlier).  The median range seems to be of 2000-4000 word chapters.


### Normalized Number of Words and Sentences per Chapter

![Normalized Count of Words and Sentences in Each Chapter]( "Normalized Count of Words and Sentences in Each Chapter")

As can be seen, the number of sentences coincide almost exactly with the number of words across chapters, with few notable exceptions in already exceptionally long chapters.  This indicates that sentence length is consistent through the book.


### Number of Words per Sentence

![Count of Words Per Sentence]( "Count of Words Per Sentence")

The number of sentences worked against the data representation here.  The actual average sentence length is something much more reasonable, but because of the frequent (not frequent enough to seriously impact the average) presence of incredibly long sentences, the data ends up looking like this.

However, we do get an important piece of information from this: Eliezer loves long sentences.  There are more than a few dozen sentences with over a hundred words, and four with over 250.


### Most Common Words

![Most Common Words]( "Most Common Words")

Perhaps the most striking (and in my opinion, only true) criticism of the book is best expressed by the fact that the two most common words by a considerable margin, are "Harry" and "said".  Following that are several names (I was surprised to find Draco ranked above Hermione, but not so much after considering that his name would have come up more often in third-person), and descriptive terms that are almost keywords into the nature of the story - 'think', 'know', 'right', 'might', are all words indicative of Harry's incessant nature to question the workings of the world, and flawed conceptions he sees in others.


### Most Common Words per Chapter

![Most Common Words in Chapter]( "Most Common Words in Chapter")

I looked at three chapters in particular here: Chapter 1: A Day of Very Low Probability, Chapter 45: Humanism, Pt 3 (My favourite chapter), and Chapter 122: Something to Protect: Hermione Granger.

The first chapter seems pretty standard, with names and honorifics featured prominently, as first chapters are often wont to exposit.  Here also, Harry's name is less overwhelmingly frequent, again due to the need to introduce so many different concepts at once.

Chapters 45 features even more of the descriptive-keyword terms, but expected here, as the majority of the chapter is introspective (and what an introspection it was).

Something notable about the last chapter is that it is the first word frequency analysis I did on the book that turned up something other than "said" for the most frequent term after "Harry".  Fitting, given what that chapter says about the nature of heroes in the story.


### Frequencies of Word Lengths

![Frequency Distribution of Word Lengths]( "Frequency Distribution of Word Lengths")

The majority of words are between four and seven characters in length.  However, there is a significant portion of words that are seven or more letters in length.  The average length of a word in general English being less than 5 characters, this indicates a relatively complex prose.


### Average Word Length per Chapter

![Distribution of Average Word Length across Chapters]( "Distribution of Average Word Length across Chapters")

As can be seen, most chapters average somewhere around the 6-character word length, with variance between adjacent chapters decreasing toward the end (again with the exception of Chapter 99).


### Disperson of Keywords

![Dispersion Plot of Keyword Positions in the Book]( "Dispersion Plot of Keyword Positions in the Book")

I chose a few keywords that seemed representative of the story at large, even if they aren't mentioned as often.  

"Science" and "Rationality" are mentioned primarily in the beginning of the book, where the story would have been more focussed on Harry's experimentation in magic, and initial reaction toward wizarding society and some wizards themselves, and taper off about a third of the way in, when he ceases his exploration of magic in light of his recklessness.

"Battle" is seen almost exclusively in the middle portion of the story, as the book starts to fully come into the serial fiction format.

"Death" is mentioned more often as the story progresses, and is most prevalent in the last quarter, as the book comes to terms with the true themes it deals with.


### Sentiment Analysis

![Dispersion Plot of Positive and Negative Sentences in the Book]( "Dispersion Plot of Positive and Negative Sentences in the Book")

