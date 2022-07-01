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

# Función suma hecha por Priscila Kwiatkowski
# La función recibe como parámetro la lista y devuelve la suma total de todos sus elementos.

total = 0

for number in lista:
    if number > 0:
     total += number
print("La suma total de todos los elementos es: ", total)