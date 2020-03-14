def add(number_str):
    if number_str == "":
        return 0

    value = 0

    for i in number_str.split(","):
        for n in i:
            value += int(n)

    return value