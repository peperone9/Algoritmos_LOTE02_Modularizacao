#declarar
fib: int #proximo da sequencia
atual: int
anterior: int
i: int
n: int #quantidade de termos

#inicio
i = 0
n = int(input())
while(i < n):
	if(i < 2):
		fib = i
		anterior = fib - 1
		atual = fib
	else:
		fib = atual + anterior
		anterior = atual
		atual = fib
	print(fib)
	i += 1
#fim
