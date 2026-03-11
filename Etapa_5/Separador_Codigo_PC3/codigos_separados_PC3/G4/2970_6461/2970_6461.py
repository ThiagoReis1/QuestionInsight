t = int(input("Tempo em meses: "))

Q0 = 1500
Qf = 1042000

i = ((Qf / Q0) ** (1 / t)) - 1

print(round(i, 5))

if i <= 0.01:
	print("Real")
	
else:
	print("Irreal")
	
