from numpy import*

nome=array(eval(input("Atividade:")))
minut=array(eval(input("Minutos: ")))

ati=array(['ALONGAMENTO','CORRIDA','DANCA','ESCALADA','HIDROGINASTICA'])
calo=array([3,10.3,6.7,9.7,5])

total=zeros(4,dtype=int)
if(nome=="ALONGAMENTO"):
	total[0]=total[0]+(minut[i]*3)
elif(nome=="CORRIDA"):
	total[1]=total[1]+(minut[i]*(10.3))
elif(nome=="DANCA"):
	total[2]=total[2]+(minut[i]*(6.7))
elif(nome=="ESCALADA"):
	total[3]=total[3]+(minut[i]*(9.7))
elif(nome=="HIDROGINASTICA"):
	total[4]=total[4]+(minut[i]*(5))
		
print(round(total,2))
	
