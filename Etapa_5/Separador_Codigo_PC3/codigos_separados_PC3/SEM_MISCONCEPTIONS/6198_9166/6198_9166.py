h_aluno, t_aluno = float(input()), float(input())
h_luna, t_luna = 1.65, 0.02

i = 0
while (h_luna > h_aluno):
	h_aluno = h_aluno + t_aluno
	h_luna = h_luna + t_luna
	i = i + 1

print(i)