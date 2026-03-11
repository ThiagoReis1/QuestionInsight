mensalidade=float(input(""))
criancas=int(input(""))

if(criancas==1):
	desc=(mensalidade*10)/100
	new_payment=(mensalidade-desc)
	
	
elif(criancas==2):
	desc=(mensalidade*30)/100
	new_payment=(mensalidade-desc)
	
elif(criancas==3 or criancas>3):
	desc=(mensalidade*40)/100
	new_payment=(mensalidade-desc)
	
print(new_payment*criancas)



