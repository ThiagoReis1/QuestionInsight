#UFAM
#Adriano Brito - 21555121
#AV 2 - qst 02

x = int(input("Digite a entrada para X: "))

ent = (x // 1000 - x % 1000) ** 4

if(x == ent):
	print(x ,"atende a propriedade")
else:
	print(ent)