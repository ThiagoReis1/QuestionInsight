nome=input().lower()

if(nome=="aspartato"):
	print(round(4*12.011+6* 1.0079+1*14.0067+4*15.9994,2))
elif(nome=="fenilalanina"):
	print(round(9*12.011+11*1.0079+2*15.9994+1*32.066,2))
elif(nome=="tirosina"):
	print(round(9*12.011+11*1.0079+1*14.0067+3*15.9994,2))
else:
	print("Entrada: ",nome)
	print("Dado Invalido")
	