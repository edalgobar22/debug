"""
Números Abundantes
Son aquellos números en los que la suma de sus divisores propios es mayor que el
número mismo. Ejemplo: 12 (1 + 2 + 3 + 4 + 6 = 16).
El software debe mostrar la lista de los números abundantes que hay entre el rango
el usuario le indique. Los extremos iniciales y finales se pueden incluir en el listado
(si es el caso de que sean números abundantes).
"""
inicio = int(input("Ingrese el rango inicial: "))
final = int(input("Ingrese el rango final: "))

print("Los números abundantes son:")

for numero in range(inicio, final + 1):
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma > numero:
        print(numero, end=", ")