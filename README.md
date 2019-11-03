## Task Summary
1. Scrape a dataset from an english newspaper with at least a 1000 articles and no older than 2017. 
2. Write a program in Python which takes the scraped data set and calculates the 1000 most likely bias words for any 10 chosen bias words of your choice. 
3. So 10 words should be chosen that are thought to be good examples for bias in the scraped dataset.
4. Use word embeddings to calculate the 100 most similar words to each of those 10 words. 
5. Print out the cosine distances of each word to all its most similar words. 


## Desired Result
For each of the 10 chosen bias words, the program will print out 100 most similar words along with their cosine distances (from the chosen word).</br>

Output for each of the seed word will be saved in a csv file in directory `/datasets` with columns being `word` and `cosine distance`. 

## How to Execute
From PyCharm (Recommended), simply execute the file 

`calculate_bias_words.py`

OR


From the terminal, in 'src' directory, execute the command 

`python calculate_bias_words.py`

## News dump taken from Kaggle

`https://www.kaggle.com/snapcrack/all-the-news/version/1#articlespart2.csv`
