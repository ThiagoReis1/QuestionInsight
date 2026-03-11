x = float(input("Numero real: "))
k = int(input("Qntd de termos: "))
#
s = 0
cont = 0
d = 1
#
while(cont < k):
	s = s + (x / d )
	d = d + 2
	cont = cont + 1
print(round(s , 8))