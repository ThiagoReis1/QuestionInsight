x = input("S/N: ")
t = 0

while (x != S):
	if (x == "SIM"):
		mensagem = x 
		t = t + 1
	else:
		mensagem = x
	print(mensagem)
	num = input("S/N: ")
print(x + t)