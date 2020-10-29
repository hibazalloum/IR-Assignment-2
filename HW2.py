movies = open('movies.txt', encoding="utf-8")

termDict = {}
kgramDict= {}

with open('movies.txt', 'r') as movie:
    for line in movie:
        words = line.replace('.', '').replace('\'', '').replace(',', '').lower().split()
        for word in words:
            g = K_Gram (3, trem)
            if word not in termDict:
                termDict[word] = 1
            else:
                termDict[word] = termDict[word] + 1


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

def search ()