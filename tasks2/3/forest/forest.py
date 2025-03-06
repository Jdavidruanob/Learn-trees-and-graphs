"""
Jose David Ruano Burbano 8982982
Tarea 3 - Forest
Arboles y grafos 2025-1

Analisis de complejidad:
Siendo N el numero de filas del bosque y M el numero de columnas:
- Exploracion de cada celda en la matriz (BFS): O(N * M)
- Ordenamiento de las especies por nombre y altura: O(K log K), donde K es la cantidad 
  de regiones distintas en el bosque.
En total, la complejidad es O(N * M + K log K), siendo el termino dominante O(N * M).
"""

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_mod_aux(x, y, matrix, vis, species):
    n, m = len(matrix), len(matrix[0])
    q = deque([(x, y)])
    vis[x][y] = True
    max_height = int(matrix[x][y].split('#')[1])
    
    while q:
        cx, cy = q.popleft()
        
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny]:
                tree_species, height = matrix[nx][ny].split('#')
                height = int(height)
                if tree_species == species:
                    vis[nx][ny] = True
                    q.append((nx, ny))
                    max_height = max(max_height, height)
    
    return max_height

def bfs_mod(n, m, matrix):
    vis = [[False] * m for _ in range(n)]
    species_heights = []
    
    for i in range(n):
        for j in range(m):
            if not vis[i][j]:
                species, _ = matrix[i][j].split('#')
                max_height = bfs_mod_aux(i, j, matrix, vis, species)
                species_heights.append((species, max_height))
    
    species_heights.sort()
    return species_heights

def main():
    t = int(sys.stdin.readline().strip())
    
    for case_num in range(1, t + 1):
        n, m = map(int, sys.stdin.readline().split())
        matrix = [sys.stdin.readline().strip().split() for _ in range(n)]
        
        species_heights = bfs_mod(n, m, matrix)
        
        print(f"Forest #{case_num}")
        for species, height in species_heights:
            print(species, height)

main()
