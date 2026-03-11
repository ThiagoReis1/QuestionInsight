nome = input("Insira o nome do aminoacido:")
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794

if(nome.upper() != 'ASPARAGINA' and nome.upper() != 'TRIPTOFANO' and nome.upper() != 'GLUTAMINA' ):  
	print("Entrada:", nome.upper())
	print("Dado Invalido")	
	
	
if(nome.upper() == 'ASPARAGINA'):
	peso = c*4 + h*8 + n*2 + o*3
	print(round(peso,2))

if(nome.upper() == 'GLUTAMINA'):
	peso = c*5 + h*8 + n*1 + o*4
	print(round(peso,2))
	
if(nome.upper() == 'TRIPTOFANO'):
	peso = c*11 + h*11 + n*2 + o*2
	print(round(peso,2))



	
