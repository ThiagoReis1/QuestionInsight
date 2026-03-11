from numpy import*
v=array(eval(input("Digite o numero de passageiros que entraram no onibus:")))
u=array(eval(input("Digite o numero de passageiros que sairam no onibus:")))
i=0
sobrar=0
while(i<size(v)):
	#if(v[i]>0 and u[i]>=0):
	sobrar= sobrar+ v[i]-u[i] 
	#else:
		#print("Dados invalidos")
	i=i+1
print(int(sobrar))
	
		









