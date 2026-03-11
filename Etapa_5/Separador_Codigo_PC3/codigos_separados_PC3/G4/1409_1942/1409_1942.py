tipoAtq=input("Tipo de Ataque (espada/cauda): ")
d1=int(input("valor 1: "))
d2=int(input("valor 2: "))
d3=int(input("valor 3: "))
d4=int(input("valor 4: "))
if(tipoAtq == 'espada'):
	dano=(d1+6)+(d2+6)+(d3+6)+(d4+6)
	print(dano)
if(tipoAtq == 'cauda'):
   dano=(d1+d2+d3)*d4
   print(dano)