altura_macaco = 1.86
taxa_macaco = 0.01
altura_coelho = float(input("digite a altura: "))
taxa_coelho = float(input("digite a taxa: "))
cont = 0

while(altura_macaco >= altura_coelho):
	altura_macaco = altura_macaco + taxa_macaco
	altura_coelho = altura_coelho + taxa_coelho
	cont = cont + 1
print(cont)