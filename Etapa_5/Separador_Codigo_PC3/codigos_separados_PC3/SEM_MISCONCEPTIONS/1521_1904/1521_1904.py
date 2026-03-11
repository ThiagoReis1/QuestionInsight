n = int(input("capacidade n do navio:"))
e = int(input("estoque inicial:"))
#ida e volta = uma semana

#a cada semana :
q = int(input("+ containers que chegam ao terminal:"))
semana = 0
contador = 0

while(e>0):
	e = (e-n)+(q)
	contador = contador + 1
	semana = semana + 1
	
print(semana)