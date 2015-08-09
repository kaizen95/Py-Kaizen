# -*- coding: utf-8 -*-
import tweepy, time, os, sys, urllib

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

line = "호갱아 자고 잇냐!"
status = api.update_status(status=line)
#콘솔모드 status = api.update_status(status=unicode("는 하필 잘 때 끝낫네 ㅍㅅㅍ....",'cp949'))
