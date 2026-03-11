kwh = float(input())

total = (0.43*kwh + 10)
total = total + (total*25/100)

print(round(total,2))