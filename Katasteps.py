import string
class NegativesNotAllowed(Exception):
    pass

def add(number_str):
    if number_str == "":
        return 0
     

    value = 0
    negatives = ""
    new_delimeter = ","

    if number_str[:2] == "//":
        new_delimeter = number_str[2] #Making the new delimeter by the format given.
        number_str = number_str[4:]

    number_str = number_str.replace("\n", new_delimeter) #Replacing newline with the new delimeter which I split.

    for n in number_str.split(new_delimeter):

        if n == "":
            n = 0

        if int(n) < 0:
            negatives += str(n) + ","

        if int(n) > 1000:
            n = "0"

        
        value += int(n)

    if negatives != "":
        raise NegativesNotAllowed("Negatives not allowed: {}".format(negatives[0:-1]))
    return value

add("1,\n2")
