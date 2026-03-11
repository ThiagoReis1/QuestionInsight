ataq = input("qual o ataque:")
num = int(input("rodas:"))
dano1 = int(input("dano 1:"))
dano2 = int(input("dano 2:"))

constricao = num *(dano1 + dano2 +1)  
polen = (dano1*dano2)
if (ataq == "polen"):
	print(int(polen))
else:
	print(int(constricao))
