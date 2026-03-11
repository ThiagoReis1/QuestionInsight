#ENTRADA DE DADOS
t=float(input("t, em min?"))

#CALCULO INTERNO
p1=(100*t) + 5000
p2=(8000)+(100*200)+(90*(t-200) ) 

#SAIDA DE DADOS
if (t<200):
	print(p1)
else:
	print(p2)

