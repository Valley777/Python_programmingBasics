n = float(input()) #дължината на страна от площадката -square
w = float(input()) #широчината на една плочка в интервала
l = float(input()) #дължината на една плочка в интервала
m = float(input()) #широчината на пейката в интервала
o = float(input()) #дължината на пейката в интервала

workingArea = n*n #обща площ кв.м
bench = m*o #размер на пейката
sizeOnePlate = w*l #размер на плочката
areaExceptTheBench  = workingArea-bench
totalPlatesNeeded = areaExceptTheBench /sizeOnePlate #плочки за пространството
timeNeeded = totalPlatesNeeded*0.2 #minutes
print(totalPlatesNeeded)
print(timeNeeded)