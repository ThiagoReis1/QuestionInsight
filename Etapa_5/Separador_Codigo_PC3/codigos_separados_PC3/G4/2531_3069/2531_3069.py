vinicial = float(input("premio"))
m = float(input("saque"))
i =float(input("taxadejuros"))
t=0
if(not vinicial>0 or not m>0 or not i>0):
	print("Dados incorretos")
else:
	while(vinicial*(1+i/100)-m<=1.10*(vinicial*(1+i/100)-m+m)*vinicial**(-1)*(1+i/100)**(-1)*vinicial):
		vinicial =round(vinicial*(1+i/100)-m,2)
		t =t+1
print(t)	