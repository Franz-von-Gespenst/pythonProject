hallo = list("hallo")
klempner = list("klempner")
das = list("das")
ist = list("ist")
fantastisch = list("fantastisch")
fluggegecheimen = list("fluggegecheimen")

list = []

list.extend(hallo)
list.extend(klempner)
list.extend(das)
list.extend(ist)
list.extend(fantastisch)
list.extend(fluggegecheimen)

dict = {}

for i in list:
    dict[i] = list.count(i) / len(list)

stopWord = input()
res = 1
for i in range(0, len(stopWord)):
    res *= dict[stopWord[i]] if dict.__contains__(stopWord[i]) else 0

print(res)
