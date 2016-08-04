import sys
import json

from pprint import pprint

def hw():

    print "hello world!"


def main():
    tweet_file = open(sys.argv[1])
    hw()
    
    wordcount = {}     #initializes empty dictionary
    wordcount1 = {}    #initializes dictionary to add new words
    total = 1
    #open output.txt and put it new_tweet_file
    new_tweet_file = tweet_file	

    #pull the text of the tweets out
    for line in new_tweet_file:
        tweet = json.loads(line)   #this makes a json type thing named tweets
        if 'text' in tweet:	   #looks for the key 'text' in the tweets file 	
                                   #'text' points toward the text of the tweet          
            # print('mytweet ' + tweet['text'].encode('ascii', 'ignore'))	  
            #prints mytweet then the text associated with the 'text' key  
            #.encode makes the unicode work

            #one_tweet holds 1 tweet at a time
            
            one_tweet = tweet['text'].encode('ascii', 'ignore')   
              
            
            words = one_tweet.split()    #this will break the tweet into words 

    #for loop take the first word and count it through the file
         
	    
            for word in words:
                
                
                if word in wordcount: 
                    frequency = 0
                    frequency = 1 + wordcount[word]
                    wordcount[word] = 1.00*frequency/total
                    
                else:
                    wordcount[word] = 1.*1/total

                total = len(wordcount)
	
    

    for word in wordcount:
        print word,  '    ',     wordcount[word]
 
  
if __name__ == '__main__':
    main()
              
                
 
