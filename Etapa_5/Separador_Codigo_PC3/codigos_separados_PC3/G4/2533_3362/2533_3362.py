v = float(input("insira o valor da indenizacao R$: "))
c = float(input("insira o valor do saque mensal fixo R$: "))
j = float(input("insira o valor da taxa de juros: "))

i= 0
t1 = v
if  (v > 0 and c > 0 and j > 0):	
	while(t1 > v/2):
		t1 = (t1 + (t1*(j/100)))- c
		t1 = round(t1,2)
		i= i+1
		
	print(i)
else:
		print("Dados incorretos")