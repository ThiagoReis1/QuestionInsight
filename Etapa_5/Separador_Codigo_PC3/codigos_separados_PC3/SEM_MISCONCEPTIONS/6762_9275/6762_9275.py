# faça seu código aqui!
idade_do_espectador = float(input("digite a sua idade: "))

ingresso = 20.00

if idade_do_espectador <12:
	custo_total = ingresso + 1.25
	
elif idade_do_espectador == 12: 
	custo_total = ingresso + 2.25
	
else:
	custo_total = ingresso + 3.25
	
print(round(custo_total, 2))