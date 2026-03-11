# faça seu código aqui!
q_c = int(input())
combo = 50.0

if q_c >= 4:
	desconto = (combo * q_c) * 12/100 
	total = combo * q_c - desconto
else:
	total = combo * q_c
	
print(round(total, 1))