#!/usr/bin/python

import tweepy
import itertools

# item limits to keep
user_timeline_limit = 20
favorites_limit = 3
direct_messages_limit = 3
sent_direct_messages_limit = 3
blocks_limit = 3
saved_searches_limit = 1

# OAuth application
consumer_key = "get this from https://apps.twitter.com/"
consumer_secret = "get this from https://apps.twitter.com/"
# OAuth account
access_token = "get this from https://apps.twitter.com/"
access_token_secret = "get this from https://apps.twitter.com/"

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_timeline = tweepy.Cursor(api.user_timeline).items()
for status in itertools.islice(user_timeline, user_timeline_limit, None):
	api.destroy_status(status.id)
	print("deleted status:", status.id)

favorites = tweepy.Cursor(api.favorites).items()
for status in itertools.islice(favorites, favorites_limit, None):
	api.destroy_favorite(status.id)
	print("deleted favorite:", status.id)

direct_messages = tweepy.Cursor(api.direct_messages).items()
for direct_message in itertools.islice(direct_messages, direct_messages_limit, None):
	api.destroy_direct_message(direct_message.id)
	print("deleted direct message:", direct_message.id)

sent_direct_messages = tweepy.Cursor(api.sent_direct_messages).items()
for direct_message in itertools.islice(sent_direct_messages, sent_direct_messages_limit, None):
	api.destroy_direct_message(direct_message.id)
	print("deleted sent direct message:", direct_message.id)

blocks = tweepy.Cursor(api.blocks).items()
for block in itertools.islice(blocks, blocks_limit, None):
	api.destroy_block(block.id)
	print("deleted block:", block.id)

saved_searches = api.saved_searches()
for saved_search in itertools.islice(saved_searches, saved_searches_limit, None):
	api.destroy_saved_search(saved_search.id)
	print("deleted saved search:", saved_search.id)
