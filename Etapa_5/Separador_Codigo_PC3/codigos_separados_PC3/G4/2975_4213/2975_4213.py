a=int(input("Sucos:"))
b=int(input("Salgados:"))
c=float(input("Valor disponivel:"))
valortotal= a*3+b*3.5
if(valortotal>c):
	print(valortotal)
	print("Nao")
else:
	print(valortotal)
	print("Sim")