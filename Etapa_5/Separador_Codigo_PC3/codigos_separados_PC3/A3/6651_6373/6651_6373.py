from numpy import*
notas_str = input("digite o vetor:")
vp= array(eval(input([5,4,3,2])))

notas = eval(notas_str)

if len(notas) != len(vp):
	print("ERROR")
else:
	soma_notas_pesos = sum([notas * vp ])
			  