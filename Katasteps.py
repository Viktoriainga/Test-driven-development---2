def add(number_str):
    if number_str == "":
        return 0

    value = 0

    for i in number_str.split(","):
        i= i.strip().split("\n")    
        for n in i:
            if int(n) > 1000:
                n = "0"
            value += int(n)

    return value