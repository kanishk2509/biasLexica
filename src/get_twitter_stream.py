import tweepy
from tweepy import OAuthHandler, Cursor
import csv


def get_api(consumer_key, consumer_secret, access_token, access_secret):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


def print_program_header(user_screen_name):
    print("****************************************")
    print("", user_screen_name, "Twitter Stream Grab")
    print("****************************************")


def ask_newspaper_choice(news_source_list):
    print("****************************************")
    print("Select a news source to grab its twitter stream ")
    for v in news_source_list:
        print("{}. {}".format(v, news_source_list[v]))
        print("****************************************")
    return input("Your input: ")


def get_news_stream(api, news_source_twitter_id):
    csv_file = open('news_stream_fox.csv', 'w+', encoding='utf-8<', errors='replace')
    my_fields = ['tweet_id', 'created_at', 'text']
    csv_writer = csv.DictWriter(csv_file, fieldnames=my_fields)
    csv_writer.writeheader()

    user = api.get_user(news_source_twitter_id)
    print_program_header(user.name)
    # end_date = datetime.utcnow() - timedelta(days=30)
    for tweet in Cursor(api.user_timeline, id=news_source_twitter_id, tweet_mode='extended').items():
        csv_writer.writerow(
            {'tweet_id': tweet.id, "created_at": tweet.created_at, "text": tweet._json['full_text']})
    csv_file.close()


def main():
    """Twitter Account Keys"""
    key = ['xxx',
           'xxx',
           'xxx-xxx',
           'xxx']
    api = get_api(key[0], key[1], key[2], key[3])
    news_source_list = {"807095": "The New York Times (Input 1)", "1367531": "Fox News (Input 2)"}
    # get_news_stream(api, 807095)
    get_news_stream(api, 1367531)


if __name__ == '__main__':
    main()
