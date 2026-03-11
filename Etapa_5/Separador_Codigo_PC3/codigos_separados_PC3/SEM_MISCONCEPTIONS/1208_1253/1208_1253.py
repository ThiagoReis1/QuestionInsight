from numpy import*
recorde = 98.48 #recorde mundial
vetor_dardo = array(eval(input("Digite o vetor:")))#vetor dos lançamentos

i= 0
count = 0 
while( i < size(vetor_dardo)):
	if(vetor_dardo[i] == recorde):
		count = count + 1
	i = i + 1
else:
		print(recorde)
i= 0
count = 0
	
while(i < size(vetor_dardo)):
	if(vetor_dardo[i] < recorde):
		count = count + 1
	i = i + 1
print(count)
			
