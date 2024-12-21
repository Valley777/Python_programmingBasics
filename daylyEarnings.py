wd = float(input()) #работни дни в месеца
md = float(input()) #изкарани пари на ден
usdToLv= float(input()) #курсът на долара спрямо лева /1 долар = X лева/

monthlyPayment = wd * md #usd
yearIncome  = (monthlyPayment * 12) +   (monthlyPayment*2.5)
incomeAfterTax = yearIncome-(0.25*yearIncome)
conversionToLV = incomeAfterTax*usdToLv #lv
averageProfit = conversionToLV/365
print(f'{averageProfit:.2f}')
