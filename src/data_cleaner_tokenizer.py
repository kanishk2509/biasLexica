import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.utils import resample


# Performs basic tokenizing and character replacements
def pre_process_text(frame):
    frame.dropna(inplace=True)
    stop_words = set(stopwords.words('english'))
    for index, sentence in enumerate(frame):
        sentence = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', str(sentence))
        sentence = re.sub(r'[?|!|\'|’|"|#|@|_|:|“|”|-|"|-|-|<|>|{|}.|,|)|(|\|/]', r'', sentence)
        tokens = nltk.word_tokenize(sentence)
        words = [w for w in tokens if w not in stop_words]
        frame.loc[index] = (" ".join(map(str, words)))
    return frame


def main():
    # Reads the original news dump
    data_frame = pd.read_csv(r"..\datasets\/news_dump_1.csv",
                             encoding='utf-8')

    # Down sample the observations for our use case
    data_frame_down_sampled = resample(data_frame,
                                       replace=False,
                                       n_samples=2000,
                                       random_state=123)

    # Extracting data from only one source
    data_frame_new_york_times = data_frame_down_sampled[data_frame_down_sampled['publication'] == 'New York Times']

    # Extract relevant fields
    news_title = data_frame_new_york_times['title']
    news_content = data_frame_new_york_times['content']

    # Pre-processing of text
    news_title_cleaned = pre_process_text(news_title)
    news_content_cleaned = pre_process_text(news_content)

    # Concat the title and content of the news article
    df_new = pd.concat([news_title_cleaned, news_content_cleaned], axis=1, keys=['title', 'content'])
    df_new.to_csv(r"..\datasets\/news_dump_cleaned.csv",
                  encoding='utf-8', index=False)


if __name__ == '__main__':
    main()
