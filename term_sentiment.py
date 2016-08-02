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
        def _init_(self, mood, count):
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
        scores[term] = sentiment_scores(float(score), 1) # convert score to an integer
        
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
		        my_scores[word]=sentiment_scores(mood, 1)     
		
		    else:
		        my_scores[word].mood= (my_scores[word].count*my_scores[word].mood+mood)/(my_scores[word].count+1)
			my_scores[word].count +=1
	    	
		
		
		
                # averaging moodscore of word already in my_scores
                elif word in my_scores and mood!=0:
		    mood = (my_scores[word].count*my_scores[word].mood+mood)/(my_scores[word].count+1)
		    count = word.count+1
		    my_scores = (word, mood, count)
		
		#else statement taking the words without a mood associated
                #with them and averaging the score of the surrounding
		#words and giving that score to the unknown word
		else:
                    #print word + ' ' + str(mood) 
                    my_scores = (word, mood, count+1) 
	    #print one_tweet + ': mood ' + str(mood)
            
            #prints the mood score of each tweet to the screen
            #print str(mood) 

if __name__ == '__main__':
    main()
