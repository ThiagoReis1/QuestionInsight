sla = float(input("numero: "))

d1 = sla // 1000
s1 = sla % 1000
d2 = sla // 10
d3 = sla // 1

if (((d1 + s1)**2) == d3):
	print("atende")
	print(round(sla, ))
else:
	print("nao atende")
	print(round(sla, ))
