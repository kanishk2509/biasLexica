import gensim
import os.path
import pandas as pd
from Settings import Settings


class WordEmbeddings:
    model = None

    # Creates and saves a word2vec model for a given set of tokens
    def create_word2vec_model(self, tokens):
        model_name = Settings.word2vec_model_file_name
        # Check if a model already exists in the storage to save up re run time
        if os.path.isfile(model_name):
            print('-----------------------------------------------------')
            print('Loading pre-trained model: {} ...'.format(model_name))
            print('-----------------------------------------------------')
            # Loads the model from the disk
            model = gensim.models.Word2Vec.load(model_name)
        else:
            print('-----------------------------------------------------')
            print('Training model: {} ...'.format(model_name))
            print('-----------------------------------------------------')
            model = gensim.models.Word2Vec(tokens, size=150, window=5, min_count=1, workers=4)
            print('Saving model as {}'.format(model_name))
            print('-----------------------------------------------------')
            # Saves the model to the disk
            model.save(model_name)
        self.model = model

    # Computes n=max_count similar words for each word in 'seeds'
    def get_similarity_by_word(self, seeds, max_count):
        for seed in seeds:
            similar_representations = self.model.wv.most_similar(seed, topn=max_count)
            print("For the bias word {}, the {} most similar bias words are: ".format(seed.upper(), max_count))
            print(similar_representations)
            df = pd.DataFrame(similar_representations, columns=['word', 'cosine_distance'])
            df.to_csv(r"..\datasets\/similar_words_for_{}.csv".format(seed.upper()), encoding='utf-8', index=False)
            print('Result saved as: similar_words_for_{}.csv in directory /datasets '.format(seed.upper()))
            print('-----------------------------------------------------')

    # Computes n=max_count similar words for a given word vector
    def print_similarity_by_vector(self, mean_seed_vector, max_count):
        print(self.model.wv.similar_by_vector(mean_seed_vector, topn=max_count))
        print('-----------------------------------------------------')
