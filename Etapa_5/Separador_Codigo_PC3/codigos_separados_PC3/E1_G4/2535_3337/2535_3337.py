DA = float(input())
DB = float(input())
jA = float(input())
jB = float(input())
t = 0

if DA<=0 or DB <= 0 or jA <= 0 or jB <= 0 or DA <= DB or jA >= jB:
	print("Dados incorretos")
else:
	while DA >= DB:
		t = t + 1
		DA = round(DA + DA*jA/100, 2)
		DB = round(DB + DB*jB/100, 2)
		
	print(t)
	
	