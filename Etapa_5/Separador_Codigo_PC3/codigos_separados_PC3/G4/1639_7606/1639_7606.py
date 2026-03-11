from numpy import*
v = array(eval(input("digite")))
qtd = 0
for i in range(size(v)):
	if v[i] % 2 == 0:
		qtd = qtd + 1
		
print(qtd)
resultados = zeros(qtd, dtype = int)
a = 0

for i in range(size(v)):
	if v[i] % 2 == 0:
		resultados[a] = i
		a = a + 1

print(resultados)

	