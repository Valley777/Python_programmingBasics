import math

hoursNeeded = int(input()) #90 необходимите часове
workdays = int(input()) #7 дни , с които фирмата разполага
numberEmployees = int(input()) #3 броят на всички служители


workingHours= workdays*8*numberEmployees
workingHours = math.floor(workingHours)
#print(f'workingHours',workingHours)
overTimeHours = workdays*2*numberEmployees

hoursTotal = workingHours+overTimeHours
hoursTotal = math.floor(hoursTotal)
#print(f'hoursTotal',hoursTotal)
hoursFinal = hoursTotal - (hoursTotal*0.1)
hoursFinal=math.floor(hoursFinal)
#print(hoursFinal)

if hoursNeeded<hoursFinal:
    z = hoursFinal - hoursNeeded
    print(f'Yes!{z:.0f} hours left.')
elif hoursNeeded >hoursFinal:
    z1 = hoursNeeded-hoursFinal
    z1 = math.floor(z1)
    print(f'Not enough time!{z1} hours needed.')



# 3*7*2 > rabotnici po 7 dni po dva càsa -> 42 overtajm
# 7*8*3 = rabotni casove 168
# suma = 168+42 = 210 -10% = 210 -21 =189   189-90=99