import os.path
import matplotlib.pyplot as plt
import wordData


letters = 'abcdefghijklmnopqrstuvwxyz'


def makeLetterDict() -> dict:
    """
    The func makes a dictionary of all the letters of the alphabet and their frequency
    and then returns the dictionary of each letter with a value of 0.

    :return:
    """
    result = dict()
    for char in letters:
        result[char] = 0
    return result


def checkLetterCount(word: str, words: dict, alphabet: dict) -> dict:
    """
    The func finds the occurrence of a word and adds that count for each
    letter in the word to the alphabet dictionary.

    :param word:
    :param words:
    :param alphabet:
    :return:
    """
    occurrences = wordData.totalOccurrences(word, words)
    for char in word:
        alphabet[char] += occurrences
    return alphabet


def letterFreqDict(words: dict) -> dict:
    """
    The func calls other functions in order to make a list of letters
    and their count of occurrences and then sorts the dictionary in
    descending order based on the count and returns it.

    :param words:
    :return:
    """
    alphabet = makeLetterDict()
    for word in words.keys():
        alphabet = checkLetterCount(word, words, alphabet)
    result = dict(sorted(alphabet.items(), key=lambda x: x[1], reverse=True))
    return result


def letterFreq(words: dict) -> str:
    """
    The func goes through each word in the file and runs the
    checkLetterCount() function and the orders the list of keys
    based on their count in descending order.

    :param words:
    :return:
    """
    result = ''
    if type(words) != dict:
        raise TypeError('Error: letterFreq() expected type dict for words parameter')
    for letter in letterFreqDict(words).keys():
        result += letter
    return result


def main():
    file_name = input('Enter a file name\n-> ')
    if not os.path.isfile(os.path.join('data', file_name)):
        raise FileNotFoundError('Error: File does not exist')
    words_dict = wordData.readWordFile(file_name)
    letter_counts = letterFreqDict(words_dict)
    order = ''
    for letter in letter_counts.keys():
        order += letter
    print(f'The order of the letter frequency is "{order}"')
    alphabet_freq = sorted(letter_counts.items(), key=lambda x: x[0])
    values_lst = []
    for item in alphabet_freq:
        values_lst.append(item[1])
    plt.bar(list(letters), values_lst, color='skyblue')
    plt.show()


if __name__ == '__main__':
    main()
