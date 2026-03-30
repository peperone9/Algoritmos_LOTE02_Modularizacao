#32. Receba um número inteiro. Calcule e mostre o seu fatorial.

#declarar
i: int
n: int = -1
fat: int

#inicio
i = 1
fat = 1

while(n < 0):
	n = int(input("Informe um número inteiro positivo para fatorial: "))

while(i <= n):
	fat *= i
	i += 1

print(str(n) + "! =", fat)
#fim

