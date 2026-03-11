volume = float(input("volume de agua consumido: "))
total = (0.37*volume + 15) + (0.37*volume + 15)*35/100
print(round(total, 2))
