altura = float(input("Digite: "))
tc = float(input("Digite: "))

am = 1.4
tcm = 0.06
tempo = 0

while altura > am:
	altura += tc
	am += tcm
	
	tempo += 1
	
print(tempo)