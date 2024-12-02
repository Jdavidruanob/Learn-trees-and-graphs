from sys import stdin
from collections import deque
di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

def ssspBfsMod(grid, si, sj, ti, tj, n, m):
    visited = [[[[False for _ in range(4)] for _ in range(5)] for _ in range(m)] for _ in range(n)]
    ans, flag, queue, visited[si][sj][0][0] = 0, False, deque(), True
    queue.append((si, sj, 0, 0))  # (x, y, color, dirección)

    while queue and not flag:
        for _ in range(len(queue)): # Procesamos todos los elementos del nivel actual
            i, j, color, d = queue.popleft()
            if i == ti and j == tj and color == 0:
                flag = True  # Flag para detenerse si ya se llego
            else:
                for aux in [1, 3]:  # 1 = 90 grados der - 3 = 90 grados izq
                    nextD = (aux + d) % 4
                    if not visited[i][j][color][nextD]:
                        visited[i][j][color][nextD] = True
                        queue.append((i, j, color, nextD))
                nextI = i + di[d]
                nextJ = j + dj[d]
                nextColor = (1 + color) % 5  # Cambiar de color
                if 0 <= nextI < n and 0 <= nextJ < m and grid[nextI][nextJ] != '#': # Pos valida
                    if not visited[nextI][nextJ][nextColor][d]:
                        visited[nextI][nextJ][nextColor][d] = True
                        queue.append((nextI, nextJ, nextColor, d))

        if not flag: ans += 1
    if not flag: ans = -1
    return ans

def main():
    n, m = map(int, stdin.readline().split()) # Lectura entrada
    case = 1
    flag = True
    while n != 0 and m != 0:
        grid = []
        for i in range (n):
            grid.append(list(stdin.readline().strip()))
            for j in range(len(grid[i])): # Obetener la pos de T y S
                if grid[i][j] == 'T': ti, tj = i, j
                if grid[i][j] == 'S': si, sj = i, j

        ans = ssspBfsMod(grid, si, sj, ti, tj, n, m)
        if not flag: print() # Impirimir correctamente la salida
        flag = False
        print(f"Case #{case}")
        if ans == -1: print("destination not reachable")
        else: print(f"minimum time = {ans} sec")
        case += 1
        n, m = map(int, stdin.readline().split())
main()