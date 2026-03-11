from math import*

p = float(input("qual o peso daa racao em gramas: "))
q = float(input("qual a quantidade diaria de racao em gramas: "))

d = p - 6 * q
print(round(d,4))