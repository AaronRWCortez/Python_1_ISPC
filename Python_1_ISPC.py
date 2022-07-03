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
# La funcion recorre la lista e imprime en consola el valor minimo entre sus elementos


def minimo():
    minimo = lista[0]
    for number in lista:
        if number < minimo:
            minimo = number
    print("El valor minimo de la lista es ", minimo)

# Función minimo hecha por Julián Rolón
# La funcion recorre la lista e imprime en consola el valor maximo entre sus elementos


def maximo():
    maximo = lista[0]
    for number in lista:
        if number > maximo:
            maximo = number
    print("El valor maximo de la lista es ", maximo)


#Función promedio hecha por Eric Diaz
#la función recorre la lista e imprime el promedio de los números ingresados


def promedio():
    print("¿cuántos números deseas ingresar? ")
    n = int(input())
    i = 0

    while i < n:
        print("valor número: ",i+1)
        val = float(input())
        lista.append(val)
        i+=1
    prom = sum(lista) / len(lista)

    print("el promedio es: ",prom)  



main()
