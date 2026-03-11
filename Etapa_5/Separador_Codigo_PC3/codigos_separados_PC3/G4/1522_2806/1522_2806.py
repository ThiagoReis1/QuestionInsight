qi= int(input("Digite a quantidade inicial: "))
dp=int(input("Digite despesa mensal: "))
qm= int(input("Digite a quantidade de impostos: "))
qr=int(input("Digite a quantidade roubada: "))

t= 1 #variável contadora
soma= 0 #variável acumuladora

while(qi >= t):
	a= (qi + qm) - (dp + qr)
	soma= soma + a
	t= t + 1

print(t)