# faça seu código aqui!
alunos = int(input(""))
c = 0
tais = 0
edgar = 0
ana = 0

while c < alunos:
	candidato = input("").lower()
	if (candidato == "tais"):
		tais = tais + 1
		#c = c + 1
	
	if (candidato == "edgar"):
		edgar = edgar + 1
		#c = c + 1
	
	if (candidato == "ana"):
		ana = ana + 1
	c = c + 1
		
	
print("tais=", tais)
print("edgar=", edgar)
print("ana=", ana)