import random

britDic = {}
amerDic = {}
spellingUKUS = [["tre", "ter"], ["ogue", "og"], ["our", "or"], ["ise", "ize"], ["isa", "iza"], ["yse","yze"], ["xion", "ction"], ["ce", "se"], ["lled", "led"]]
inSelect = 0

def addToDic(srcLang, desLang, inSrc, inDes):
    if(inSrc in srcLang.keys()):
        if(inDes in srcLang[inSrc]):
            print "already in there"
        else:
            srcLang[inSrc].append(inDes)
            if(inDes in desLang):
                desLang[inDes].append(inSrc)
            else:
                desLang[inDes] = [inSrc]
    else:
        srcLang[inSrc] = [inDes]
        desLang[inDes] = [inSrc]

def bulkAdd(srcLang, desLang):
    inFile = open("UK-US.csv", "r")
    line = inFile.readline()
    while line:
        translation = line.split(",")
        UK = translation[0]
        US = translation[1].split("\n")[0]
        addToDic(srcLang, desLang, UK, US)
        line = inFile.readline()

def modifySpelling(toLang, word):
    if(toLang == "American"):
        for sym in spellingUKUS:
            if sym[0] in word:
                word = word.replace(sym[0], sym[1])
    if(toLang == "British"):
        for sym in spellingUKUS:
            if sym[1] in word:
                word = word.replace(sym[1], sym[0])
    return word


def translateSentence(srcLang, toLang, sentence):
    for word in inWords:
            if(word in srcLang.keys()):
                if len(srcLang[word]) > 1:
                    outWord = srcLang[word][random.randint(0,(len(srcLang[word]) - 1))]
                else:
                    outWord = srcLang[word][0]
            else:
                outWord = modifySpelling(toLang, word)
            
            print outWord,
    print "\n\n"


while(inSelect != 7):
    inSelect = raw_input("What would you like to do?\n(1) add British word\n(2) add American word\n(3) bulk add British words\n(4) bulk add American words\n(5) translate British to American\n(6) translate American to British\n(7) Quit\n")
# Add UK word
    if(inSelect == "1"):
        inBrit = raw_input("Specify British word\n")
        inAmer = raw_input("Specify American translation\n")
        addToDic(britDic, amerDic, inBrit, inAmer)
# Add American word
    elif(inSelect == "2"):
        inAmer = raw_input("Specify American word\n")
        inBrit = raw_input("Specify British translation\n")
        addToDic(amerDic, britDic, inAmer, inBrit)
# Bulk add UK words
    elif(inSelect == "3"):
        bulkAdd(britDic, amerDic)
# Bulk add American words
    elif(inSelect == "4"):
        bulkAdd(amerDic, britDic)
# Translate UK-US
    elif(inSelect == "5"):
        inText = raw_input("Please enter your sentence to translate:\n")
        inWords = inText.split(" ")
        translateSentence(britDic, "American", inWords)
# Translate UK-US
    elif(inSelect == "6"):
        inText = raw_input("Please enter your sentence to translate:\n")
        inWords = inText.split(" ")
        translateSentence(amerDic, "British", inWords)
    elif(inSelect == "7"):
        break
    else:
        print "Not valid, try again"