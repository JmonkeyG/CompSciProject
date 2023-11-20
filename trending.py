import os.path
import wordData


def trending(words: dict, startYr: int, endYr: int) -> list:
    """
    The func takes in a dictionary of words with their years and word count, a start year,
    and an end year. Then it if the word count for both the start year and end year is
    greater than 1000, the function will make a tuple of the word and its trend value
    (end year word count/start year word count) and append it to the result list.
    Finally, the func will sort the list in reverse order and return the list.

    :param words:
    :param startYr:
    :param endYr:
    :return:
    """
    if type(words) != dict:
        raise TypeError('Error: letterFreq() expected type dict for words parameter')
    result = []
    for word, year_info in words.items():
        if startYr in year_info.keys() and endYr in year_info.keys():
            if year_info[startYr] >= 1000 and year_info[endYr] >= 1000:
                result.append((word, year_info[endYr]/year_info[startYr]))
    result.sort(key=lambda x: x[1], reverse=True)
    return result


def printResults(trend_lst: list, start_year: str, end_year: str):
    """
    The func takes in the results from trending() and prints the results
    line by line depending on the length of the list.

    :param trend_lst:
    :param start_year:
    :param end_year:
    """
    top_count = 10
    bottom_count = 10
    if len(trend_lst) < 10:
        top_count = len(trend_lst)
        bottom_count = 0
    elif 10 <= len(trend_lst) < 20:
        top_count = 10
        bottom_count = len(trend_lst) - 10
    if top_count > 0:
        print(f'\nThe top {top_count} trending word from {start_year} to {end_year}:')
        for i in range(top_count):
            print(str((trend_lst[i])[0]))
    if bottom_count > 0:
        print(f'\nThe bottom {bottom_count} trending word from {start_year} to {end_year}:')
        for i in range(len(trend_lst) - bottom_count, len(trend_lst)):
            print(str((trend_lst[i])[0]))


def main():
    try:
        file_name = input('Enter a file name\n-> ')
        if not os.path.isfile(os.path.join('data', file_name)):
            raise FileNotFoundError('Error: File does not exist')
        start_year = input(f'Enter a start year to search in {file_name}\n-> ')
        if not start_year.isdigit():
            raise ValueError('Error: start year is not an integer')
        end_year = input(f'Enter an end year to search in {file_name}\n-> ')
        if not end_year.isdigit():
            raise ValueError('Error: end year is not an integer')
        words = wordData.readWordFile(file_name)
        trend_lst = trending(words, int(start_year), int(end_year))
        printResults(trend_lst, start_year, end_year)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
