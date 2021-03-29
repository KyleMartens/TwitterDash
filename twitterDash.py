#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import twitter
import json
import sys
import os
import t


def get_tweets(api=None, screen_name=None):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=1)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=5
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            print("getting tweets before:", earliest_tweet)
            timeline += tweets

    return timeline


if __name__ == "__main__":
    api = twitter.Api(t.CONSUMER_KEY, t.CONSUMER_SECRET, t.ACCESS_TOKEN_KEY, t.ACCESS_TOKEN_SECRET)
    screen_name = 'JustinTrudeau'
    print(screen_name)
    timeline = get_tweets(api=api, screen_name=screen_name)

    with open('timeline.json', 'w+') as f:
        for tweet in timeline:
            f.write(json.dumps(tweet._json))
            f.write('\n')