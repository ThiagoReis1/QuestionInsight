
tempo=float(input("tempo de investimento:"))
qf=1042000.00
q0=1500.00
i=((qf/q0)**(1/tempo))-1
print(round(i,5))

if(i<=0.01):
	print ("Real")

else:
	print ("Irreal")