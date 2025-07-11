print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 25 de mayo del 2025                                      * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Peso de Hamming                                                  * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

"""
Descripción del ejercicio:
El peso de Hamming de un número es la cantidad de bits que están encendidos (es decir, cuántos '1' tiene su representación binaria).
Por ejemplo:
    hamming_weight(10) => binario: 1010  => 2 bits encendidos
    hamming_weight(21) => binario: 10101 => 3 bits encendidos

Restricción: No se pueden usar operaciones con cadenas como bin(), format(), str(), etc.
Se debe resolver usando operaciones matemáticas simples o bit a bit.
"""

def hamming_weight(n: int) -> int:
    """
    Esta función cuenta cuántos bits '1' hay en la representación binaria de un número entero positivo n.
    Para lograrlo, usa el operador AND (&) y desplazamiento a la derecha (//2), sin convertir a cadena.

    :param n: Número entero positivo
    :return: Cantidad de bits encendidos ('1') en su representación binaria
    """
    contador = 0
    while n > 0:
        # Si el bit menos significativo es 1, sumamos al contador
        if n % 2 == 1:    # También se puede usar: if n & 1:
            contador += 1
        n = n // 2        # Eliminamos el bit menos significativo y repetimos
    return contador



if __name__ == '__main__':
    print("Prueba 1: hamming_weight(10)  =>", hamming_weight(10))    # 2 (1010)
    print("Prueba 2: hamming_weight(21)  =>", hamming_weight(21))    # 3 (10101)
    print("Prueba 3: hamming_weight(0)   =>", hamming_weight(0))     # 0
    print("Prueba 4: hamming_weight(255) =>", hamming_weight(255))   # 8 (11111111)
    print("Prueba 5: hamming_weight(1)   =>", hamming_weight(1))     #  1 (1)


"""


- El peso de Hamming se puede calcular revisando los bits uno por uno usando divisiones sucesivas por 2.
- En vez de usar cadenas o funciones como bin(), usamos lógica matemática.
- El operador módulo (%) permite saber si el último bit es 1 o 0 (si es impar o par).
- También puede usarse el operador & (bit a bit) para comparar el último bit: `if n & 1`.
- n // 2 elimina el bit menos significativo y desplaza los bits hacia la derecha.
- El ciclo termina cuando el número llega a 0, lo que significa que ya no quedan bits por revisar.
- Esto demuestra que se puede trabajar con binarios sin necesidad de convertir a texto.

"""

