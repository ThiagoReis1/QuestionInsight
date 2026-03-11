he=float(input(":"))
nf=float(input(":"))

h=he-(2/3)*nf

if(he<0 or nf<0):
	print("Entradas:", round(he,2),"horas extras" ,"e" ,nf ,"horas de falta")
	print("Dados invalidos")
elif(h>2400):
	s= 500.0
	print("Entradas:", round(he,2),"horas extras" ,"e" ,nf ,"horas de falta")
	print("Gratificacao: R$", round(s,1))
elif(h>1800 and h<2400):
	s= 400.0
	print("Entradas:", round(he,2) ,"horas extras","e" ,nf ,"horas de falta")
	print("Gratificacao: R$", round(s,1))
elif(h>1200 and h<1800):
	s= 300.0
	print("Entradas:", round(he,2),"horas extras" ,"e" ,nf ,"horas de falta")
	print("Gratificacao: R$", round(s,1))
elif(h>600 and h<1200):
	s= 200.0
	print("Entradas:", round(he,2) ,"horas extras","e" ,nf ,"horas de falta")
	print("Gratificacao: R$", round(s,1))
elif(h<600):
	s= 100.0
	print("Entradas:", round(he,2),"horas extras" ,"e" ,nf ,"horas de falta")
	print("Gratificacao: R$", round(s,1))