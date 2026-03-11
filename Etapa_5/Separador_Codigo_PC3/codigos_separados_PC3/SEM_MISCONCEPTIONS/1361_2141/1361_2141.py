from math import *
x = int(input("quantidade"))

snowberry = ((5**0.5 - 1)/4)* x
fogo = sqrt(5 - 2*(5**0.5))* x
amanita = 5*(5 - 2*(5**0.5))* x

print(round(snowberry,2))
print(round(fogo,2))
print(round(amanita,2))


