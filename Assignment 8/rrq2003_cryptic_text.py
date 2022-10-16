"""This script requests some text, separates it by word, and returns the same text
but only the first and last letter of the word is returned along with the number of characters removed.

Submitted by Reyhan Quayum, rrq2003
"""
text = input("Enter some text")
separated = text.split(" ")
print(separated)
output = []
for word in separated:
    if len(word) >= 3:
        if word.isalpha():
            first, last = word[0], word[-1]
            new_word = first + last
            characters_removed = len(word) - len(new_word)
            new_word_with_number = first + str(characters_removed) + last
            output.append(new_word_with_number)
        else:
            no_punctuation_word = []
            punctuation_removed_list = []
            for character in word:
                if character.isalpha():
                    no_punctuation_word.append(character)
                else:
                    punctuation_removed_list.append(character)
            no_punctuation_wordstring = "".join(no_punctuation_word)
            first, last = no_punctuation_wordstring[0], no_punctuation_wordstring[-1]
            new_word = first + last
            characters_removed = len(no_punctuation_wordstring) - len(new_word)
            new_word_with_number_punctuation = first + str(characters_removed) + last + \
                                               "".join(punctuation_removed_list)
            output.append(new_word_with_number_punctuation)
    else:
        output.append(word)
output_string = " ".join(output)
print(output_string)

