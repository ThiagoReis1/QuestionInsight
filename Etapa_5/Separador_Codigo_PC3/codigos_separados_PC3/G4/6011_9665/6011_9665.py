Vrc = float(input("digite a renda da dona Carla: "))
Vp = float(input("digite o valor da prestacao: "))

Vr = Vrc * 0.35

if Vp > Vr:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")