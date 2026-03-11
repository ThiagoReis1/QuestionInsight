#Universidade Federal do Amazonas
#Jorge Trajano da Silva Junior
#lab de codificação 02 - Avaliação Parcial
#06.07.2016 
#Solicitar as notas das provas do período de Fredegunda
n1 = float(input("Informe a nota primeira nota: "))
n2 = float(input("Informe a nota da prova 2: "))
n3 = float(input("Informe a nota da terceira prova: "))
#Fórmula do programa
media = (n1 + n2 + n3) / 3
#Fazer a condição do programa e informar a situação de Fredegunda
if(media >= 7):
	situacao = "Aprovado"
else:
	situacao = "Reprovado"
#Imprimir resultados
print(round(media, 1))
print(situacao)