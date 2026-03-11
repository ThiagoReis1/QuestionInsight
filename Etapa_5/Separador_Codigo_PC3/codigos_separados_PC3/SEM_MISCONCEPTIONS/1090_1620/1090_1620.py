compra1 = float(input("valor da primeira compra: "))
compra2 = float(input("valor da segunda compra: "))
compra3 = float(input("valor da terceira compra: "))
compra4 = float(input("valor da quarta compra: "))

limite = float(input("limite do cartao: "))

ntotal = (compra1 + compra2 + compra3 + compra4)

print(round(ntotal, 2))

if (ntotal <= limite):
	  print("Sim")

else:
     print("Nao")