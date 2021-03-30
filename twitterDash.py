#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import twitter
import json
import sys
import os
#This is the file I keep my API key information in
import t
import json

if __name__ == "__main__":
    api = twitter.Api(t.CONSUMER_KEY, t.CONSUMER_SECRET, t.ACCESS_TOKEN_KEY, t.ACCESS_TOKEN_SECRET)
    results = api.GetSearch(raw_query="q=%23Dog", count=5)
    json_results = []
    count = 1
    for x in results:
        print(f'This is the {count} Tweet')
        print(x)
        count +=1
    #print(json_results[0])
