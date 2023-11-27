import os.path

from numpy import dot
from numpy.linalg import norm
import numpy as np
import wordData
from scipy.spatial import distance

def getNumRange(words: dict) -> tuple[int, int]:
    low = 0
    high = 0
    for word, year_info in words.items():
        for year, count in year_info.items():
            if low == 0:
                low = year
            if year <= low:
                low = year
            if year >= high:
                high = year
    return low, high


def topSimilar(words: dict, search_word: str):
    low, high = getNumRange(words)
    array_dict = dict()
    for word, year_info in words.items():
        array_dict[word] = []
        for i in range(low, high + 1):
            if i not in year_info.keys():
                array_dict[word].append(0.1)
            else:
                array_dict[word].append(year_info[i])
    word_counts = np.array(list(array_dict.values()))
    compare_array = np.array(array_dict[search_word])
    numpyArray = [np.dot(line, compare_array)/(norm(line)*norm(compare_array)) for line in word_counts]
    word_sim = dict()
    for i in range(len(array_dict.keys())):
        word_sim[list(array_dict.keys())[i]] = numpyArray[i]
    word_sim = sorted(word_sim.items(), key=lambda x: x[1], reverse=True)[0:5]
    return [word[0] for word in word_sim]


def main():
    try:
        file_name = input('Enter a file name\n-> ')
        if not os.path.isfile(os.path.join('data', file_name)):
            raise FileNotFoundError('Error: File does not exist')
        word_dictionary = wordData.readWordFile(file_name)
        search_word = input(f'Enter a word to search in {file_name}\n-> ')
        if search_word not in word_dictionary.keys():
            raise KeyError('Error: Search word not contained in data')
        topSimilar(word_dictionary, search_word)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
