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
    klist = []
    if k > 1:
        doller = '$' * (k-1)
        text = doller + text + doller

    for i in range(len(text) - (k - 1) ):
        klist.append(text[i:i+k])
    return klist


for i in range(4):
    mydict = dict.fromkeys(k_Gram(i+1, termDict))

print(mydict)

"""
def jaccard(mydict, termdict):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union
"""
"""
for i in range(4):
    print (k_Gram(i+1,"termDict"))

KList = k_Gram(3,"termDict")
for kGram in iter(KList):
    print ('"' + kGram + '"')
 """