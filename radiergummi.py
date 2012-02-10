#!/usr/bin/python

# source: https://gist.github.com/113241
# needs: http://packages.python.org/tweepy/html/
# license: beerware

import tweepy
import itertools

# OAuth Application settings
consumer_key = 'edit.this'
consumer_secret = 'edit.this'
# OAuth account access token
key = 'edit.this'
secret = 'edit.this'

# limits to keep
user_timeline_limit = 4
retweeted_by_me_limit = 3
favorites_limit = 3
direct_messages_limit = 2
sent_direct_messages_limit = 2

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, secure = True)
auth.set_access_token(key, secret)
api = tweepy.API(auth, secure = True)

user_timeline = tweepy.Cursor(api.user_timeline).items()
for status in itertools.islice(user_timeline, user_timeline_limit, None):
	api.destroy_status(status.id)
	print "deleted status:", status.id

retweeted_by_me = tweepy.Cursor(api.retweeted_by_me).items()
for status in itertools.islice(retweeted_by_me, retweeted_by_me_limit, None):
	api.destroy_status(status.id)
	print "deleted retweet:", status.id

favorites = tweepy.Cursor(api.favorites).items()
for status in itertools.islice(favorites, favorites_limit, None):
	api.destroy_favorite(status.id)
	print "deleted favorite:", status.id

direct_messages = tweepy.Cursor(api.direct_messages).items()
for direct_message in itertools.islice(direct_messages, direct_messages_limit, None):
	api.destroy_direct_message(direct_message.id)
	print "deleted direct message:", direct_message.id

sent_direct_messages = tweepy.Cursor(api.sent_direct_messages).items()
for direct_message in itertools.islice(sent_direct_messages, sent_direct_messages_limit, None):
	api.destroy_direct_message(direct_message.id)
	print "deleted sent direct message:", direct_message.id
