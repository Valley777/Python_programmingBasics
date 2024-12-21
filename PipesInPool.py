import math
volume = float(input())  #V – обем на басейна в литри
firstPipe = float(input()) # - дебит на първата тръба за час
secondPipe = float(input())  # - дебит на втората тръба за час
hoursDebit = float(input()) # - часовете, в които работникът отсъства

volumePipe1 =  firstPipe *hoursDebit
#print(volumePipe1)
volumePipe2 = secondPipe * hoursDebit
#print(volumePipe2)

finalVolume = volumePipe1+ volumePipe2
#print(finalVolume)
#The formula used to calculate the percentage of something is: (value/total value)×100%.
percentageFromTotalVolumePool  = (finalVolume/volume)*100
percentageFromTotalVolumePool = math.floor(percentageFromTotalVolumePool)
percentageFirstPipeFromTotalVolumePool = (volumePipe1/finalVolume)*100
percentageFirstPipeFromTotalVolumePool =  math.floor(percentageFirstPipeFromTotalVolumePool)
percentageSecondPipeFromTotalVolumePool = (volumePipe2/finalVolume)*100
percentageSecondPipeFromTotalVolumePool = math.floor(percentageSecondPipeFromTotalVolumePool)

if finalVolume < volume:
    print(f'The pool is {percentageFromTotalVolumePool }% full. Pipe 1: {percentageFirstPipeFromTotalVolumePool }%. Pipe 2: {percentageSecondPipeFromTotalVolumePool }%.')
elif finalVolume >volume:
    z = finalVolume - volume
    print(f'For {hoursDebit} hours the pool overflows with {z:.2f} liters.')
