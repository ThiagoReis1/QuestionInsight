from numpy import*
#dano do mago = dano da magia * nivel do magico

vstr = array(eval(input("")))
vint = array(eval(input("")))

i=0
dano = 0

while(i<size(vstr)):
	if(vstr[i]=="GELO"):
		dano  = dano + 2*vint[i]
	elif(vstr[i]=="FOGO"):
		dano  = dano + 3*vint[i]
	elif(vstr[i]=="CHOQUE"):
		dano  = dano + 4*vint[i]
	elif(vstr[i]=="CONJURACAO"):
		dano  = dano + 8*vint[i]
	elif(vstr[i]=="ILUSAO"):
		dano  = dano + 10*vint[i]
		
	print (dano)