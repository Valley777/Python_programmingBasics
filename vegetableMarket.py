priceKgVeg = float(input())
priceKgFruits = float(input())

totalKGVeg = float(input())
totalKGFruits = float(input())

amountVeg = priceKgVeg * totalKGVeg
amountFruits= priceKgFruits *totalKGFruits

total = (amountVeg+amountFruits)
totalEur = total/1.94
print(totalEur)
