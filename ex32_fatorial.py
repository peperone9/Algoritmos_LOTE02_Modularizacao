#32. Receba um número inteiro. Calcule e mostre o seu fatorial.

#declarar
n: int = -1
fat: int


def ler_fatorial(n) -> int:
	while(n < 0):
		n = int(input("Informe um número inteiro positivo para fatorial: "))
	return n 

def fatorial(n: int) -> int:
	fat = 1
	i = 1
	while(i <= n):
		fat *= i
		i += 1
	return fat

def main():
	global n
	global fat 

	n = ler_fatorial(n)
	fat = fatorial(n)
	print(str(n) + "! =", fat)
main()
