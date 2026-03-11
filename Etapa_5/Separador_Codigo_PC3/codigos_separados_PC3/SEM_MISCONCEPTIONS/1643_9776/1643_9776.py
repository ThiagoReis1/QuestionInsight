from numpy import*
def alunos_aprovados(notas):
	indices_aprovados = []
	
	count = 0
	for i in range(len(notas)):
		if notas[i] >= 5.0:
			count += 1
			indices_aprovados.append(i)
			
	return count, array(indices_aprovados)

entrada = input().strip()
entrada_lista = eval(entrada)

quantidade, indices = alunos_aprovados(entrada_lista)

print(quantidade)
print(indices)