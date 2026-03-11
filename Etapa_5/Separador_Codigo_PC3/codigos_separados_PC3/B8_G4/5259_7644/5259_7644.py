p = float(input("Valor da mensalidade: "))
n = int(input("Numero de criancas: "))
p1 = 0.10 * p
p2 = 0.30 * p
p3 = 0.40 * p
if(n == 1):
	vt = (p1 - p)
elif(n == 2):
	vt = (p2 - p)
elif(n >= 3):
	vt = (p3 - p)
print(round(vt * n * (-1), 2))
# p = 100
# x = 10%
#100x = p*10
#100/p*10
