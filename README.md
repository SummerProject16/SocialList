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
      * Length of Hashtag checker : testFile1.py
      * Number of Words checker : testFile2.py
      * Week Name checker : testFile4.py
      * Parsts of Speech Counter : testFile5.py
      * Noun Counter : testFile6.py
      * Adjective Counter : testFile7.py
      * Verb Counter : testFile8.py
      * Adverb Counter : testFile9.py
      * Pronoun Counter : testFile10.py
      * Pos Tag Entropy Finder : testFile11.py
      * Non-English to English Words Ratio : testFile12.py
      * Search Web for popularity and Precision : testFile14.py
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

  * ## **Work Flow**

    when the Main File is run first it segments the hashtags into words using the wordsegment packae then it converts the hashtags in the text file provided into a decimal numbered strings
    using the `str2num` package. Then the list thus obtained is passed through the CMUTweetTagger script for pos tagging and the list thus obtained is passed to all features listed below one by one, i.e
      * testFile1   -   counts character length of the unsegmented hashtag
      * testFile2   -   counts number of words in the hashtag
      * testFile4   -   checks if hashtag contains any week name
      * testFile5   -   counts # of prepositions and conjunctions in hashtag
      * testFile6   -   counts # of Nouns in hashtag
      * testFile7   -   counts # of Adjectives in hashtag
      * testFile8   -   counts # of Verbs in hashtag
      * testFile9   -   counts # of Adverbs in hashtag
      * testFile10  -   counts # of Pronouns in hashtag
      * testFile11  -   calculates the pos tag entropy of the hashtag
      * testFile12  -   calculates the ratio of non-english words to english words
      * checkTweets -   checks the tweets containing the hashtag in the tweetsfile provided and checks if they contain a common noun in number or any url corresponding to a picture or hashtag related one.
      * Category    -   checks if the hashtag matches available categories
      * plurals     -   checks if the hashtag contains a plural common noun
      * type        -   type of socialList from available data

     the data from this is stored in a file provided in csv format

    when the GoogleSearch.py is run it passes the hashtag to testFil14.py which in turn calls the searchWeb.py and gets urls
    obtained after searching the hashtag in google, the list of urls are scraped and the popularity of the hashtag is 1 if
    atleast five of the urls contain the nouns in hashtag else popularity is 0, then the precision is obtained by searching the
    title and url for stemmed hashtag. These values are also stored in csv format in the file provided.

    When combineArff.py is run it combines the two files obtained above as
    all the features obtained in first csv except type, then values in second file and at last type.
    Thus the final CSV is obtained.