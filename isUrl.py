
tldList = []
tldFile = open("tlds-alpha-by-domain.txt", 'r')
for line in tldFile:

    line = "." + line.replace('\n','')
    tldList.append(line)

tldFile.close()

def isUrl(input):

    if " " in input:
        return False
    else:

        if 'www.' in input:
            return True
        elif 'http://' in input:
            return True
        for tld in tldList:
            if tld in input:
                return True
            elif tld.lower() in input:
                return True

    return False
