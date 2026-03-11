#Valores Iniciais 
f = int(input("Insira a quantidade de seguidores do deus \"Forseti\": "))
l = int(input("Insira a quantidade de seguidores do deus \"Loki\": "))
pf = float(input("Insira o porcentual de crescimento de seguidores do deus \"Forseti\": "))/100
pl = float(input("Insira o porcentual de crescimento de seguidores do deus \"Loki\": "))/100

#Variavel contadora
ano = 0

#Laco de acumulacao
while (f >= l):
	f = f + (f*pf)
	l = l + (l*pl)
	ano = ano + 1
print(ano)