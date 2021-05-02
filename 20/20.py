def conv(a):
    try:
        a = int(a)
        return a
    except ValueError:
        return a


def func(bottles: list, money, totalV):
    canBuy = False
    try:
        minPricePerLiter = bottles[0]["pricePerLiter"]
    except:
        {}

    for i in bottles:
        if i["price"] <= money:
            canBuy = True
        if i["pricePerLiter"] <= minPricePerLiter:
            minPricePerLiter = i["pricePerLiter"]

    if not canBuy:
        print(totalV)
        print(money)
        exit()

    tempD = None
    for i in bottles:
        if i["pricePerLiter"] == minPricePerLiter:
            tempD = i
            bottles.remove(i)

    bottleCount = 0
    while 0 <= money - tempD["price"]:
        money -= tempD["price"]
        bottleCount += 1
    print(tempD["name"], end=" ")
    print(bottleCount)
    totalV += bottleCount * tempD["v"]

    func(bottles, money, totalV)


money = int(input("money = "))
bottlesCount = int(input("bottlesCount = "))
bottles = []
canBuy = False

for i in range(bottlesCount):
    d = dict()
    d["name"], d["price"], d["v"] = map(conv, input().split())
    d["pricePerLiter"] = d["price"] / d["v"]
    bottles.append(d)
    if d["price"] < money:
        canBuy = True

if not canBuy:
    print("-1")
    exit(-1)

func(bottles, money, 0)
