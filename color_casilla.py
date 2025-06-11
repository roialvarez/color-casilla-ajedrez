"""
 Script que devuelve el color de la casilla de un tablero de ajedrez segun la 
 denominacion de la propia casilla, donde la columna ira de la a a la h y en 
 las filas de 1 a 8.
 La clave es que la casilla sera negra si el indice numerico de la columna 
 (para la a es 1) y el de la fila son ambos pares o ambos impares, si no 
 coinciden entonces la casilla sera blanca.
 Ejemplo la casilla b3 sera blanca
"""

columnas = "abcdefgh"
filas = "12345678"
flag = True

while flag == True:
    casilla = input("Introduce una casilla o pulsa cualquier tecla para salir: ")
    if len(casilla) == 2:
        c = casilla.lower()[0]
        f = casilla[1]
        if c in columnas and f in filas:
            if (columnas.index(c) % 2) == (filas.index(f) % 2):
                print(f"La casilla {casilla} es Negra")
            else:
                print(f"La casilla {casilla} es Blanca")
        else:
            print(f"La casilla {casilla} no es valida")
    else:
        flag = False
print("Saliendo")