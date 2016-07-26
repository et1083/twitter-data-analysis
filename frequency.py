
import sys
import json
from pprint import pprint
def hw():
    print "hello world!"
def main():
    hw()
    
    wordcount = {}
    #open output.txt and put it new_tweet_file
    new_tweet_file = open("output.txt") 
    #pull the text of the tweets out
    for line in new_tweet_file:
        tweet = json.loads(line)   #this makes a json type thing named tweets
        if 'text' in tweet:    #looks for the key 'text' in the tweets file     
                                   #'text' points toward the text of the tweet          
            # print('mytweet ' + tweet['text'].encode('ascii', 'ignore'))     
            #prints mytweet then the text associated with the 'text' key  
            #.encode makes the unicode work
            #one_tweet holds 1 tweet at a time
            one_tweet = tweet['text'].encode('ascii', 'ignore')   
            
            words = one_tweet.split()    #this will break the tweet into words 
    #for loop take the first word and count it through the file
    
  
