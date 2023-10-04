import tweepy
import time

#Authentication for twitter using API keys and secrets

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me

#Delays api calls if limit is reached to prevent getting in trouble w twitter
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next
    except tweepy.RateLimitError:
        time.sleep(300)

search_string = 'python'
numbersOfTweets = 2

#Finds 2 tweets that has 'python' in them and likes them.
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break