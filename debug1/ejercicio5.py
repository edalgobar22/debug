"""
Cree una función para comprobar múltiplos en ambas direcciones. Se adopta la
protección del divisor cero: nunca se efectúa una división entre cero. El cero es múltiplo
de cualquier entero no nulo. El escenario intercambia los argumentos en una segunda
llamada y muestra ambos retornos. Contrato: Comprobar múltiplos en ambas
direcciones: recibe dos enteros: primero el posible múltiplo y luego el divisor y devuelve
un valor lógico; falso si el divisor es cero o si no hay divisibilidad.
Fórmula o relación: Con divisor ≠ 0, es múltiplo cuando el residuo de la división es
cero; con divisor = 0 el retorno es falso.
"""

def comprobar_multiplo(numero, divisor):
    if divisor == 0:
        return False
    else:
        return numero % divisor == 0


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultado1 = comprobar_multiplo(a, b)
resultado2 = comprobar_multiplo(b, a)

print("¿El primer número es múltiplo del segundo?", resultado1)
print("¿El segundo número es múltiplo del primero?", resultado2)