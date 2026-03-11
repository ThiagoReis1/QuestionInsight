from math import*
pocoes = int(input("quantidade de pocoes"))

snowberry = ((5**0.5)-1)/4 
sais = sqrt(5-2*(5**0.5))
amanita = (5*(5-2*(5**0.5)))

a = pocoes* snowberry
b = pocoes* sais 
c = pocoes * amanita
				 
				 
print(round(a,2))
print(round(b,2))
print(round(c,2))