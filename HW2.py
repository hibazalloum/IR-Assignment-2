movies = open('movies.txt', encoding="utf-8")

termDict = {}

with open('movies.txt', 'r') as movie:
    for line in movie:
        words = line.replace('.', '').replace('\'', '').replace(',', '').lower().split()
        for word in words:
            if word not in termDict:
                termDict[word] = 1
            else:
                termDict[word] = termDict[word] + 1


def k_Gram(k, text):
    klist = {}
    if k > 1:
        doller = '$' * (k-1)
        text = doller + text + doller

    for i in range(len(text) - (k - 1) ):
        klist.keys(text)
    return klist

value = []
for i in range(k_Gram(termDict,termDict)):
    value.append(len(k_Gram(termDict)))
'''
for i in range(4):
    mydict = dict.fromkeys(k_Gram(i+1, termDict))

print(mydict)
'''


def jaccard(value, termDict):
    intersection = len(list(set(value).intersection(termDict)))
    union = (len(value) + len(termDict)) - intersection
    return float(intersection) / union



def edit_distance(string1, string2):


    if len(string1) > len(string2):
        difference = len(string1) - len(string2)
        string1=[:difference]

    elif len(string2) > len(string1):
        difference = len(string2) - len(string1)
        string2[:difference]

    else:
        difference = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            difference += 1

    return difference

"""
for i in range(4):
    print (k_Gram(i+1,"termDict"))

KList = k_Gram(3,"termDict")
for kGram in iter(KList):
    print ('"' + kGram + '"')
 """
"""
valuegrams =[]
for i in range(k_Gram(k=termDict)):
    valuegrams.append([i])
"""