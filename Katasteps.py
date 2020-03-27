
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

    for num in number_str.split(new_delimeter):
        if num == "": #If given a double delimeter f.x. "1,/n2" will end as "1,,2"
            num = 0

        if int(num) < 0:
            negatives += str(num) + ","

        if int(num) > 1000:
            num = "0"

        value += int(num) #All allowed numbers added together.

    if negatives != "":
        raise NegativesNotAllowed("Negatives not allowed: {}".format(negatives[0:-1]))

    return value

