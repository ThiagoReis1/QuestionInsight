v = float(input("Velocidade:" ))

vf = v
t = 0

while (vf >= 40):
	t = t + 1
	vf = vf - 0.02*vf 

print(t)