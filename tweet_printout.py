import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    hw()
    lines(sent_file)
    lines(tweet_file)
    
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    my_scores = {}  #initializes second dictionary for the words not in AFINN
    for line in afinnfile:
# the file is tab delimited "\t" means tab chracter
        term, score = line.split("\t") 
        scores[term] = int(score) # convert score to an integer

 #open output.txt and put it new_tweet_file
    new_tweet_file = open("US_tweets.txt")	
      
#for loop for each line(tweet) in new_tweet_file
    for line in new_tweet_file:
    	
        tweet = json.loads(line)   #this makes a json type thing named tweets
        if 'lang' in tweet:
	    if 'text' in tweet:	   #looks for the key 'text' in the tweets file 	
                                    #'text' points toward the text of the tweet          
                print(tweet['text'].encode('ascii', 'ignore'))	  
            #prints mytweet then the text associated with the 'text' key  
            #.encode makes the unicode work
            
            #one_tweet holds 1 tweet at a time
                one_tweet = tweet['text'].encode('ascii', 'ignore')   
            
                words = one_tweet.split()    #this will break the tweet into words    
         

if __name__ == '__main__':
    main()
