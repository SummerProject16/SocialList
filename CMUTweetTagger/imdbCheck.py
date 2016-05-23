def checkStringinMovies(string):
    file = open("../imdbMovies.txt")
    data = file.readlines()
    for x in data:
        if x.lower().replace("\n","") in string.lower():
            print x
            return True
    return False