av = input(' voce gostou do nosso atendimento ?').upper()
like = 0
while(av!='S'):
	if av=='SIM':
		like = like+1
		av = input(' voce gostou do nosso atendimento ?').upper()
		
	if av=='NAO':
		like = like 
		av = input(' voce gostou do nosso atendimento ?').upper()
print(like)
		