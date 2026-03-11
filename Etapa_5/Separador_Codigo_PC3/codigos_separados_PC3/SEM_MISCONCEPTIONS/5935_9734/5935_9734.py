pesokg = float(input("peso kg "))
frete = pesokg * 43.21 + 25.00
total = frete * (62/100) + frete
print(round(total, 2))