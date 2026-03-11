vc = float(input("Digite o valor do carro: "))
vid = float(input("Digite o valor incial depositado: "))
dm = float(input("Digite o valor do deposito mensal: "))
tj = float(input("Digite o valor da taxa de juros: "))
vc = vc
vid = vid
dm = dm
tjt = tj / 100
t = 0
 
if(vid > 0):
	 
if(dm > 0):
	 
if(tj > 0):
		
else:
	print("Dados incorretos: ")
	
while(vc > 0):
	vc = vid + ((t * dm) + tjt)
	t = t + 1
	print(round(t, 2))


	
	



