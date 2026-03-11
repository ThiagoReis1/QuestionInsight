total=float(input(" "))
codigo=input()
if codigo=='D':
	final=total-(total*(19/100))
elif codigo=='P':
		final=total-(total*(19/100))
elif codigo == 'C':
		vezes=int(input())
		if vezes==2:
			final=total+(total*(9/100))
		else:
			final = total
print(round(final,2))