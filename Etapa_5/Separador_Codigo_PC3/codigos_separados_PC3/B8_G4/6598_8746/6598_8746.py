# faça seu código aqui!
n = int(input("numero: "))
c = input("Candidato: ").lower()

qa = 0
tais = 0
edgar = 0
ana = 0

while qa <= n:
	if c == "tais".lower():
		tais = tais + 1
		qa = qa + 1
	elif c == "edgar".lower():
		edgar = edgar + 1
		qa = qa + 1
	elif c == "ana".lower():
		ana = ana + 1
		qa = qa + 1
	
	c = input("candidato:").lower()
print("tais =",tais)
print("edgar =",edgar)
print("ana =", ana)
		
	
	