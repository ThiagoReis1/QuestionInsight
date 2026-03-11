def sorteio(n: int) -> str:
	if (n > 7):
		print("maior")
	elif (n < 7):
		print("menor")
	else:
		print("fortuna")
		
if __name__ == "__main__":
	n = int(input())
	sorteio(n)