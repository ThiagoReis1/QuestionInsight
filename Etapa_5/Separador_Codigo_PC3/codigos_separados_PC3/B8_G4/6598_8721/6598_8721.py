# faça seu código aqui!
n = int(input("Qual a quantidade de alunos?: "))
p = input("Digite o nome do melhor professor: ").lower()
t = 0
e = 0
a = 0
c = 0
if p == "tais":
	t = t + 1
elif p == "edgar":
	e = e + 1
elif p == "ana":
	a = a + 1
c = c + 1
while  c  <  n :
	p = input("Digite o nome do melhor professor: ").lower() 
	if p == "tais":
		t = t + 1
	elif p == "edgar":
		e = e + 1
	elif p == "ana":
		a = a + 1
	c = c + 1
print ("tais=", t)
print ("edgar=", e)
print("ana=", a)
