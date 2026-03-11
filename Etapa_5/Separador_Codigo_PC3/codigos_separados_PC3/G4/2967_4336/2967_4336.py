vis1 = float(input("Qual a altura do visitante? "))
vis2 = float(input("Qual a altura do acompanhante? "))

if (max(vis1 , vis2) >= 1.37):
	print("Sim")
else:
	print("Nao")
print(max(vis1 , vis2))