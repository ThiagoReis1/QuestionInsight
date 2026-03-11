patP = float(input("Digite o valor do patrimônio Probesco: "))
patB = float(input("Digite o valor do patrimônio Bitcoin: "))
iP = float(input("Digite o percentual de crescimento Probesco: "))
iB = float(input("Digite o percentual de crescimento Bitcoin: "))
fP = patP
fB = patB
t = 1
while(fB < fP):
	rendP = fP * iP/100
	fP = fP + rendP
	rendB = fB * iB/100
	fB = fB + rendB
	t = t + 1
print(t)