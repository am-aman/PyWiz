def sWAP(Sen):
    sEN = ""

    for x in Sen:
        if x.isupper():
            x=x.lower()
        else:
            x=x.upper()

        sEN += "".join(x)

    return sEN


Sen = input("go on : ")
print(sWAP(Sen))
