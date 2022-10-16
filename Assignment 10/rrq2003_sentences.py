"""Interprets text as paragraphs, sentences and words

Submitted by Reyhan Quayum, rrq2003
This script takes a chapter from the book Don Quixote de la Mancha and
analyzes it to separate it in paragraphs and sentences. It provides
some basic functionality to reformat and characterize the structure of
the text.
"""

"""
This class Sentence creates an object that allows the analysis and characterization of a sentence 
using the words it contains
"""


class Sentence:

    # constructor processes input text to generate a string with original text and a list of words for analysis

    def __init__(self, input_str):
        self.original_string = str(input_str)
        self.string = ""
        self.index = -1
        for character in self.original_string:
            if character in ["_", "“", "”"]:
                pass
            elif character in ["—", "\u2014"]:
                self.string += " "
            else:
                self.string += character

        self.new_list_words = []
        list_words = self.string.split(" ")
        self.uncapitalized_list_words = []
        for word in list_words:
            if word == '':
                continue
            if word[-1] in [".", "!", "?", ","]:
                self.new_list_words.append(word[:-1])
                self.uncapitalized_list_words.append(word[:-1].lower())
            else:
                self.new_list_words.append(word)
                self.uncapitalized_list_words.append(word.lower())

    # number of words in sentence

    def __len__(self):
        return len(self.new_list_words)

    # returns the original string

    def __str__(self):
        return self.original_string

    # generates an iterator associated with the sentence that moves through the words

    def __iter__(self):
        return self

    # moves to next word

    def __next__(self):
        self.index += 1
        if self.index <= len(self.new_list_words):
            pass
            return self.new_list_words[self.index]
        else:
            raise StopIteration

    # extracts the words by indexing

    def __getitem__(self, item):
        if item > len(self.new_list_words):
            return None
        else:
            return self.new_list_words[item]

    # returns True if the word is present in the word list independent of case

    def __contains__(self, item):
        if item.lower() in self.uncapitalized_list_words:
            return True
        else:
            return False

    # resets the position of the iterator

    def reset_iterator(self):
        self.index = -1
        return self.index

    # split the sentence at the character ";" generating a list of sentence objects

    def split(self):
        list_strings = []
        word = ""
        for c in self.original_string:
            if c != ";":
                word += c
            else:
                list_strings.append(word)
                word = ""
        list_strings.append(word)
        print(list_strings)
        list_sentences = []
        for s in list_strings:
            sentence = Sentence(s)
            list_sentences.append(sentence)
        return list_sentences

