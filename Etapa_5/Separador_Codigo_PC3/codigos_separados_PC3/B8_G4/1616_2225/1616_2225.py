from numpy import*

v=array(eval(input("tipo: ").upper()))
d=array(eval(input("numero: ")))
i=0
da=0
while(i<size(v)):
	if(v[i]=="GELO"):
		da=da+2*d[i]
	elif(v[i]=="FOGO"):
		da=da+3*d[i]
	elif(v[i]=="CHOQUE"):
		da=da+4*d[i]
	elif(v[i]=="CONJURACAO"):
		da=da+8*d[i]
	elif(v[i]=="ILUSAO"):
		da=da+10*d[i]
	i=i+1
print(da)
