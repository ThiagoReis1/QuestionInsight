#Universidade Federal do Amazonas - UFAM
#Igor Rodrigues Chicolet da Silva - 21204615
#29/06/2016

num = int(input("Qual o numero? "))
var1 = num // 10000
var2 = num % 10000 

if(num == (var1 + var2) ** 2):
	print(num, "atende a propriedade")
else:
	cal = (var1 + var2) ** 2
	print(cal)
