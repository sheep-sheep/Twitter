import tweepy

consumer_key = '8U3bzFLL0mJroJE0XvORNzYFR'
consumer_secret = '0WNDIYOHnaDb5qA0woOFRvmXz5qGT8ti5SFlmEncCZGyW4pgF4'
access_token = '1869401612-NgDAp9BHpbftOAz9oDmg6Z66zOldxZjBZ4dnTqp'
access_token_secret = 'Z2IyFbFtQDFSvBtC8TbQa1Wqnv8t28UYdE6yad1x7YXFo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# user = api.get_user('AlgoricZhang')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)