"""
Jose David Ruano Burbano
Parcial 1 - Parte practica - Gems
Arboles y grafos 2024-2
Universidad Pontificia Javeriana cali
"""

from sys import stdin
from collections import deque
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

def bfs_mod(mapa, posi, posj):
    q, gems = deque(), 0  # Cola y contador de gemas que recoge el jugador
    vis = [[False for _ in range(len(mapa[0]))] for _ in range(len(mapa))] 
    vis[posi][posj] = True  
    q.append((posi, posj))  
    
    while len(q) > 0:
        x, y = q.popleft()
        if mapa[x][y] == 'G': # recoger gema
            gems += 1

        flag = True # bandera para saber si la posición es segura
        # Verificamos si la pos actual es segura
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]) and mapa[nx][ny] == 'T':
                flag = False

        # si es seguro el guerrero continua moviendose
        if flag:
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]) and not vis[nx][ny] and mapa[nx][ny] != '#':
                    vis[nx][ny] = True
                    q.append((nx, ny))

    return gems

def main():
    line = stdin.readline()
    while line != "": # Leemos hasta el EOF
        # Leemos la entrada 
        w, h = map(int, line.split())
        rows, cols = h, w
        mapa = []
        for _ in range(rows):
            linea = stdin.readline().strip()
            mapa.append(list(linea))
        
        # Obtener las pos incial del jugador
        player_posi , player_posj = None, None
        i = 0 
        while i < len(mapa) and player_posi == None:
            j = 0
            while j < len(mapa[i]) and player_posi == None:
                if mapa[i][j] == "P":
                    player_posi, player_posj = i, j
                j += 1
            i += 1
        
        # Obtener las gemas que puede recoger de manera segura en el mapa
        gems = bfs_mod(mapa, player_posi, player_posj)
        # Imprimimos la salida 
        print(gems)
        line = stdin.readline()

main()