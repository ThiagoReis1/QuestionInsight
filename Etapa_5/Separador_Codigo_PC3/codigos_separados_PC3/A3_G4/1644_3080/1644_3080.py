from numpy import*
vnf= array(eval(input())) #pede as notas finais dos alunos
r=0 #variavel acumuladora de alunos reprovados
vi= zeros(r, dtype=int)
for x in vnf :
	if( x < 5):
		r= r + 1
print(r)

		
		
		
	