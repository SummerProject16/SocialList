'''
@file : checkTweets.py
@author (A) : Madhu Kumar Dadi.
@project : Social List
@function :
	str2num(string) :   converts a pure number string into a number
		@string :   number in words
		return :    number in decimal
@function :
	cnvtwordstr2numstr(string) :    converts a string containing number in words to the string with numbers in decimal
		@string :   string containing number in words
		return :    string containing number in decimal
@function :
	cnvtnum2str(string) :   converts a string containing number in decimal to string with numbers in words
		@string :   string containing number in decimal
		return :    string containing number in words
@function :
	words2num(string) : converts a string containing mixed numbers in decimal and also words to pure decimal numbered strings
		@string :   string to be parsed
		return :    string containing numbers in pure decimals
@Licence :
	This work is licensed under the
	Creative Commons Attribution-NonCommercial-ShareAlike 4.0
	International License. To view a copy of this license,
	visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import re
import num2words

wordinnum = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
             'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
             'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
             'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
             'nineteen': 19, 'twenty': 20,
             'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
             'seventy': 70, 'eighty': 80, 'ninety': 90,
             'hundred': 100, 'hundreds': 100,
             'thousand': 1000, 'thousands': 1000,
             'lakh': 100000, 'lakhs': 100000,
             'lac': 100000, 'lacs': 100000,
             'million': 1000000, 'millions': 1000000,
             'crore': 10000000, 'crores': 10000000,
             'billion': 1000000000, 'billions': 1000000000,
             'trillion': 1000000000000, 'trillions': 1000000000000,
             }


def str2num(string="zero"):
	try:
		split_string = string.lower().split()
		cleaned_string = []
		for x in split_string:
			#Checking for strings only in wordinnum list
			if x == "and" or x == "&":
				x = "zero"
			if x in wordinnum:
				if 's' == x[len(x) - 1]:
					x = x[:-1]
					#removing trailing s in number words like 's' in 'lacs'
			else:
				raise
			if x == "lakh":
				x = "lac"
			cleaned_string.append(x)

		value = 0
		max_mark = 0

		'''
		this goes on a recursive basis, if there is a trillion in the string
		all the words before trillion are computed using the same function recursively
		then multiplied by trillion. Same goes for all the marks below.
		'''

		trillion_mark = len(cleaned_string)-1 - cleaned_string[::-1].index('trillion') \
			if 'trillion' in cleaned_string else -1
		if max_mark < trillion_mark: max_mark = trillion_mark
		billion_mark = len(cleaned_string)-1 - cleaned_string[::-1].index('billion') \
			if 'billion' in cleaned_string[max_mark + 1:] else -1
		if max_mark < billion_mark: max_mark = billion_mark
		crore_mark = len(cleaned_string)-1 - cleaned_string[::-1].index('crore') \
			if 'crore' in cleaned_string[max_mark + 1:] else -1
		if max_mark < crore_mark: max_mark = crore_mark
		million_mark = len(cleaned_string)-1 - cleaned_string[::-1].index('million') \
			if 'million' in cleaned_string[max_mark + 1:] else -1
		if max_mark < million_mark: max_mark = million_mark
		lac_mark = len(cleaned_string)-1 - cleaned_string[::-1].index('lac') \
			if 'lac' in cleaned_string[max_mark + 1:] else -1
		if max_mark < lac_mark: max_mark = lac_mark
		thousand_mark = len(cleaned_string)-1 - cleaned_string[::-1].index('thousand') \
			if 'thousand' in cleaned_string[max_mark + 1:] else -1
		if max_mark < thousand_mark: max_mark = thousand_mark
		hundred_mark = len(cleaned_string)-1 - cleaned_string[::-1].index('hundred') \
			if 'hundred' in cleaned_string[max_mark + 1:] else -1

		if trillion_mark != -1:
			value += str2num(" ".join(cleaned_string[:trillion_mark]))*1000000000000
			#Computing words before trillion and multiplying by trillion
			value += str2num(" ".join(cleaned_string[trillion_mark+1:]))
			#Adding value of words after trillion
			#Similarly for all
		else:
			if billion_mark != -1:
				value += str2num(" ".join(cleaned_string[:billion_mark]))*1000000000
				value += str2num(" ".join(cleaned_string[billion_mark+1:]))
			else:
				if crore_mark != -1:
					value += str2num(" ".join(cleaned_string[:crore_mark]))*10000000
					value += str2num(" ".join(cleaned_string[crore_mark+1:]))
				else:
					if million_mark != -1:
						value += str2num(" ".join(cleaned_string[:million_mark]))*1000000
						value += str2num(" ".join(cleaned_string[million_mark+1:]))
					else:
						if lac_mark != -1:
							value += str2num(" ".join(cleaned_string[:lac_mark]))*100000
							value += str2num(" ".join(cleaned_string[lac_mark+1:]))
						else:
							if thousand_mark != -1:
								value += str2num(" ".join(cleaned_string[:thousand_mark]))*1000
								value += str2num(" ".join(cleaned_string[thousand_mark+1:]))
							else:
								if hundred_mark != -1:
									value += str2num(" ".join(cleaned_string[:hundred_mark]))*100
									value += str2num(" ".join(cleaned_string[hundred_mark+1:]))
								else:
									for x in cleaned_string:
										value += wordinnum[x]
		return value
	except:
		print "String " + string + " is not valid for int conversion"
		exit(-1)


def cnvtwordstr2numstr(string=""):
	#coverts a string containing numbers as words to numbered string
	if len(string) == 0: return ""
	start_index = 0
	string_split = string.lower().split()
	for x in string_split:
		if x not in wordinnum:
			start_index += 1 #checks where the numbered words start
		else:
			break
	if start_index >= len(string_split): return string
	end_index = start_index
	for index in xrange(start_index+1,len(string_split)):
		if string_split[index] in wordinnum:
			end_index += 1 # checks where the numbered words end
		elif string_split[index] == "and" or string_split[index] == "&":
			if index+1 < len(string_split) and string_split[index+1] in wordinnum:
				end_index += 1
		else:
			break
	return " ".join(string_split[:start_index]) + " " + \
		str(str2num(" ".join(string_split[start_index:end_index+1]))) + " "\
		+ cnvtwordstr2numstr(" ".join(string_split[end_index+1:]))


def cnvtnum2str(string="Test case 1"):
	#converts numbers in string to words
	split_string = string.split()
	final_string =[]
	for x in split_string:
		if re.match("\d+\s", x):
			x = num2words.num2words(int(x))
			x = x.replace("-", " ").replace(",", "")
		final_string.append(x)
	return " ".join(final_string)


def words2num(string="Enter some number like 2 thousand 30"):
	'''
	First converts the string with numbers and numbered words to strings with numbers as pure words.
	Then converts the string thus obtained into a string with only numbers in decimal form
	:param string: String witth numbers in decimal and as words
	:return: String with numbers in decimal
	'''
	return cnvtwordstr2numstr(cnvtnum2str(string))


def test():
	print str2num("one thousand five hundred and forty six")
	print cnvtwordstr2numstr("I have One lac eighty five thousand ninety six rupees")
	print words2num("Hello to you and 1 billion 2 hundred & 10 million and more people")

#test() #If you want to test if its working remove the ash at the beginning of this line and run