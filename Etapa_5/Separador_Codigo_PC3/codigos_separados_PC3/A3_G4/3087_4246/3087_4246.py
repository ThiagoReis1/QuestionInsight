n = int(input("digite o numero: "))
par = 0
mp = 0.0
sp = 0

impar = 0
mi = 0.0
si = 0
while(n != 0):
	if(n%2 == 0):
		par = par + 1
		sp = sp + n
		mp = sp/par
	else:
		impar = impar + 1
		si = si + n
		mi = si/impar
	n = int(input("digite o numero: "))
print(round(mp,2))
print(round(mi,2))