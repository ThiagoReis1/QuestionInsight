#Universidade Federal do Amazonas
#Aluna: Larissa Magno Leão
#Matrícula: 21551610
#Exercicio 2

x= int(input("Informe um numero:"))

a= x //100 
r= x % 100
b= r // 10
c= r % 10

soma= a **3 + b**3 + c**3

if (soma==x):
	print(x,"atende a propriedade")
else:
	print(soma)