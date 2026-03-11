from numpy import*

vetor_ex = array(eval(input()))
vetor_tempo = array(eval(input()))

i = 0
total = 0

while(i<size(vetor_ex)):
	if(vetor_ex[i]=="ALONGAMENTO"):
		total = total + vetor_tempo[i]*3.0
	elif(vetor_ex[i]=="CORRIDA"):
		total = total + vetor_tempo[i]*10.3
	elif(vetor_ex[i]=="DANCA"):
		total = total + vetor_tempo[i]*6.7
	elif(vetor_ex[i]=="ESCALADA"):
		total = total + vetor_tempo[i]*9.7
	elif(vetor_ex[i]=="HIDROGINASTICA"):
		total = total + vetor_tempo[i]*5.0
		
	i = i+1

print(round(total,2))
 		