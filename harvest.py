import math

squareMetersVineYard = float(input()) #field
winePerOneSqMeter = float(input()) #   grapes yield per square meter
neededWine = float(input()) #desired amount of wine
workersNum = float(input()) #number of workers

wine = (squareMetersVineYard * winePerOneSqMeter)  #40% from the field for wine
totalWine =  (wine*0.4)/2.5

if totalWine < neededWine:

    z = neededWine-totalWine
    z = math.floor(z)
    print(f'It will be a tough winter! More {z} liters wine needed.')

elif totalWine > neededWine:
    totalWine = math.floor(totalWine)

    leftOvers = totalWine - neededWine
    leftOvers = math.ceil( leftOvers)
    winePerWorker = leftOvers/ workersNum
    winePerWorker = math.ceil(winePerWorker)

    print(f'Good harvest this year! Total wine: {totalWine} liters.\n {leftOvers} liters left -> {winePerWorker} liters per person.')



