def checkStringinMovies(string):
    file = open("../imdbMovies.txt")
    #reading each line from the file 
    data = file.readlines()
    #checking if the line matches with the given string,return true or false 
    for x in data:
        if x.lower().replace("\n","") == string.lower():
            return True
    return False
