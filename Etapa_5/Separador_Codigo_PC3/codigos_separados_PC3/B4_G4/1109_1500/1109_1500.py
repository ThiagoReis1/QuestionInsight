x= int(input("digite sua idade:"))
m= float(input("digite seu peso:"))

print("Entradas:",x,"anos e",m, "kg")
if(x>=12)and(x<=130)and(m>=60):
		 print("Dosagem: 1000 mg")
elif(x>=12)and(x<=130)and(m<60):
		 print("Dosagem: 875 mg")
elif(x<12)and(x>=0)and(m<=5):
	    print("Dosagem: 75 mg")
elif(x<12)and(x>=0)and(m>5)and(m<=9):
	    print("Dosagem: 125 mg")
elif(x<12)and(x>=0)and(m>5)and(m<=9):
	    print("Dosagem: 75 mg")
elif(x<12)and(x>=0)and(m>19)and(m<=16):
	    print("Dosagem: 250 mg")
elif(x<12)and(x>=0)and(m>16)and(m<=24):
	    print("Dosagem: 375 mg")
elif(x<12)and(x>=0)and(m>24)and(m<=30):
	    print("Dosagem: 500 mg")
elif(x<12)and(x>=0)and(m>5):
	    print("Dosagem: 750 mg")
else:
	print("Dados invalidos")
			


	