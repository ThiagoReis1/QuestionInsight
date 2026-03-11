from math import*
c = float(input("peso da mercadoria: "))


f = (c*43.21+25)
y = f*(62/100)
total = (f+y)

print(round(total,2))