lista = []


def main():
    pedir5()
    print()


def pedir5():
    # Función pedir5 hecha por Aaron Ramiro Waldemar Cortez

    i = 1
    while i <= 5:
        # La función pide 5 veces un número y lo va almacenando con cada vuelta en la lista
        numero = int(input("Ingrese el valor numero " + str(i) + ": "))
        lista.append(numero)
        i += 1

# Función suma hecha por Priscila Kwiatkowski
# La función recibe como parámetro la lista y devuelve la suma total de todos sus elementos.


def suma():
    total = 0
    for number in lista:
        if number > 0:
            total += number
    print("La suma total de todos los elementos es: ", total)

# Función minimo hecha por Julián Rolón
# La funcion recorre la lista el imprime en consola el valor minimo entre sus elementos


def minimo():
    minimo = lista[0]
    for number in lista:
        if number < minimo:
            minimo = number
    print("El valor minimo de la lista es ", minimo)

# Función minimo hecha por Julián Rolón
# La funcion recorre la lista el imprime en consola el valor maximo entre sus elementos


def maximo():
    maximo = lista[0]
    for number in lista:
        if number > maximo:
            maximo = number
    print("El valor maximo de la lista es ", maximo)


main()
