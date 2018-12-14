from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from datetime import datetime
import json
import pymongo

class MyListener(StreamListener):
    consumerKey = ''
    consumerSecretKey = ''
    token = ''
    secretToken = ''
    keywords = []

    def __init__(self):
        self.authetication()
        self.startDatabase()

    def on_data(self, dados):
        tweet = json.loads(dados)
        text = tweet["text"]
        quoted_text = None
        retweeted_text = None
        print(tweet)
        print ("\n")
        if "extended_tweet" in tweet:
            text = tweet["extended_tweet"]["full_text"]

        if tweet["is_quote_status"]:
            quoted_text = tweet["quoted_status"]["text"]
            if "extended_tweet" in tweet["quoted_status"]:
                quoted_text = tweet["quoted_status"]["extended_tweet"]["full_text"]

        if "retweeted_status" in tweet:
            retweeted_text = tweet["retweeted_status"]["text"]
            if "extended_tweet" in tweet["retweeted_status"]:
                retweeted_text = tweet["retweeted_status"]["extended_tweet"]["full_text"]

        obj = {
            "created_at": tweet["created_at"],
            "text": text,
            "user_name": tweet["user"]["name"],
            "user_id": tweet["user"]["id"],
            "user_location": tweet["user"]["location"],
            "hashtags": tweet["entities"]["hashtags"],
            "quoted_text": quoted_text,
            "retweeted_text": retweeted_text
        }
        self.collection.insert_one(obj)
        print (obj)
        print ("\n")
        return True

    def startDatabase(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.twitter
        self.collection = self.db.tweets
        return True

    def authetication(self):
        self.auth = OAuthHandler(self.consumerKey, self.consumerSecretKey)
        self.auth.set_access_token(self.token, self.secretToken)


if __name__ == "__main__":
    mylistener = MyListener()
    mystream = Stream(mylistener.auth, listener=mylistener, tweet_mode='extended')
    mystream.filter(track=mylistener.keywords, languages=['pt'])
