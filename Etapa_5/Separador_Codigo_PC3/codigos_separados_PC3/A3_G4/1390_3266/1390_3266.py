consumo= float(input("insira um valor:"))
tar= 1.20
taxa= 25.00
tar2= 1.40
if(consumo<= 100):
	soma= consumo * tar1
else:
    soma= consumo * tar2 + taxa
print(round(soma, 1))