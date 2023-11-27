import os.path
from numpy.linalg import norm
import numpy as np
import wordData


def getYearRange(words: dict) -> tuple[int, int]:
    """
    The func takes in a dictionary and returns the lowest and highest year
    in all the data.

    :param words:
    :return:
    """
    years = [year for year_info in words.values() for year in year_info.keys()]
    return min(years), max(years)


def topSimilar(words: dict, search_word: str) -> list:
    """
    The func takes a dictionary of words and their data and a search word.
    Then it makes an array of vectors for each word and a vector for the
    search word. Then it compares all the vectors using cosine similarity
    to determine the most similar. Finally, the func returns a list of the
    top 5 most similar words.

    :param words:
    :param search_word:
    :return:
    """
    low, high = getYearRange(words)
    word_vectors = {}
    for word, year_info in words.items():
        word_vectors[word] = [year_info.get(year, 0.001) for year in range(low, high + 1)]

    vector_array = np.array(list(word_vectors.values()))
    compare_vector = np.array(word_vectors[search_word])
    numpyArray = [np.dot(vector, compare_vector)/(norm(vector)*norm(compare_vector)) for vector in vector_array]

    word_sim = {}
    for i in range(len(word_vectors.keys())):
        word_sim[list(word_vectors.keys())[i]] = numpyArray[i]
    word_sim = sorted(word_sim.items(), key=lambda x: x[1], reverse=True)[0:5]
    return [word[0] for word in word_sim]


def printResults(lst):
    """
    The func takes the results from the program and prints the
    list of similar words.

    :param lst:
    """
    print(f'\nThe top {len(lst)} results are:')
    for word in lst:
        print(f'{word}')


def main():
    try:
        file_name = input('Enter a file name\n-> ')
        if not os.path.isfile(os.path.join('data', file_name)):
            raise FileNotFoundError('Error: File does not exist')
        word_dictionary = wordData.readWordFile(file_name)
        search_word = input(f'Enter a word to search in {file_name}\n-> ')
        if search_word not in word_dictionary.keys():
            raise KeyError('Error: Search word not contained in data')
        printResults(topSimilar(word_dictionary, search_word))
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
