num = int(input("escreva um num: "))
num1 = num // 100000
resto1 = num % 100000
numero2 = resto1 // 10000
resto2 = resto1 % 10000
numero3 = resto2 // 1000
resto3 = resto2 % 1000
numero4 = resto3 // 100
resto4 = resto3 % 100
numero5 = resto4 // 10
resto5 = resto4 % 10
numero6 = resto5 / 1

var = (num1*10 + numero2)**3 + (numero3*10 + numero4)**3 + (numero5*10 + numero6)**3
if(var == num):
	print(num,"atende a propriedade")
else:
	print(var)
