Digital Eraser
==============

Digital Eraser deletes Twitter account data. It is intended to be run via cron.

Name
----

Radiergummi is german for "eraser".

Google "[Digitaler Radiergummi](https://www.google.com/search?q=%22Digitaler+Radiergummi%22)" for background info.

Description
-----------

Twitter is a (near) real time medium. It doesn't need to keep an archive of
everything I have ever done on there.

Especially since I have my own archive via mail and client logs.

Digital Eraser can delete these things:

- status messages
- retweets
- favorites
- direct messages: sent and received
- blocks
- saved searches
- lists

It is designed to be run via cron automatically and regularly.

Warning
-------

This will permanently delete content of your Twitter-account.

Inspiration
-----------

Dave Jeffery: [delete_all_tweets.py](https://gist.github.com/113241)

Requirements
------------

[Tweepy](https://github.com/tweepy/tweepy/) - A Twitter library for Python

Configuration
-------------

Get OAuth key and secret for application and account at:
[dev.twitter.com/apps](https://dev.twitter.com/apps)

Change the limits-variables to whatever value you want to keep.

Notes
-----

The Twitter API seems to have a hard time with old content. An initial deletion
to the specified limits will take a while.

You will probably see a few tweepy.error.TweepError. These are Twitters fault:

- Twitter error response: status code = 503
- No status found with that ID.

License
-------

[Beerware](https://en.wikipedia.org/wiki/Beerware)
