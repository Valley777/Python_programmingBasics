km = float(input())
dayTime = input().lower()
price = 0.0
                            #Такси
if km <= 20 and dayTime=='day':
 price =  0.70+(0.79*km)
 print(price)
elif km<=20 and dayTime == 'night':
 price = 0.70 + (0.90*km)
 print(price)
                            # Автобус
elif km>=21 and km<=100:
  price = 0.09* km
  print(price)
elif km>=101:              #Влак
  price = 0.06 * km
  print(price)