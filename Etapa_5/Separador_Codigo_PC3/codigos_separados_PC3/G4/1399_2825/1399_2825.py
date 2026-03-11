Q1 = float(input("Quantidade de votos para o candidato Ambrosio Rutra:"))
Q2 = float(input("Quantidade de votos para o candidato Demelza Olecram:"))

x = (Q1 + Q2)



if(Q1>Q2):
	y = (Q1*100)/x
	print("Ambrosio Rutra")
	print(round(y,2))
	
else:
	z = (Q2*100)/x
	print("Demelza Olecram")
	print(round(z,2))