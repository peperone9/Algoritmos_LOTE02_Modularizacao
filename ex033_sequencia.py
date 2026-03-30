#33. Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 +
# ... + 1/N.

#declarar
i: int
n: int
s: int = 0  #somatoria sequencia

#inicio
i = 1
n = 0

while(n < 1):
	n = int(input("Digite um numero maior 0 para iniciar a sequencia: "))

while(i <= n):
	s += 1/i
	print(f"1/{i} = {(1/i):.5f}")
	print(f"{s:.5f}")
	print()
	i += 1
print()
#fim
