
n = int(input("Cuantos elementos tendra el arreglo??"))
arreglo = []
for i in range(n):
    valor = input(f"ingresa el valor {i+1}:")
    arreglo.append(valor)

def invertir_arreglo(lista):
    return list(reversed(lista))
arreglo_invertido = invertir_arreglo(arreglo)

print("Arreglo original:", arreglo)
print("Arreglo invertido:", arreglo_invertido)



