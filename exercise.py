import random

def es_camaleon(numero):

    suma = 0
    for digito in str(numero):
        suma += int(digito)
    invertido = int(str(numero)[::-1])
    suma_es_par = (suma % 2 == 0)  
    invertido_div3 = (invertido % 3 == 0) 

    return suma_es_par, invertido_div3, suma, invertido

cantidad = int(input("Cantida de numeros a: "))

if cantidad == 4:
    numeros = [324, 518, 742, 901]
else:
    numeros = []
    for _ in range(cantidad):
        numeros.append(random.randint(100, 99999))

print("\nNúmeros a revisar:", numeros)
print("Resultados:\n")

for n in numeros:
    suma_par, invertido_div3, suma, invertido = es_camaleon(n)

    if suma_par and invertido_div3:
        print(f"{n} -> SI cumple (suma={suma} par, invertido={invertido} divisible por 3)")
    elif suma_par:
        print(f"{n} -> NO cumple (suma={suma} par, invertido={invertido} NO divisible por 3)")
    elif invertido_div3:
        print(f"{n} -> NO cumple (suma={suma} impar, invertido={invertido} divisible por 3)")
    else:
        print(f"{n} -> NO cumple (suma={suma} impar, invertido={invertido} NO divisible por 3)")
