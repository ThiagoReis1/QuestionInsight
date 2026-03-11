lanche = input("Queres coxinha ou esfirra? Digite C ou E: ")
quantidade_lanche = int(input("Quantas vai querer? "))
quantidade_suco = int(input("Quantos copos de suco vai querer? "))

if (lanche.upper () == "C"):
	print(round(quantidade_lanche * 2 + quantidade_suco * 6, 1))
else:
	print(round(quantidade_lanche * 4.5 + quantidade_suco * 6, 1))