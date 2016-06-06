#parts of speech tagger for social list
import CMUTweetTagger as cmu
from wordsegment import segment
from collections import Counter
file = open('../socialList.txt')
idiomsEx = file.readlines()
arr = []
i = 0

idioms = []

strlength = 0
word = 0
for x in idiomsEx:
    a = segment(x.replace("\n",""))
    strlength += len(x.replace("\n",""))
    idioms.append(" ".join(a))
    word = word+len(a)

postags = cmu.runtagger_parse(idioms)

count = len(postags)
nouns = 0
pronouns = 0
conjunctions = 0
interjections = 0
verbs = 0
adjectives = 0
adverbs = 0
prepositions = 0

for x in postags:
    tagscount = Counter(x)
    nouns += tagscount['N']+tagscount['^']
    pronouns += tagscount['O']
    conjunctions += tagscount['&']
    interjections += tagscount['!']
    verbs += tagscount['V']
    adjectives += tagscount['A']
    adverbs += tagscount['R']
    prepositions += tagscount['P']

print "Avg no. of Nouns: "+str("%.4f"%(float(nouns)/count))
print "Avg no. of Pronouns: "+str("%.4f"%(float(pronouns)/count))
print "Avg no. of Conjuctions: "+str("%.4f"%(float(conjunctions)/count))
print "Avg no. of Interjections: "+str("%.4f"%(float(interjections)/count))
print "Avg no. of Verbs: "+str("%.4f"%(float(verbs)/count))
print "Avg no. of Adjectives: "+str("%.4f"%(float(adjectives)/count))
print "Avg no. of Adverbs: "+str("%.4f"%(float(adverbs)/count))
print "Avg no. of Prepositions: "+str("%.4f"%(float(prepositions)/count))
print "Avg length of string: "+str("%.4f"%(float(strlength)/count))
print "Avg length of word: "+str("%.4f"%(float(word)/count))
