lancamento = int(input("Face: "))
total_6=0
total_lancamentos=0
while lancamento !=  -1:
	total_lancamentos += 1 
	
	if lancamento == 6:
		total_6 += 1
		
	lancamento = int(input("Face: "))


if total_lancamentos!=0: 
	print(total_lancamentos)
	print(round((total_6/total_lancamentos)*100,2))