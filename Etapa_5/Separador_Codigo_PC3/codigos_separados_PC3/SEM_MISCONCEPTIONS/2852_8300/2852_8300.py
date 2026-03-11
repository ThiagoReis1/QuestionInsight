def soma_vetor(vetor):
soma=0
for elemento in vetor:
	if elemento == 88:
		soma/=2
else:
	soma += elemento 
	return soma
resultado = soma_vetor(vetor)
print("Resultado")
	