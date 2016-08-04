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
    
    
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}                 
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    state_mood = {}
    for line in afinnfile:
# the file is tab delimited "\t" means tab chracter
        term, score = line.split("\t") 
        scores[term] = int(score) # convert score to an integer

    for x in states:
        state_mood[x] = float(0)    
    
 #open output.txt and put it new_tweet_file
    new_tweet_file = open("US_tweets.txt")	
  
#for loop for each line(tweet) in new_tweet_file
    for line in new_tweet_file:
        tweet = json.loads(line)   
        
       
	if 'user' in tweet:                                 
            if 'location' in tweet['user']:
		if tweet['user']['location'] is not None:
		    locale = tweet['user']['location'].encode('UTF8')
		        
		    places = locale.split() 
                    
		    for term in places:
			    
		        if term in states:
			    if 'text' in tweet:
			        one_tweet = tweet['text'].encode('ascii', 'ignore')   
              
                                words = one_tweet.split()    #this will break the tweet into words    
                                mood = 0
                                for word in words:    #scores each word in the tweet and adds it up
                                    if word in scores:  
                          
                                        mood = mood + scores[word]
			    
			   
                                state_mood[term] = mood                               
				
                                
   
   
    
    count = 0
    for term in sorted(state_mood, key=state_mood.get, reverse=True):
        
	if count < 1:
            print 'the happiest state is', term, 'with a mood of',  state_mood[term] 
	    count +=1  
    

if __name__ == '__main__':
    main()
