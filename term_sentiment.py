×Close
Interested in translating the app in your language ? Click here
×Close
Found a bug in the app ?
Click here to report it on the community
 Logo
File
Open
Favorites
Options

tweet_sentiment_tennant.py
 Saved
 

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary

    for line in afinnfile:
        term, score = line.split("\t") # the file is tab delimited "\t" means tab chracter

    scores[term] = int(score) # convert score to an integer

    #print scores.items()  #print every (term, score) pair in the dictionary
    #with open('problem_1_submission.txt') as tweet_file:

    new_tweet_file = open("output.txt")    #open problem_1-submission and put it new_tweet_file

    for line in new_tweet_file:      #for loop for each line in new_tweet_file
        tweet = json.loads(line)     #this makes a json type thing named tweets
        if 'text' in tweet:      #looks for the word text in the tweets file    
           # print('mytweet ' + tweet['text'].encode('ascii', 'ignore'))      #prints mytweet then the text associated with the 'text' key  .encode 

makes the unicode work
            one_tweet = tweet['text'].encode('ascii', 'ignore')
  
