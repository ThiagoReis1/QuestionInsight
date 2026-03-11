n = input()

if (n.lower()=="alanina"):
	soma = (3*12.011)+(7*1.0079)+(1*14.0067)+(2*15.9994)
	print(round(soma,2))
elif(n.lower()=="valina"):
	soma= (5*12.011)+(11*1.0079)+(1*14.00674)+(2*15.9994)
	print(round(soma,2))
elif (n.lower()=="tirosina"):
	soma = (9*12.011)+(11*1.0079)+(1*14.0067)+(3*15.9994)
	print(round(soma,2))
else:
	print("Entrada: ",n)
	print("Dado Invalido")
