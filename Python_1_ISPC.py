lista = []


def main():
    pedir5()
    print("Los numero ingresados son:",lista)
    menu_1()
    menu_2()


def pedir5():
    # Función pedir5 hecha por Aaron Ramiro Waldemar Cortez

    i = 1
    while i <= 5:
        # La función pide 5 veces un número y lo va almacenando con cada vuelta en la lista
        numero = int(input("Ingrese el valor número " + str(i) + ": "))
        if is_int(numero):
            lista.append(numero)
            i += 1
        else:
            print("¡Ese valor no es un entero!")


def is_int(string):
    #Comprueba si el numero es un entero
    try: 
        int(string)
        return True
    except ValueError:
        return False

def menu_1():
    opcion = 0
    while opcion < 1 or opcion > 6:
        opcion = input("""
    +-----------------------+
    |  ¿Que desea realizar? |
    | 1) Suma               |
    | 2) Promedio           |
    | 3) Máximo             |
    | 4) Mínimo             |
    | 5) Cambiar Números    |
    | 6) Cerrar             |
    +-----------------------+
        Su respuesta: """)

        if is_int(opcion):
            
            opcion = int(opcion)
            if opcion == 1:
                print("La suma total de todos los elementos es: ", suma(lista))
            elif opcion == 2:
                print("el promedio es: ",promedio(lista))
            elif opcion == 3:
                print("El valor máximo de la lista es ", maximo(lista))
            elif opcion == 4:
                    print("El valor mínimo de la lista es ", minimo(lista))
            elif opcion == 5:
                lista.clear
                pedir5()
                opcion = 0
            elif opcion == 6:
                print("Cerrando...")
            else:
                print("esa opción no se encuentra disponible")
                opcion = 0
        else:
            print("Por favor ingrese un número entero")
            opcion = 0

def menu_2():
    opcion = 0
    while opcion < 1 or opcion > 3:
        opcion = input("""
    +---------------------------+
    |   ¿Que desea realizar?    |
    |  1) Hacer otra operación  |
    |  2) Cambiar Números       |
    |  3) Cerrar                |
    +---------------------------+
            Su respuesta: """)

        if is_int(opcion):
            opcion = int(opcion)
            if opcion == 1:
                menu_1()
                opcion = 0
            elif opcion == 2:
                lista.clear
                pedir5()
                menu_1()
                opcion = 0
            elif opcion == 3:
                print("Cerrando...")
            else:
                print("esa opción no se encuentra disponible")
                opcion = 0
        else:
            print("Por favor ingrese un número entero")
            opcion = 0

# Función suma hecha por Priscila Kwiatkowski
# La función recibe como parámetro la lista y devuelve la suma total de todos sus elementos.


def suma(numeros):
    total = 0
    for number in numeros:
            total += number
    return total

# Función minimo hecha por Julián Rolón
# La funcion recorre la lista e imprime en consola el valor minimo entre sus elementos


def minimo(numeros):
    minimo = numeros[0]
    for number in numeros:
        if number < minimo:
            minimo = number
    return minimo

# Función minimo hecha por Julián Rolón
# La funcion recorre la lista e imprime en consola el valor maximo entre sus elementos


def maximo(numeros):
    maximo = numeros[0]
    for number in numeros:
        if number > maximo:
            maximo = number
    return maximo


#Función promedio hecha por Eric Diaz
#la función recorre la lista e imprime el promedio de los números ingresados


def promedio(numeros):
    prom = sum(numeros) / len(numeros)  
    return prom


main()
