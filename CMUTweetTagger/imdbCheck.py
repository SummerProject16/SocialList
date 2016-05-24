def checkStringinMovies(string):
    file = open("../imdbMovies.txt")
    data = file.readlines()
    for x in data:
        if x.lower().replace("\n","") == string.lower():
            return True
    return False