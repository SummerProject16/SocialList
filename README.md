# _Social Lists_

## **_Info_**  
  *	### **Requirements**
  
  		num2words
        pyenchant
        stemming
        wordsegment
        CMUTweetTagger
		inflect

  *	### **Files**  

  	  * Arff Generator : [CMUTweetTagger/SocialList.py](http://github.com/SummerProject16/project/blob/master/CMUTweetTagger/socialList.py)  
      * Precision Generator : [CMUTweetTagger/GoogleSearch.py](http://github.com/SummerProject16/project/blob/master/CMUTweetTagger/GoogleSearch.py)  
      * Feature Files : testFile[i].py where i is feature number  
      * String to Number converter : [CMUTweetTagger/tweets/str2num/str2num.py](http://github.com/SummerProject16/project/blob/master/CMUTweetTagger/tweets/str2num/str2num.py)  
      * Getting Tweets and Urls related to a hashtag : [CMUTweetTagger/hashtag.py](http://github.com/SummerProject16/project/blob/master/CMUTweetTagger/hashtag.py)  
      * Searching Google for a HashTag popularity : [CMUTweetTagger/searchWeb.py](http://github.com/SummerProject16/project/blob/master/CMUTweetTagger/searchWeb.py)  
      * Checking for K Lists and Urls in Tweets : [CMUTweetTagger/TweetCheck.py](http://github.com/SummerProject16/project/blob/master/CMUTweetTagger/TweetCheck.py)
      * Checking for Categories in Tweets : [CMUTweetTagger/Category.py](http://github.com/SummerProject16/project/blob/master/CMUTweetTagger/Category.py)
      * Checking for presence of plural Common Nouns in Tweets : [CMUTweetTagger/plurals.py](http://github.com/SummerProject16/project/blob/master/CMUTweetTagger/plurals.py)

  * ## **Example Commands**
        
        First of all commands must be run in virtual environment  

        After generating there arff files they must be merged and attributes must be noted.
      * Run Main File : `python socialList.py finallist.txt finaltype.txt finallist.arff`
      * Create a websearch file : `python GoogleSearch.py finallist.txt weblist.arff`
	  *	Joining both Arff files : `python combineArff.py finallist.arff weblist.arff socialList.arff`
