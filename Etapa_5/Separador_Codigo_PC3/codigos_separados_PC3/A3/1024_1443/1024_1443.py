#Universidade Federal do Amazonas - UFAM
#Igor R Chicolet da Silva
#Matricula: 21204615
#Avaliacao 1 - Ex. 01

a = float
b = float
c = float
a = float(input("Qual o valor do lado a? "))
b = float(input("Qual o valor do lado b? "))
c = float(input("Qual o valor do lado c? "))
custo = float(input("Qual e o custo de construcao da cerca? "))
custo_total = (a + b + c) * custo
print(round(custo_total,2))