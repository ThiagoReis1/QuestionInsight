#n = 25502500
#LEIA: UM NUMERO FORNECIDO
#SAIDA: 1- numero fornecido 2 - atende/nao atende

n = int(input("Digite um numero de 8 digitos: "))

d_4 = n // 10000
d_8 = n % 10000

#condicao
prop = (d_4 + d_8)**2

if(prop == n):
	m = "atende"
else:
	m = "nao atende"
print(n)
print(m)

