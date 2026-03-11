s = float(input("valor do salario atual: "))

if(s < 1212):
	no = s + (s * 0.12)
elif(s >= 1212) and (s <= 5000):
	no = s + (s * 0.08)
elif(s > 5000):
	no = s + (s * 0.03)

print(round(no,2))