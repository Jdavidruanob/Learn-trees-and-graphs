from collections import deque
from sys import stdin

# Movimientos posibles: Norte, Sur, Este, Oeste
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(grid, startA, startB, startC, targets, n):
    # Cola de BFS: almacenamos las posiciones de A, B, C y el tiempo
    queue = deque()
    visited = set()
    
    # Estado inicial: las posiciones de A, B, C y tiempo inicial 0
    queue.append((startA, startB, startC, 0))
    visited.add((startA, startB, startC))
    
    while queue:
        posA, posB, posC, time = queue.popleft()
        
        # Verificar si los tres robots han llegado a cualquier salida
        if posA in targets and posB in targets and posC in targets:
            return time
        
        # Intentar mover en las 4 direcciones para los tres robots simultáneamente
        for i in range(4):
            newA = (posA[0] + dx[i], posA[1] + dy[i])
            newB = (posB[0] + dx[i], posB[1] + dy[i])
            newC = (posC[0] + dx[i], posC[1] + dy[i])
            
            # Validar movimientos
            if not (0 <= newA[0] < n and 0 <= newA[1] < n and grid[newA[0]][newA[1]] != '#'):
                newA = posA  # Si A no puede moverse, se queda en el mismo lugar
            if not (0 <= newB[0] < n and 0 <= newB[1] < n and grid[newB[0]][newB[1]] != '#'):
                newB = posB  # Si B no puede moverse, se queda en el mismo lugar
            if not (0 <= newC[0] < n and 0 <= newC[1] < n and grid[newC[0]][newC[1]] != '#'):
                newC = posC  # Si C no puede moverse, se queda en el mismo lugar
            
            # Verificar que no colisionen entre sí (que dos robots no ocupen la misma celda)
            if len({newA, newB, newC}) < 3:
                continue  # Si hay una colisión, saltamos este movimiento
            
            # Si este estado no ha sido visitado, añadirlo a la cola
            newState = (newA, newB, newC)
            if newState not in visited:
                visited.add(newState)
                queue.append((newA, newB, newC, time + 1))
    
    # Si no se encuentra solución
    return -1

def main():
    t = int(stdin.readline().strip())  # Número de casos de prueba
    for case_num in range(1, t + 1):
        n = int(stdin.readline().strip())  # Dimensión del grid
        grid = []
        startA = startB = startC = None
        targets = []

        # Leer el grid y encontrar las posiciones iniciales y las salidas
        for i in range(n):
            line = stdin.readline().strip()
            grid.append(list(line))
            for j in range(n):
                if line[j] == 'A':
                    startA = (i, j)
                elif line[j] == 'B':
                    startB = (i, j)
                elif line[j] == 'C':
                    startC = (i, j)
                elif line[j] == 'X':
                    targets.append((i, j))

        # Ejecutar el BFS desde las posiciones iniciales
        result = bfs(grid, startA, startB, startC, targets, n)
        
        if result == -1:
            print(f"Case {case_num}: trapped")
        else:
            print(f"Case {case_num}: {result}")

main()
