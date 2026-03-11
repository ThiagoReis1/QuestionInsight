am = 1.4
tm = 0.06
al = float(input())
tl = float(input())
cont = 1
am = am + tm
al = al + tl

while am<al:
	am = am + tm
	al = al + tl
	cont = cont + 1 
	
print(cont)