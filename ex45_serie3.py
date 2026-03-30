#45. Calcule e mostre a série 1–2/4 + 3/9 –4 /16 + 5/25 + ... +
#15/225

#declarar
serie: float
numerador: int
denominador: int

#inicio
serie = 1
numerador = 1
denominador = numerador * numerador
while(numerador <= 15):
	print(f"{numerador}/{denominador}")
	print(f"{serie:.5f}", "\n")
	serie -= numerador/denominador
	numerador += 1
	denominador = numerador * numerador
