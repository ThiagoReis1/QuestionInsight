vr=float(input("valor da renda da dona carla: "))
vp= float(input("valor da prestacao que ela paga por mes:"))
vh= vr*0.35
vc=vr+vh

if vp>=vr:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
