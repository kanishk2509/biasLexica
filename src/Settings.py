import os


# Settings class for word embedding task with required properties
class Settings:
    seeds = ['slur', 'policeman', 'handicap', 'homosexual', 'black',
             'fanatic', 'Latino', 'transgender', 'media', 'radical']
    os.chdir('..\datasets')
    cd = os.getcwd()
    file_to_read = cd + "\\news_dump_cleaned.csv"
    word2vec_model_file_name = 'trained_word2vec_model'
