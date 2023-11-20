import os.path
import matplotlib.pyplot as plt
import wordData


def printedWords(words: dict) -> list:
    """
    This function takes a dictionary of words and how many times they appeared each year
    and returns a list of tuple pairs containing (year, yearWordCount).

    :param words:
    :return:
    """
    if type(words) != dict:
        raise TypeError('Error: letterFreq() expected type dict for words parameter')
    word_count_by_year = {}
    for word, year_info in words.items():
        for year, count in year_info.items():
            word_count_by_year[year] = word_count_by_year.get(year, 0) + count
    return list(word_count_by_year.items())


def wordsForYear(year: int, year_lst: list) -> int:
    """
    The func takes a year and a list of years and their word count, and
    then returns the number of words that appeared for that year.

    :param year:
    :param year_lst:
    :return:
    """
    year_dict = {year: count for (year, count) in year_lst}
    if year in year_dict:
        return year_dict[year]
    raise IndexError('Error: year is not contained in year_lst')


def main():
    try:
        file_name = input('Enter a file name\n-> ')
        if not os.path.isfile(os.path.join('data', file_name)):
            raise FileNotFoundError('Error: File does not exist')
        search_year = input(f'Enter a year to search in {file_name}\n-> ')
        if not search_year.isdigit():
            raise ValueError('Error: search year is not an integer')
        search_year = int(search_year)
        word_dictionary = wordData.readWordFile(file_name)
        year_lst = printedWords(word_dictionary)
        occurrences = wordsForYear(search_year, year_lst)
        print(f'The year {search_year} contains {occurrences} word{"s" if occurrences != 1 else ""}')
        list_of_years, list_of_counts = zip(*year_lst)
        plt.plot(list_of_years, list_of_counts)
        plt.show()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
