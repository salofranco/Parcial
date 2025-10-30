def invertir_arreglo(lista):
    return lista[::-1]

def main():
    n = int(input("¿Cuántos elementos tendrá el arreglo?: "))
    arreglo = []
    for i in range(n):
        valor = input(f"Ingresa el valor {i+1}: ")
        arreglo.append(valor)
    arreglo_invertido = invertir_arreglo(arreglo)

    print("\nArreglo original:", arreglo)
    print("Arreglo invertido:", arreglo_invertido)
    
if __name__ == "__main__":
    main()




