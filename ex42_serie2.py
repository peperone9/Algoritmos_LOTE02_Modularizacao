#42. Calcule e mostre a série 1+ 2/3 + 3/5 + ... + 50 /99
serie: float
numerador: int
denominador: int

serie = 1
numerador =  1
denominador = 1
while(numerador <= 50):
	print(f"{numerador}/{denominador}")
	print(serie, "\n")
	numerador += 1
	denominador += 2
	serie += numerador / denominador
print()
