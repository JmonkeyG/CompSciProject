import os.path


def readWordFile(file) -> dict or None:
    """
    The func takes in a file name and returns a dictionary in
    the format {word: {year: word_count, ...}, ...}.

    :param file:
    :return:
    """
    if not os.path.isfile(os.path.join('data', file)):
        raise FileNotFoundError('Error: File does not exist')
    wordDict = dict()
    with open(os.path.join('data', file)) as file:
        temp = str()
        for line in file:
            stripped = line.strip()
            splitted = stripped.split(',')
            if (splitted[0])[0].isdigit():
                (wordDict[temp])[int(splitted[0])] = int(splitted[1])
            else:
                temp = str(stripped)
                wordDict[temp] = dict()
    return wordDict


def totalOccurrences(word: str, dictionary: dict) -> int:
    """
    The func takes a word and a dictionary of words and returns the
    number of times that word appears for all years.

    :param word:
    :param dictionary:
    :return:
    """
    if word not in dictionary.keys():
        return 0
    result = 0
    for year in dictionary[word]:
        result += (dictionary[word])[year]
    return result


def main():
    file_name = input('Enter a file name\n-> ')
    if not os.path.isfile(os.path.join('data', file_name)):
        raise FileNotFoundError('Error: File does not exist')
    search_word = input(f'Enter a word to search in {file_name}\n-> ')
    try:
        word_dictionary = readWordFile(file_name)
        occurrences = totalOccurrences(search_word, word_dictionary)
        print(f'The word {search_word} shows up {occurrences} time{"s" if occurrences != 1 else ""}')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
