inicial_d=float(input(""))
taxa=float(input(""))
juros=float(input(""))

new_juros=juros/100
t=0
final_percent=(inicial_d*15)/100
final_d=inicial_d+final_percent


while(inicial_d<final_d):
	if(inicial_d>0 and taxa>0 and juros>0):
		inicial_d=inicial_d-taxa+(inicial_d*new_juros)
		t=t+1
	else:
		print("Dados incorretos")
		exit()
print(t)