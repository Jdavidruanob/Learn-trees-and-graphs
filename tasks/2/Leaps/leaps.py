
"""
Jose David Ruano Burbano
Tarea 2 - Leaps
Arboles y grafos 2024-2

Análisis de complejidad:
La complejidad temporal de este algoritmo es O(n * log(epsilon)), donde n es el número de edificios,
y epsilon es la precisión deseada. Esto se debe a que el método de bisección reduce el intervalo de búsqueda
a la mitad en cada iteración, y en cada iteración se realiza un recorrido lineal de los edificios.
"""
import sys
import math

num_buildings, epsilon = int(), 1e-8
distances, heights = [0 for _ in range(105)], [0 for _ in range(105)]

def main():
    global num_buildings, heights, distances
    # Leer los la entrada 
    input_line = sys.stdin.readline()
    while input_line != "": # leemos hasta el EOF
        num_buildings, total_distance = int(input_line), 0 # Inicializamos las variables
        for i in range(num_buildings): # Para la cantidad de edificion hacemos 
            heights[i], distances[i] = list(map(float, sys.stdin.readline().split())) # Leemos la altura y la distancia
            total_distance += distances[i] # Sumamos la distancia total
        
        left, right = 0, math.pi / 2 # limites en los que va a estar el angulo
        while abs(right - left) > epsilon: # Mientras la diferencia entre los limites sea mayor a la precis
            mid_angle = (left + right) / 2 # Calculamos el angulo medio
            initial_velocity = math.sqrt(total_distance * 9.8 / math.sin(2 * mid_angle)) # V(t) = sqrt(d * g / sin(2 * theta))
            
            flag = True # Bandera para saber si el angulo es valido
            current_distance = 0
            i = 0

            while i < num_buildings and flag: # Mientras no hayamos recorrido todos los edificios y la bandera sea verdadera
                
                # verificar que superman puede pasar la primera altura del edificio
                time = current_distance / (initial_velocity * math.cos(mid_angle)) # Calculamos el tiempo
                height_at_time = initial_velocity * math.sin(mid_angle) * time - 4.9 * (time ** 2) # Calculamos la altura
                
                if height_at_time < heights[i] - epsilon: # Si la altura es menor a la del edificio actual menos la precisión
                    flag = False # La bandera se vuelve falsa porque superman no puede pasar
                    
                # verificar que superman puede pasar la segunda altura del edificio
                current_distance += distances[i] # Sumamos la distancia recorrida
                time = current_distance / (initial_velocity * math.cos(mid_angle)) # Calculamos el tiempo
                height_at_time = initial_velocity * math.sin(mid_angle) * time - 4.9 * (time ** 2) # Calculamos la altura
                
                if height_at_time < heights[i] - epsilon: # Si la altura es menor a la del edificio actual menos la precisión
                    flag = False # La bandera se vuelve falsa porque superman no puede pasar 
                i += 1
            
            if flag:
                right = mid_angle
            else:
                left = mid_angle
        
        angle_degrees = mid_angle * 180 / math.pi # Convertimos el angulo a grados
        print(f"{angle_degrees:.2f} {initial_velocity:.2f}")
        input_line = sys.stdin.readline()


main()
