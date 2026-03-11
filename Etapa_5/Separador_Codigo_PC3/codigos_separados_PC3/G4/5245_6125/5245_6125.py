sal= float(input(''))
print("Entrada:", "R$",sal)

if 0 < sal<= 800:
	ts= sal * 0.50
	tt= sal + ts
	print('Novo salario:',"R$",(round(tt, 2)))
elif 800< sal<= 1000:
	ts= (sal * 0.40) 
	tt= sal + ts
	print("Novo salario:","R$", (round(tt,2)))
elif 100< sal <= 1200:
	ts= sal * 0.30
	tt= sal + ts
	print("Novo salario:","R$", (round(tt,2)))
elif 1200< sal <= 1400:
	ts= sal * 0.20
	tt= sal + ts
	print("Novo salario:", "R$", (round(tt,2)))
elif 1400< sal <= 1600:
	ts= sal * 0.10
	tt= sal + ts
	print('Novo salario:', "R$", (round(tt,2)))
elif 1600< sal:
	ts= sal * 0.05
	tt= sal + ts
	print("Novo salario:", "R$", (round(tt,2)))
else:
	print("Dado invalido")