from math import*

x = float(input(": "))
k = int(input(": "))

cont = 0 
ac = 0
i = 1

while (cont < k):
	ac = ac + ( x / factorial (i))
	i = i + 2
	cont = cont + 1
print(round(ac, 8))