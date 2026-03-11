p = float(input())
d = float(input())
c = int(input())
custo_p = 25.00
custo_d = 0.10

if c == 1:
	s = (p * custo_p + d * custo_d) * (1.0 + 0.17)
elif c == 2:
	s = (p * custo_p + d * custo_d) * (1.0 + 0.175)
elif c == 3:
	s = (p * custo_p + d * custo_d) * (1.0 + 0.18)
else:
	s = (p * custo_p + d * custo_d) * (1.0 + 0.20)
print(round(s,2))
	
