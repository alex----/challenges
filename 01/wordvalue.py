from data import DICTIONARY, LETTER_SCORES
import unittest


def load_words(file_name=DICTIONARY):
    """Load dictionary into a list and return list"""
    # Feels like returning a set is probably better?
    # However the test requires the order to be specific
    with open(file_name, 'r') as dict_file:
        return dict_file.read().splitlines()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words(DICTIONARY)
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    unittest.main(module='test_wordvalue', exit=True)
