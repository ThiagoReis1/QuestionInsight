num = int(input("numero:"))
soma = 0
rodadas = 1
while(num < 6):
	soma = soma + num
	num = int(input("numero:"))
	rodadas = rodadas + 1
print(rodadas)