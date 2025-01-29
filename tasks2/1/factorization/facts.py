from collections import deque
def factorize_non_recursive(n):
    """
    Genera las factorizaciones únicas de un número n usando un enfoque no recursivo.
    """
    queue = deque() # Pila para almacenar el estado del backtracking
    result = []  # Lista para almacenar las factorizaciones válidas

    # Inicializamos con el valor n y el primer factor (2)
    queue.append((n, 2, []))  # (valor restante, siguiente factor a probar, factores actuales)

    while queue:
        current, start, current_factors =   queue.pop()

        # Caso base: Si el valor restante es 1 y hay más de un factor, es una factorización válida
        if current == 1 and len(current_factors) > 1:
            result.append(current_factors[:])
            continue

        # Probar divisores desde el valor "start" hasta sqrt(current)
        for i in range(start, int(current**0.5) + 1):
            if current % i == 0:
                # Empujar nuevo estado a la pila
                queue.append((current // i, i, current_factors + [i]))

        # Caso especial: agregar el factor "restante" si es mayor que el último factor probado
        if current >= start and len(current_factors) > 0:
            result.append(current_factors + [current])

    return result


def main():
    import sys
    input = sys.stdin.read
    numbers = list(map(int, input().split()))
    
    for n in numbers:
        if n == 0:
            break

        # Obtener todas las factorizaciones de manera no recursiva
        factorizations = factorize_non_recursive(n)
        
        # Imprimir el número de factorizaciones
        print(len(factorizations))
        # Imprimir cada factorización
        factorizations.reverse()
        for factors in factorizations:
            for i, factor in enumerate(factors):
                if i > 0:
                    print(" ", end="")
                print(factor, end="")
            print()

main()