ea = float(input("estimativa de alunos por metros quadrados: "))
base_menor = float(input("comprimento da base menor: "))
base_maior = float(input("comprimento da base maior: "))
h = float(input("altura: "))
					  
A= h*(base_maior + base_menor)/2

QA = A*ea


print(int(QA))
