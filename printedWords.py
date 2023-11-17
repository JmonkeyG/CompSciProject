import os
import matplotlib as plt
import wordData


def printedWords(words: dict) -> list:
    """
    The func takes a dictionary of words and how much they appeared each year
    then returns a list of tuple pairs containing (year, yearWordCount)

    :param words:
    :return:
    """
    pass


def wordsForYear(year: int, year_lst: list) -> int:
    """
    The func takes a year and a list of years and their word count

    :param year:
    :param year_lst:
    :return:
    """
    for yr in year_lst:
        if yr[0] == year:
            return yr[1]
    raise Exception('Error: year is not contained in year_lst')


def main():
    file_name = input('Enter a file name\n-> ')
    if not os.path.isfile(os.path.join('data', file_name)):
        raise Exception('Error: File does not exist')
    search_year = input(f'Enter a year to search in {file_name}\n-> ')
    for char in search_year:
        if not char.isdigit():
            raise Exception('Error: search year is not an integer')
    try:
        search_year = int(search_year)
        word_dictionary = wordData.readWordFile(file_name)
        year_lst = printedWords(word_dictionary)
        occurrences = wordsForYear(search_year, year_lst)
        match occurrences:
            case 1:
                print(f'The word {search_year} shows up {occurrences} time')
            case occurrences:
                print(f'The word {search_year} shows up {occurrences} times')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
