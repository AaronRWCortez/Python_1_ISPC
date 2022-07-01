lista = []

def main():
    pedir5()
    print(lista)

def pedir5():
# Función pedir5 hecha por Aaron Ramiro Waldemar Cortez
    
    i = 1
    while i <= 5:
        # La función pide 5 veces un número y lo va almacenando con cada vuelta en la lista
        numero = int(input("Ingrese el valor numero " + str(i) + ": "))
        lista.append(numero)
        i += 1

main()