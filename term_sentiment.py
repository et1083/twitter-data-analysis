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
    class sentiment_scores:
        def __init__(self, mood, count):
		self.mood = mood
		self.count = count	
    lines(sent_file)
    lines(tweet_file)
    
    afinnfile = open("AFINN-111.txt")
    
    scores = {} # initialize an empty dictionary
    
    my_scores = {}  #initializes second dictionary for the words not in AFINN
    
    for line in afinnfile:
	# the file is tab delimited "\t" means tab character
        term, score = line.split("\t") 
        scores[term] = sentiment_scores(float(score), 1) # convert score to an float
        
    #open output.txt and put it new_tweet_file
    new_tweet_file = open("output.txt")	
  
#for loop for each line(tweet) in new_tweet_file
    for line in new_tweet_file:
        tweet = json.loads(line)   #this makes a json type thing named tweets
        if 'text' in tweet:	   #looks for the key 'text' in the tweets file 	
                                   #'text' points toward the text of the tweet          
            #print('mytweet ' + tweet['text'].encode('ascii', 'ignore'))	  
            #prints mytweet then the text associated with the 'text' key  
            #.encode makes the unicode work

            #one_tweet holds 1 tweet at a time
            one_tweet = tweet['text'].encode('ascii', 'ignore')   
            
            words = one_tweet.split()    #this will break the tweet into words    
            mood = 0
            for word in words:    #scores each word in the tweet and adds it up
		if word in scores:  
                    #print word
                    mood = mood + scores[word].mood
                
	    for word in words:
	    	if word not in scores:
		    if word not in my_scores:
		        my_scores[word]=sentiment_scores(float(mood), 1)     
		
		    else:
		        my_scores[word].mood= float((my_scores[word].count*my_scores[word].mood+mood)/(my_scores[word].count+1))
			my_scores[word].count +=1
	    	
		
	
    for x in my_scores:
        print x, '  ' , my_scores[x].mood #, 'count',  my_scores[x].count	
   
if __name__ == '__main__':
    main()
