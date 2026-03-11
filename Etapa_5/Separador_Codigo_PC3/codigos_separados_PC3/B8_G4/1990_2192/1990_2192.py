nome = input()

o = 15.9994
c = 12.011
n = 14.0067
h = 1.00794

if(nome == "GLUTAMINA" or nome == "SERINA" or nome == "TREONINA"):
	if(nome == "GLUTAMINA"):
		p = round(float(c*5 + h*8 + n + o*4), 2)
		print(p)
	elif(nome == "SERINA"):
		p = round(float(c*3 + h*7 + n + o*3), 2)
		print(p)
	elif(nome == "TREONINA"):
		p = round(float(c*4 + h*9 + n + o*3), 2)
		print(p)
else:
	print("Entrada:", nome)
	print("Dado Invalido")