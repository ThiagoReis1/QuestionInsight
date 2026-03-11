from numpy import*
v = array(eval(input(" ")))

saque_igual = 0
saque_maior = 0

for i in range(size(v)):
	if(v[i] <=2000 == 0):
		saque_igual = 2000
		
for i in range(size(v)):
	if(v[i] >=2000 == 0):
		saque_maior += 2000
		
aux = zeros(saque_igual, saque_maior, dtype = int)

x = 0

for i in range(size(v)):
	if i == 0 and v[0] >2000 == 0:
		aux[0] = 0
		x+= 1
		
print(saque_maior)
print(saque_igual)
print(aux)