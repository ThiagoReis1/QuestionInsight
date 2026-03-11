idade=int(input())
peso=float(input())

if	(peso<=60)or(60<=peso<=90)or(peso>90):
	if	(idade<=20 and peso<=60):
		print("Grupo 9")
	elif	(idade<=20 and 60>peso>=90):
		print("Grupo 8")
	elif	(idade<=20 and peso>90):
		print("Grupo 7")
		
	
			