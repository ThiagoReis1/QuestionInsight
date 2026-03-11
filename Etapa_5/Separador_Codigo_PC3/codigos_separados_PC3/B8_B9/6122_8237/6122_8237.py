q_combustivel = float(input("Digite um valor:"))

if(q_combustivel < 17.5):
	Coaxium = 0.8
	total = q_combustivel + Coaxium
	print(round(total, 1))
elif(q_combustivel >= 17.5) and (q_combustivel < 35.0):
	Coaxium = 1.3
	total = q_combustivel + Coaxium
	print(round(total, 1))
elif(q_combustivel >= 35.0) and (q_combustivel < 50.0):
	Coaxium = 2.1
	total = q_combustivel + Coaxium
	print(round(total, 1))
elif(q_combustivel >= 50.0):
	Coaxium = 3.0
	total = q_combustivel + Coaxium
	print(round(total, 1))