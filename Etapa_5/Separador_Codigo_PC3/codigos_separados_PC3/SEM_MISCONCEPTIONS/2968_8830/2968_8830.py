solido = input("Lanche ou Salgado? Digite: L/S: ")
quantidade = float(input("Quantas unidades voce quer deseja?: "))
liquido = float(input("Sabendo que a coca eh 4 pila, quantas voce deseja?: "))

lanche=5
salgado=3.5
refri=4

if solido == "L":
	precof = (lanche * quantidade) + (refri*liquido)
	print(round(precof,2))
else:
	precof = (salgado * quantidade) + (refri*liquido) 
	print(round(precof,2))