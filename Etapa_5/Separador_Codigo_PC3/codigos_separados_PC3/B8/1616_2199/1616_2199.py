from numpy import*

tipodemagia = input("Qual tipo de magia?:")

nivelmago = array(eval(input("Qual nivel do mago?:")))

i = 0
dano = 0
while (i < len(tipodemagia)):
	if(tipodemagia[i] == "GELO"):
		dano = dano + 2 * nivelmago[i]
	elif(tipodemagia[i] == "FOGO"):
		dano = dano + 3 * nivelmago[i]
	elif(tipodemagia[i] == "CHOQUE"):
		dano = dano + 4 * nivelmago[i]
	elif(tipodemagia[i] == "CONJURACAO"):
		dano = dano + 8 * nivelmago[i]
	elif(tipodemagia[i] == "ILUSAO"):
		dano = dano + 10 * nivelmago[i]
		
		i = i + 1
		
	print(dano)