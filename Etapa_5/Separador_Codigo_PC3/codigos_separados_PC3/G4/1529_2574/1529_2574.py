from math import*
inf = int(input("Insira a quantidade inicial da infantaria: "))
cal = int(input("Insira quantidade inicial da cavalaria.: "))
pinf = float(input("Insira o percentual da infantaria: "))
pcal = float(input("Insira o percentual da cavalaria: "))

xinf = inf
xcal = cal
m = 0

while(xinf + xcal < 50000):
	xinf = xinf +(xinf*pinf/100)
	xcal = xcal +(xcal*pcal/100)
	m = m + 1

print(m)	

