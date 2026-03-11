from numpy import*

saques = array(eval(input("Insira o valor: "))) dtype = int

cont = 0

for i in (size(saques)):
	if saques <= 50:
		cont += 1
ind = zeros(cont, dtype = int)

x = 0
for i in range(size(saques)):
	if saques[i] == saques:
		ind[x] = i
		x += 1
		
print(ind)
print(min(cont))