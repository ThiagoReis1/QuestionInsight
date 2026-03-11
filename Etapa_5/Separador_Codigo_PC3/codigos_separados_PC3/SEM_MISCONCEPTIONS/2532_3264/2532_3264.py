carro=float(input(""))
inicial_d=float(input(""))
mensal_d=float(input(""))
juros=float(input(""))

new_juros=juros/100
t=0

while(inicial_d<carro):
	if(inicial_d>0 and mensal_d>0 and juros>0):
		inicial_d=inicial_d+mensal_d+(inicial_d*new_juros)
		t=t+1
	else:
		print("Dados incorretos")
		exit()
print(t)