pop_i=int(input())
ct=float(input())
rt=int(input())
ano=1
nt=0
pop=0

while pop_i > 0:
	pop_i = pop_i + pop_i*ct - rt - 500
	ano=ano+1
print(ano)