movies = open('movies.txt', encoding="utf-8")


def k_Gram(k, text):
    klist = []
    for i in range(len(text) - (k - 1) ):
        klist.append("$".join(text[i:i+k]))
    return klist


def jaccardCoefficient(lst1, lst2):
    list1= set(lst1)
    list2 = set(lst2)
    return float(len(list1.intersection(list2))/len(list1.union(list2)))


def edit_distance(term, query, x, y):
    distProb = [[0 for i in range(x+1)] for i in range(y+1)]
    for n in range(y+1):
        for m in range(x+1):
            if n == 0:
                distProb[n][m] = m
            elif term [n-1] == query[m-1]:
                distProb[n][m] = distProb[n-1][m-1]
            else:
                distProb[n][m]= 1 + min(distProb[n][m-1],distProb[n-1][m],distProb[n-1][m-1])
    return distProb[x][y]

jaccard = 0.1
jc =0
factor = 2
wd = {}
highjaccrd =[]


def search(q):
    sg = k_Gram(3,q)
    for k in sg:
        highjaccrd.append(kgramDict[k])
    for i in range(len(highjaccrd)):
        for j in highjaccrd[i]:
            high = termDict[j]
            jaccard = jaccardCoefficient(high,sg)
            if jaccard > jc:
                if j not in wd.keys():
                    wd[j] = jaccard
    print(wd)
    highJaccard = list(wd)
    final = []
    for word in highJaccard:
        distence = edit_distance(word,q, len(word),len(q))
        if distence < factor:
            final.append(word)
    print(final)


termDict = {}
kgramDict = {}

with open('movies.txt', 'r') as movie:
    for line in movie:
        words = line.replace('.', '').replace('\'', '').replace(',', '').lower().split()
        for word in words:
            g = k_Gram(3, word)
            for k_Gram in g:
                if k_Gram in kgramDict:
                    kgramDict[k_Gram].append(word)
                else:
                    kgramDict[k_Gram] = [word]
            if word not in termDict.keys():
                termDict[word] = g


query = input("input your query : ")
search(query)