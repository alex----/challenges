from data import DICTIONARY, LETTER_SCORES
import unittest


def load_words(file_name=DICTIONARY):
    """Load dictionary into a list and return list"""
    # Feels like returning a set is probably better?
    # However the test requires the order to be specific
    words = []
    with open(file_name, 'r') as dict_file:
        for word in dict_file:
            words.append(word.strip())
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    def lookup_char_value(char):
        if char.upper() in LETTER_SCORES:
            return LETTER_SCORES[char.upper()]
        return 0
    return sum(map(lookup_char_value, word))


def max_word_value_v1(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words(DICTIONARY)
    max_word = (None, 0)
    for word in words:
        word_score = calc_word_value(word)
        if word_score > max_word[1]:
            max_word = word, word_score
    return max_word[0]


def max_word_value_v2(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words(DICTIONARY)
    sorted_words = sorted(words, key=calc_word_value, reverse=True)
    return sorted_words[0]


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    # V1 is quite slow to loop this whole set
    # return max_word_value_v1(words)

    # this is using more of the sorted and so is less code to maintain
    # but requires you know a little more python
    # Still a little slow,
    # precomputing will speed up check sort by assuming we have a 1 to 1 load and sort, not that good an idea
    return max_word_value_v2(words)


if __name__ == "__main__":
    unittest.main(module='test_wordvalue', exit=True)
