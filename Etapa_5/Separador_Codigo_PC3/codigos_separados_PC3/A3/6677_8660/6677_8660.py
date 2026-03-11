projetos_concuidos = []
for i in range (10):
	projeto = int(input())
	if projeto >= 0 and projeto <=20:
		projetos_concluidos.append(projeto)
	minimo_aprovacao = int(input())

aprovados = 0

projetos_acima_minimo = []
for projeto in projetos_concluidos:
	if projeto >= minino_aprovacao:
		aprovados += 1
		projetos_acima_minimo.append(projeto)

print(aprovados)
print(aprovado_acima_minimo)