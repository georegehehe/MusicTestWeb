aasdf = ["a","1" ,"b","c","2"]
for items in aasdf:
    try:
        print int(items)
    except ValueError:
        print items + " is not a number"


