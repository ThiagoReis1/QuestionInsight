'''
	|-----------|
	| Questão 1 |
	|-----------|
	
	Universidade Federal do Amazonas
	Instituto de Ciências Exatas
	Departamento de Física
	
	Aluno: Micael Davi Lima de Oliveira
	Matrícula: 21851626 | Turma: FB01

'''
from numpy import* # biblioteca necessária para utilizar a função array

# o vetor 'tipo' armazenará strings, e será crucial para armazenar todos os correspondentes tipos de espada dos combatentes. 
tipo = array(eval(input("Tipos de Espada: \n 1.CENOURA \n 2.FERRO \n 3.DWARVEN \n 4.ELVEN \n 5.DAEDRIC \n  *Escolha: ")))
# o vetor 'nivel' armanará valores inteiros, e será importante para armzenas os níveis dos combatentes.
nivel = array(eval(input("Nivel do Combatente: ")))

dano_total = 0 # varíavel acumuladora

i = 0 # variável contadora
while (i < size(tipo)): # laço de repetição para percorrer os vetores
	if (tipo[i] == "CENOURA"):
		dano_total += 2*nivel[i]
	elif (tipo[i] == "FERRO"):
		dano_total += 4*nivel[i]
	elif (tipo[i] == "DWARVEN"):
		dano_total += 8*nivel[i]
	elif (tipo[i] == "ELVEN"):
		dano_total += 11*nivel[i]
	elif (tipo[i] == "DAEDRIC"):
		dano_total += 14*nivel[i]
	i += 1 # para cada combatente analisado, 'i' precisa ser incrementado
print("%d" %(dano_total)) # por último, é impresso como saída o valor final da variável acumuladora(dano_total)
