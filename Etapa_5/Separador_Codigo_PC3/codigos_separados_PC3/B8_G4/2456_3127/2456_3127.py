vm = float(input("valor da mensalidade: "))
nc = int(input("numero de criancas: "))

if(nc==1):
	vt=(vm -(vm*0.10))
	print(vt)
elif(nc==2):
	vt=((vm*nc) - ((vm*nc)*0.30))
	print(vt)
elif(nc>=3):
	vt=((vm*nc) - ((vm*nc)*0.40))
	print(vt)
