volume = float(input("Volume de agua do mes: "))

total = (volume*0.37) + 15

contames = (total*(35/100)) + total

print (round(contames,2))