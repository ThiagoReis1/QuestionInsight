e = input()
qtd=int(input())
acai=int(input())
total=0
if e.upper()=='T':
	total+=(4.5*qtd)+(acai*12)
else:
	total+=(5*qtd)+(acai*12)
print(round(total,1))