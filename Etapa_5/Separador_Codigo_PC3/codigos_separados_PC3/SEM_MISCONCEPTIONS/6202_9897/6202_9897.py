altura_bia = 1.69
taxa_bia = 0.01

h_p = float(input('altura atual: '))
tx = float(input('taxa de crescimento: '))

cont = 0 #anos

while altura_bia > h_p:
	altura_bia = altura_bia + taxa_bia
	h_p = h_p + tx
	cont += 1
print(cont)