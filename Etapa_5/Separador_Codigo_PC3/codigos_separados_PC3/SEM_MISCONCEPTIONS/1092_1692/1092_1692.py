#Wagner William Amorim de Andrade - 21552149
#Segundo Exercicio Avaliativo
#Questão 2
#30/06/2016

numero = (int(input("Digite o numero desejado: ")))

n100 = numero // 100
resto100 = numero % 100

n10 = resto100 // 10
resto10 = resto100 % 10

n1 = resto10 // 1 

x = ((n100 ** 3 + n10 ** 3 + n1 ** 3))

if (x == numero):
		print (numero, "atende a propriedade")
else:
		print(x)
