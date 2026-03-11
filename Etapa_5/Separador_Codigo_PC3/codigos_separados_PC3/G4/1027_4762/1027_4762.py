from math import*
var1 = float(input("Custo de energia: "))
var2 = 0.43
var3 = 10.00

x = (var1*var2)+var3
x2 = (x/100)*25

print(round(x+x2,2))