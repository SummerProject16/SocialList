'''
@file : imdbCheck.py
@author (A) : Madhu Kumar Dadi.
@project : Social List



This work is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License. To view a copy of this license,
visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

def checkStringinMovies(string):
    file = open("../imdbMovies.txt")
    #reading each line from the file 
    data = file.readlines()
    #checking if the line matches with the given string,return true or false 
    for x in data:
        if x.lower().replace("\n","") == string.lower():
            return True
    return False
