import math

offDays = int(input()) #broj po4ivni dni ex > 113
workingDays = 365-offDays # 365-113 =252
minutesPerWDay = 63  #playtime wday
minutesPerODay = 127 #playtime oday

realPlayTime = (workingDays * minutesPerWDay) + (offDays*minutesPerODay) #252*63+113*127=15876+14351
#print(realPlayTime) #Реалното време за игра
normMinutesperyear = 30000
if normMinutesperyear > realPlayTime:
  normMinutes = normMinutesperyear- realPlayTime #Разликата от нормата е 5 725
  normConvertedHours = normMinutes/60
  normConvertedHours = math.floor(normConvertedHours) #hours
  normConvertedMinutes = normMinutes%60 #minutes
  print(f'Tom sleeps well\n{normConvertedHours} hours and {normConvertedMinutes} minutes less for play')
elif 30000 < realPlayTime:
    norm = realPlayTime - normMinutesperyear
    normH = norm/60
    normH = math.floor(normH)
    normM = norm%60
    print(f'Tom will run away\n{normH} hours and {normM} minutes more for play')


