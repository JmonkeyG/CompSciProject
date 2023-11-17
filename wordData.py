import os.path


def readWordFile(file) -> dict or None:
    if not os.path.isfile(os.path.join('data', file)):
        raise Exception('Error: File does not exist')
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
    if word not in dictionary.keys():
        return 0
    result = 0
    for year in dictionary[word]:
        result += (dictionary[word])[year]
    return result


def main():
    file_name = input('Enter a file name\n-> ')
    if not os.path.isfile(os.path.join('data', file_name)):
        raise Exception('Error: File does not exist')
    search_word = input(f'Enter a word to search in {file_name}\n-> ')
    try:
        word_dictionary = readWordFile(file_name)
        occurrences = totalOccurrences(search_word, word_dictionary)
        match occurrences:
            case 1:
                print(f'The word {search_word} shows up {occurrences} time')
            case occurrences:
                print(f'The word {search_word} shows up {occurrences} times')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
