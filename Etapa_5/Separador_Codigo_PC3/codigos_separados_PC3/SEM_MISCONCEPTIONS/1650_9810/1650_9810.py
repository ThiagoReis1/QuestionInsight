entrada=input()

contagens={'P':0,"C":0,'R':0, 'L':0, "B":0}
cores= entrada.split(',')
for cor in cores:
	if cor in contagens:
		contagens[cor]+=1

maiorn= max(contagens.values())
vetor_quantidade= [contagens['P'], contagens['C'], contagens['R'], contagens['L'], contagens['B']]

print(maiorn)
print(vetor_quantidade)