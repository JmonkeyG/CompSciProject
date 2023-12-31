# Computer Science I Project
### Institution: Rochester Institute of Technology (RIT)
### Course: CSCI 141 Computer Science I
### Author: John Brown

<br> 

**Project Files**

> ### [wordData.py](wordData.py)
> #### wordData is Task 0 and the central project file that all other files in the project will relate to for their own functions.
> #### wordData has 3 functions inside of it:
> - readWordFile(file)
>   - *The func takes in a file name and returns a dictionary in the format {word: {year: word_count, ...}, ...}*
> - totalOccurrences(word, dictionary)
>   - *The func takes a word and a dictionary of words and returns the number of times that word appears for all years.*
> - main()
>   - *When run on its own wordData will ask the user to input a file name and a word to search for in that file. Then it
>   returns a string stating how many times the word appeared in the file.*

> ### [letterFreq.py](letterFreq.py) 
> #### letterFreq is Task 1 of the project which interprets a given dictionary and figures out the letters frequency within the dictionary of words.
> #### letterFreq has 5 functions inside of it:
> - makeLetterDict()
>   - *The func makes a dictionary of all the letters of the alphabet and their frequency and then returns the 
>   dictionary of each letter with a value of 0.*
> - checkLetterCount(word, words, alphabet)
>   - *The func finds the occurrence of a word and adds that count for each letter in the word to the alphabet 
>   dictionary.*
> - letterFreqDict(words)
>   - *The func calls other functions in order to make a list of letters and their count of occurrences and then sorts 
>   the dictionary in descending order based on the count and returns it.*
> - letterFreq(words)
>   - *The func goes through each word in the file and runs the checkLetterCount() function and the orders the list of 
>   keys based on their count in descending order.*
> - main()
>   - *When run on its own letterFreq will ask the user to input a file name. Then it returns a string stating the order
>   of letters with the most occurrences in descending order. Finally, the function plots a bar graph in alphabetical 
>   order of each letter's occurrence.*

> ### [printedWords.py](printedWords.py)
> #### printedWords desc
> #### printedWords has 3 functions inside of it:
> - printedWords(words)
>   - *This function takes a dictionary of words and how many times they appeared each year
>   and returns a list of tuple pairs containing (year, yearWordCount).*
> - wordsForYear(year, year_lst)
>   - *The func takes a year and a list of years and their word count, and
    then returns the number of words that appeared for that year.*
> - main()
>   - *When run on its own printedWords will ask the user to input a file name and a year to search. Then it returns a 
>   string that states how many words appeared for the given year. Finally, the function plots a line graph of all the
>   years and their word count.*

> ### [trending.py](trending.py)
> #### trending desc
> #### trending has 3 functions inside of it:
> - trending(words, startYr, endYr)
>   - *The func takes in a dictionary of words with their years and word count, a start year, and an end year. Then it 
>   if the word count for both the start year and end year is greater than 1000, the function will make a tuple of the 
>   word and its trend value (end year word count/start year word count) and append it to the result list. Finally, the 
>   func will sort the list in reverse order and return the list.*
> - printResults(trend_lst, start_year, end_year)
>   - *The func takes in the results from trending() and prints the results line by line depending on the length of the 
>   list.*
> - main()
>   - When run on its own trending will ask the user to input a file name, a start year, and an end year. Then it will 
>   print out a list of the top 10 trending words and the bottom 10 trending words.

> ### [wordSimilarity.py](wordSimilarity.py)
> #### wordSimilarity desc
> #### wordSimilarity has 4 functions inside of it:
> - getYearRange(words)
>   - *The func takes in a dictionary and returns the lowest and highest year in all the data.*
> - topSimilar()
>   - *The func takes a dictionary of words and their data and a search word. Then it makes an array of vectors for each
>   word and a vector for the search word. Then it compares all the vectors using cosine similarity to determine the 
>   most similar. Finally, the func returns a list of the top 5 most similar words.*
> - printResults()
>   - *The func takes the results from the program and prints the list of similar words.*
> - main()
>   - *When run on its own wordSimilarity will ask the user to input a file name and a word to check the similarities 
>   to. Then it will print out the closest 5 words in similarity.*

<br>

## Overall Description
#### The overall purpose of the project is to write python files that interpret text files containing data, and then return data and plot graphs based on the returned data.

### To-Do:
- [x] Create Project outline
- [x] Write wordData.py
- [x] Write letterFreq.py
- [x] Write printedWords.py
- [x] Write trending.py
- [x] Write wordSimilarity.py
- [x] All tests work
- [ ] All inputs are backed up with fail-safes
- [ ] All code is optimized
- [ ] All code is cleaned up and looks nice