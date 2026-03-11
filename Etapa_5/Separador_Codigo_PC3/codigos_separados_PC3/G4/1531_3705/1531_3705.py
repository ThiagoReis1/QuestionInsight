from math import*
x = eval(input(""))
k = int(input("")) - 1
d = 0 #soma
t = 0 #contagem
while(t<k):
    cos = ((((-1) ** t)) * (x ** (2 * t + 2))/(factorial(2 * t + 2)))
    d = d + cos
    t = t + 1
print(round(d,10))	