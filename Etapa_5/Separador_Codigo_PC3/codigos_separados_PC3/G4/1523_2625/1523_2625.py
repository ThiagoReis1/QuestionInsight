qi = int(input(" "))
q_c = int(input(" "))
q_d = int(input(" "))

t = 0
quant = qi
while(quant < 200):
	x = q_c - q_d
	quant = quant + x
	t = t + 1
print(t)
	