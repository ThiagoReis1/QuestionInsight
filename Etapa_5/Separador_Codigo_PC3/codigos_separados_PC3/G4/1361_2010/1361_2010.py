from math import*

p=int(input("quantidade de poções: "))

a= (sqrt(5) - 1) / 4
b= sqrt((5 - 2*sqrt(5)))
c= 5 * (5 - 2*sqrt(5))

s= p*a
sa= p*b
am= p*c

print(round(s,2))
print(round(sa,2))
print(round(am,2))
