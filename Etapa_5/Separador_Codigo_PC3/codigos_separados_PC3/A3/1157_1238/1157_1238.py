# Talita Oliveira Gomes Passos
# 28 de Julho de 2016
# Av. 4 - Ex 01

pop_tamb = int(input("População inicial de tambaquis: "))
taxa_ano = float(input("Taxa anual de crescimento de tambaquis: "))
retirados = int(input("Número de tambaquis retirados anualmente: "))

# Var contadora
anos = 0

# Var acumuladora
cres = pop_tamb * taxa_ano

while(cres > 0):
	ext = pop_tamb + cres - retirados
	anos = 10
print(anos)