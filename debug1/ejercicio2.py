"""
Números perfectos
Son aquellos números que son iguales a la suma de sus divisores propios
(excluyendo el número mismo). Ejemplo: 6 (1 + 2 + 3 = 6), 28 (1 + 2 + 4 + 7 + 14 = 28).
Se espera que el interesado ingrese una serie de número enteros positivos mayores
que dos y después del ingreso de cada uno el programa indique si es un número
perfecto o no. Esta lista termina cuando el que introduce la lista digita un número
negativo.
"""
while True:
    numero = int(input("Ingrese un número: "))

    if numero < 0:
        print("Programa finalizado")
        break

    if numero <= 2:
        print("Ingrese un número mayor que 2")
        continue

    suma = 0

    for i in list(range(1, numero)):
        if numero % i == 0:
            suma += i

    if suma == numero:
        print("El número es perfecto", list)
    else:
        print("El número no es perfecto")