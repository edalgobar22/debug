"""
Tu programa recogerá los datos emitidos por un dispositivo que detecte la
Temperatura. Dichos datos, por el momento, son introducidos por el operador
manualmente. Además, deberá avisar a los biólogos cuando la temperatura sea muy
baja con un mensaje que diga “T. baja”, cuando la temperatura sea normal “T.
normal”, y cuando la temperatura sea muy alta, “T. alta”. Si quieres, puedes
inventar iconos (en modo texto) que reemplacen los textos pero que resulten
evidentes para quien observa.
"""
temp = int(input("Indique la temperatura en °C: "))
if temp >= 26 and temp <= 34:
    print("T. normal")
elif temp > 34:
    print("T. alta")
else:
    print("T. baja")    