P=float(input())

if(0<P<=50.00):
	final=P+P
elif(50.01<=P<=100.00):
	final=P+P*0.5
elif(100.01<=P<=500.00):
	final=P+P*0.4
elif(P>500.00):
	final=P+P*0.3
else:
	final="Invalido"

print(round(final,2))	