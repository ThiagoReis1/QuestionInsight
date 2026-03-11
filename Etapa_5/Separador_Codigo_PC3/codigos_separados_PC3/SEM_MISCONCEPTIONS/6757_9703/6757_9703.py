pizza = int(input())
if pizza < 3:
	total = pizza * 5 + 3
elif pizza == 3:
	total = pizza * 5 + 3.25
else:
	total = pizza * 5 + 4.5
print(round(total, 2))