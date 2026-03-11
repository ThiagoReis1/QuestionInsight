com1 = int(input("combustivel em litros: "))
if (com1<17.5):
	t = (com1 + 0.8)
elif(com1>17.5) and (com1<35):
	t = (com1 + 1.3)
elif(com1>35.0) and (com1<50.0):
	t = (com1 + 2.1)
elif(com1>=50.0):
	t = (com1 + 3.0)
print(round(t,1))