#36. Receba um número N. Calcule e mostre a série 
#1 + 1/1! + 1/2! + ... + 1/N!

#declaracao
s: float = 0
n: int
fat: int
i: int

#inicio
n = int(input("Termos da sequencia: "))

while(n <= 0):
	n = int(input("A sequencia tem de começar com pelo menos 1: "))

i = 1
fat = 1
while(i <= n):
	fat *= i
	s += 1/fat
	print(f"1/{i}! = {(1/fat):.5f}", sep=" ")
	print(f"{s:.5f}")
	print()
	i += 1


