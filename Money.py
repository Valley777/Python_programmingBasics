bitcoins = float(input())
chineseCurrency  = float(input())
percentTax = float(input())/100

sumBitcoins = bitcoins *1168 #lv
#print(sumBitcoins) - OK
sumChineseToUSD = chineseCurrency *0.15
#print(sumChineseToUSD ) - OK
usdToLV = sumChineseToUSD*1.76 #lv
#print(usdToLV ) -OK
sumLv = sumBitcoins + usdToLV
#print(sumLv) - OK
sumEUR = sumLv /1.95
#print(sumEUR )
ResultNotax= sumEUR-(sumEUR*percentTax )
print(f'{ResultNotax:.2f}')

