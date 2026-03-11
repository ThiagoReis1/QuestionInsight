from numpy import*
v=array(eval(input("notas: ")))

prova=v[0]
sem=v[1]
trab=v[-1]
n=((prova*5)+(sem*3)+(trab*2))/10
if(n>=5.0):
	print(round(n,2))
	print("APROVADO")
else:
	print(round(n,2))
	print("REPROVADO")