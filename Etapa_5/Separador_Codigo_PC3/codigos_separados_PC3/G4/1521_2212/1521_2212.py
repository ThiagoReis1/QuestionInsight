#n containers a cada viagem
#ida e volta duram uma semana ou 7 dias
# Q containers chegam ao terminal de carga
n = int(input("Qual a capacidade do navio, em número de containers? "))
e = int(input("Qual o estoque inicial de containers no depósito? "))
q = int(input("Qual a quantidade de containers que chegam no depósito a cada semana? "))

#variavel acumuladora
f=e
#contador
t=0
while(f>0):
	f = f+q-n
	t =t+1
print(t)
	