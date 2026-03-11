from math import*
x = eval(input(""))
k = int(input("")) - 1
d = 0 
t = 0 
while(t<=k):
    g = ((((-1) ** t)) * (x ** (2 * t + 1))/(factorial(2 * t + 1)))
    d = d + g
    t = t + 1
print(round(d,6))	

