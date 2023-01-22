#!/usr/bin/python

import tweepy
import itertools

# item limits to keep
user_timeline_limit = 20
favorites_limit = 3
direct_messages_limit = 3
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

API = tweepy.API(auth)

user_timeline = API.user_timeline()
for status in itertools.islice(user_timeline, user_timeline_limit, None):
	API.destroy_status(status.id)
	print("deleted status:", status.id)

favorites = API.get_favorites()
for status in itertools.islice(favorites, favorites_limit, None):
	API.destroy_favorite(status.id)
	print("deleted favorite:", status.id)

direct_messages = API.get_direct_messages()
for direct_message in itertools.islice(direct_messages, direct_messages_limit, None):
	API.destroy_direct_message(direct_message.id)
	print("deleted direct message:", direct_message.id)

blocks = API.get_blocks()
for block in itertools.islice(blocks, blocks_limit, None):
	API.destroy_block(block.id)
	print("deleted block:", block.id)

saved_searches = API.get_saved_searches()
for saved_search in itertools.islice(saved_searches, saved_searches_limit, None):
	API.destroy_saved_search(saved_search.id)
	print("deleted saved search:", saved_search.id)
