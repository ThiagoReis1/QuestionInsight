from math import*
tp = input("torta ou pastel")
q = int(input("Quantos t ou p"))
c = int(input("quantos cappuccinos"))

tp.upper 

if tp == "T":
	total = (c*4.5) + (q*6)
else: 
	total = (c*4.5) + (q*5)
	
print(total)