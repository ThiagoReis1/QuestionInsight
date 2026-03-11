from numpy import*
tp= array(eval(input("tipo de magia: ")))
nm= array(eval(input("nivel do mago:")))

i=0
s=0

while(i< size(tp)):
	if(tp[i]== 'GELO'):
		s = s+ nm[i]*2 
	elif(tp[i]== 'FOGO'):
		s = s+ nm[i]*3
	elif(tp[i]== 'CHOQUE'):
		s = s+ nm[i]*4
	elif(tp[i]== 'CONJURACAO'):
		s = s+ nm[i]*8
	elif(tp[i]== 'ILUSAO'):
		s = s+ nm[i]*10
	i=i+1
	
print(s)
		