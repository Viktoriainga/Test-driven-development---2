class NegativesNotAllowed(Exception):
    pass

def add(number_str):
    if number_str == "":
        return 0

    value = 0
    negatives = ""
    for i in number_str.split(","):
        i= i.strip().split("\n")    
        for n in i:
            if int(n) < 0:
                negatives += str(n) + ","

            if int(n) > 1000:
                n = "0"
                
            value += int(n)
    
    if negatives != "":
        raise NegativesNotAllowed("Negatives not allowed: {}".format(negatives[0:-1]))
    return value
