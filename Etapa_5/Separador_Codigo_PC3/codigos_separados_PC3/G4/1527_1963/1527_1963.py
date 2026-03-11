#Dina Karen Barros 
#Trabalho Prático 04
#ex 01

f0 = int(input("Qtdade inicial do deus Forseti:"))
l0 = int(input("Qtdade inicial do deus Loki:"))
fx = float(input("Pecentual de crescimento do deus Forsete:"))
lx = float(input("Pecentual de crescimento do deus Loki:"))

somafi = f0
somali = l0
ano = 0

#laço
while (somali < somafi):
	somafi = somafi + (somafi * (fx/100))
	somali = somali + (somali * (lx/100))
	ano = ano + 1
	
print(ano)