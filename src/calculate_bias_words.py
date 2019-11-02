import nltk
import pandas as pd
from itertools import combinations
from Settings import Settings
from WordEmbeddings import WordEmbeddings


# Reads the csv file from the path variable and returns a pandas data frame
def data_factory(path, field):
    data_frame = pd.read_csv(path, encoding='utf-8')
    return data_frame[field]


# Tokenize a given sentence list/data frame
def tokenize(sentence):
    tokens = []
    for s in sentence:
        token = nltk.word_tokenize(s)
        tokens.append(token)
    return tokens


# Returns the mean of all the vector word representations for a given word space
def mean_vectorize_all_seeds(model, seeds):
    blob = model.wv[seeds[0]]
    b = blob.copy()
    for s in range(1, len(seeds)):
        b += model.wv[seeds[s]]
    return b / len(seeds)


# Performs combination operations for a given list and returns combined words from the list and their mean vector
def combinatorics(seeds, seed_combination, model):
    unique_combinations = [" ".join(map(str, comb)) for comb in combinations(seeds, seed_combination)]
    new_seeds = tokenize(unique_combinations)
    new_seeds_vector = mean_vectorize_all_seeds(model, new_seeds)
    vector_sum = new_seeds_vector[0]
    for i in range(1, len(new_seeds_vector)):
        vector_sum += new_seeds_vector[i]
    mean_new_seeds_vector = vector_sum / len(new_seeds_vector)
    return mean_new_seeds_vector, new_seeds


# Executable main function
def main():
    data_frame = data_factory(path=Settings.file_to_read, field='content')
    seeds = Settings.seeds
    word_embeddings = WordEmbeddings()
    tokens = tokenize(data_frame)

    '''Create word2vec model'''
    word_embeddings.create_word2vec_model(tokens)

    '''Print similar words based on the mean vector of all the word vectors from 'seeds' list'''
    mean_seeds_vector = mean_vectorize_all_seeds(model=word_embeddings.model, seeds=seeds)
    print('Closest 100 words for averaged seeds vectors: ')
    word_embeddings.print_similarity_by_vector(mean_seed_vector=mean_seeds_vector, max_count=100)

    '''
    Print similar words based on the mean vector of the 'seeds' combined and arranged as
    [['seed1', 'seed2'], ['seed1', 'seed3'], ['seed2', 'seed3'], ...]
    Train the model with the new seeds list
    Print the similar words based on the supplied vector
    '''
    mean_new_seeds_vector, new_seeds = combinatorics(seeds, seed_combination=2, model=word_embeddings.model)
    word_embeddings.model.train(new_seeds, total_examples=1, epochs=1)
    print('Closest 100 words for all seeds vectors combined as pairs and averaged: ')
    word_embeddings.print_similarity_by_vector(mean_seed_vector=mean_new_seeds_vector, max_count=100)

    '''
    Print similar words based on the mean vector of the 'seeds' combined and arranged as
    [['seed1', 'seed2', 'seed3], ['seed1', 'seed3', 'seed4], ...]
    Train the model with the new seeds list
    Print the similar words based on the supplied vector
    '''
    mean_new_seeds_vector, new_seeds = combinatorics(seeds, seed_combination=3, model=word_embeddings.model)
    word_embeddings.model.train(new_seeds, total_examples=1, epochs=1)
    print('Closest 100 words for all seeds vectors combined as triplets and averaged: ')
    word_embeddings.print_similarity_by_vector(mean_seed_vector=mean_new_seeds_vector, max_count=100)

    '''Print 100 most similar words to each word that exists in the seeds list'''
    word_embeddings.get_similarity_by_word(seeds, max_count=100)


if __name__ == '__main__':
    main()
