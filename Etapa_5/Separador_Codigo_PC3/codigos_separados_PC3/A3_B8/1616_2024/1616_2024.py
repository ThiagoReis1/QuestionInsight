from numpy import*
magia=array((input()))
nivel= array(eval(input("Nivel do mago: ")))
i=0
x=0
danos=0
while(i<size(magia) and i<size(nivel)):
	print(i)
	if(magia[i]=='GELO'):
		danos=danos+(2*(nivel[i]))
		i+=1
	elif(magia[i]=='FOGO'):
		danos=danos+(3*(nivel[i]))
		i+=1
		x+=1
	elif(magia[i]=='CHOQUE'):
		danos=danos+(4*(nivel[i]))
		i+=1
		x+=1
	elif(magia[i]=='CONJURACAO'):
		danos=danos+(8*(nivel[i]))
		i+=1
		x+=1
	elif(magia[i]=='ILUSAO'):
		danos=danos+(10*(nivel[i]))
		i+=1
		x+=1
print(danos)
	