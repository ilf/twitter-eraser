#!/usr/bin/python

# source: https://gist.github.com/113241
# needs: http://packages.python.org/tweepy/html/

import tweepy
import itertools

# OAuth Application settings
consumer_key = 'edit.this'
consumer_secret = 'edit.this'
# OAuth account access token
key = 'edit.this'
secret = 'edit.this'

# thresholds to keep
user_timeline_threshold = 15
retweeted_by_me_threshold = 3
favorites_threshold = 3
direct_messages_threshold = 2
sent_direct_messages_threshold = 2

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
print "authenticated user:", api.me().screen_name

print "deleting statuses, keeping", user_timeline_threshold
user_timeline = tweepy.Cursor(api.user_timeline).items()
for status in itertools.islice(user_timeline, user_timeline_threshold, None):
	api.destroy_status(status.id)
	print "deleted:", status.id

print "deleting retweets, keeping", retweeted_by_me_threshold
retweeted_by_me = tweepy.Cursor(api.retweeted_by_me).items()
for status in itertools.islice(retweeted_by_me, retweeted_by_me_threshold, None):
	api.destroy_status(status.id)
	print "deleted:", status.id

print "deleting favorites, keeping", favorites_threshold
favorites = tweepy.Cursor(api.favorites).items()
for status in itertools.islice(favorites, favorites_threshold, None):
	api.destroy_favorite(status.id)
	print "deleted:", status.id

print "deleting direct messages, keeping", direct_messages_threshold
direct_messages = tweepy.Cursor(api.direct_messages).items()
for direct_message in itertools.islice(direct_messages, direct_messages_threshold, None):
	api.destroy_direct_message(direct_message.id)
	print "deleted:", direct_message.id

print "deleting sent direct messages, keeping", sent_direct_messages_threshold
sent_direct_messages = tweepy.Cursor(api.sent_direct_messages).items()
for direct_message in itertools.islice(sent_direct_messages, sent_direct_messages_threshold, None):
	api.destroy_direct_message(direct_message.id)
	print "deleted:", direct_message.id
