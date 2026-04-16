def ordenamiento_burbuja(numeros):
	"""Ordena una lista de menor a mayor usando el algoritmo burbuja."""
	lista = numeros[:]  # Copia para no modificar la lista original
	n = len(lista)

	for i in range(n):
		intercambio = False
		for j in range(0, n - i - 1):
			if lista[j] > lista[j + 1]:
				lista[j], lista[j + 1] = lista[j + 1], lista[j]
				intercambio = True
		if not intercambio:
			break

	return lista


if __name__ == "__main__":
	datos = [64, 34, 25, 12, 22, 11, 90]
	print("Lista original:", datos)
	print("Lista ordenada:", ordenamiento_burbuja(datos))
