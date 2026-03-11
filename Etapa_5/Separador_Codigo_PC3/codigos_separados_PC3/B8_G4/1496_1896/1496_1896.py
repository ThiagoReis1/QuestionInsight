T=int(input("Informe o tempo de voo:"))
if(T>-1 and T<101):
	VT=float((T*80.00)+3000.00)
elif(T>100 and T<201):
	VT=float((T*90.00)+4000.00)
elif(T>200 and T<301):
	VT=float((T*100.00)+5000.00)
elif(T>300):
	VT=float((T*110.00)+6000.00)
	
print("",round(VT,2))