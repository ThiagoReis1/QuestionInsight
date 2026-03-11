from math import*
amin = input('aminoacido:')
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079
g = (c*2)+(h*5)+n+(o*2)
p = (c*5)+(h*10)+n+(o*2)
s = (c*3)+(h*7)+n+(o*3)
if(amin.upper() == 'Glicina'.upper()):
	print(round(g, 2))
elif(amin.upper() == 'Prolina'.upper()):
	print(round(p, 2))
elif(amin.upper() == 'Serina'.upper()):
	print(round(s, 2))
else:
	print('Entrada:', amin)
	print('Dado Invalido')
	
