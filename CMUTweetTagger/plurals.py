'''
@file : plurals.py
@author (A) : Madhu Sai Ravada
@project : Social List

@function :
    :returns 1 if the hastag contains plural noun else returns 0

This work is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License. To view a copy of this license,
visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import stemming.porter2
import inflect

plural = inflect.engine()

def containspluralNouns(segmented_hashtag,pos_tags):
    flag = 0
    segmented_hashtag = segmented_hashtag.split()
    for i in xrange(len(pos_tags)):
        if(pos_tags[i]=='N'):
            # converts the stemmed Noun to its plural form and compares to original word
            if(plural.plural_noun(stemming.porter2.stem(segmented_hashtag[i])) == segmented_hashtag[i]):
                flag=1
    if(flag):
        return 1
    else:
        return 0

def test():
    print containspluralNouns("gift ideas",['A','N'])
    print containspluralNouns("perked girl",['N','N'])

#test() #remove ash at begining of this line to test