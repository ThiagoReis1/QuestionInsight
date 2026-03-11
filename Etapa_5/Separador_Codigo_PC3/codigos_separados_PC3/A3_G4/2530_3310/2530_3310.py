# D reias 
# tmf de tf reais
#tx = j% - tm
#LEIA: DEPOSITO INICIAL
#saida: tempo necessario saldo > 15% o valor do deposito

D = float(input("Digite o valor do deposito inicial: "))
TF = float(input("Digite o valor da tarifa fixa mensal: "))
J = float(input("Digite o valor do juros: "))

t = 0
s = D
fim = s*(15/100) + s



if(D>0 and TF>0 and J>0):
	while(s<=fim):
		s = s + s*(J/100) - TF
		novo_s = round(s,2)
		t = t + 1
	print(t)
else:
	print("Dados incorretos")






