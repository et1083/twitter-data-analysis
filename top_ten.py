import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw()
    
    #lines(tweet_file)
    hashtag = {}
    
    
    #for loop for each line(tweet) in tweet_file
    for line in tweet_file:
        
	tweet = json.loads(line)   #this makes a json type thing named tweets
        if 'entities' in tweet:
	        
	    all_hashtag = tweet['entities']['hashtags'] 
	    
	    for tag in all_hashtag:
	       y = str(tag['text'].encode('ascii', 'ignore'))  
	       
	       if y in hashtag:
	           hashtag[y] += 1
               else:
	           hashtag[y] = 1
	       
            
    mount = 0 
    for tag in sorted(hashtag, key=hashtag.get, reverse=True):
        
	if mount < 11:
	    print tag, hashtag[tag]  
	    mount +=1     
			
   
if __name__ == '__main__':
    main()
