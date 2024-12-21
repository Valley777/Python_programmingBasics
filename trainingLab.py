

l = float(input())*100
w = float(input())*100

rows = l /120
rows = round(rows)
desksPerRow = (w-100)/70
desksPerRow = round(desksPerRow)
totalNumberOfDesks = (rows * desksPerRow )-3
print(totalNumberOfDesks)