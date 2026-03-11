consumo= float(input("insira um valor:"))
tar= 0.60
taxa= 5.00
tar2= 0.75
taxa2= 16.00

if(consumo<= 150):
	soma= consumo * tar + taxa
else: 
   soma= consumo * tar2 + taxa2
print(round(soma, 1))
