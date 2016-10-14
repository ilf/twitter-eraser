Digital Eraser
==============

Digital Eraser deletes Twitter account data. It is intended to be run via cron.

Name
----

Radiergummi is German for "eraser".

See [Delete: The Virtue of Forgetting in the Digital Age](http://press.princeton.edu/titles/9436.html) for more background information.

Description
-----------

Twitter is a (near) real time medium. It doesn't need to keep an archive of
everything you have ever done.

Digital Eraser can delete these things:

- status messages, including retweets
- favorites
- direct messages: sent and received
- blocks
- saved searches

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

On first run, you will probably see a few errors. These are Twitters fault:

- Twitter error response: status code = 503
- No status found with that ID.

Twitters "Tweet Count" of a profile is not accurate. It seems to be about 20
Tweets over the actual count. Count them manually, and you will see Twitter
Eraser is correct, Twitter not.

License
-------

[Beerware](https://en.wikipedia.org/wiki/Beerware)
