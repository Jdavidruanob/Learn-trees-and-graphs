""" 
Jose David Ruano Burbano 8982982
Tarea 2 - weights
Arboles y grafos 2025-1

Analisis de complejidad:
La complejidad temporal de este algoritmo es O(n log m), donde:
- n es la longitud de las filas de pesas
- m es el peso maximo entre todas las pesas

Esto se debe a que:
La busqueda binaria (search) realiza O(log m) iteraciones, donde m es el peso maximo
En cada iteracion de la busqueda binaria:
   - bool_organize hace O(n) operaciones al recorrer las filas y buscar posiciones
   - La creacion del set de pesos unicos es O(n)

Por lo tanto, la complejidad total es O(n log m) ya que en cada una de las O(log m) 
iteraciones de la busqueda binaria realizamos O(n) operaciones.

"""
from sys import stdin

def bool_organize(max_w, r1, r2):
  r1_copy, r2_copy = r1[:], r2[:]
  weights = list(set(r1_copy + r2_copy))
  ans = True
  i = 0
  
  while i < len(weights) and ans:
    w = weights[i]
    if w > max_w and ans:
      r1_pos = []
      for j in range(len(r1_copy)):
        if r1_copy[j] == w:
          r1_pos.append(j)

      r2_pos = []
      for j in range(len(r2_copy)):
        if r2_copy[j] == w:
          r2_pos.append(j)
      if len(r1_pos) > 0 and len(r2_pos) > 0:
        ans = False
    i += 1
  return ans
      
def search(r1, r2):
  l, r  = 0, max(max(r1),max(r2)) 
  ans = r
  while l <= r:
    mid = (l + r) // 2
    
    if bool_organize(mid, r1, r2):
      ans = mid
      r = mid - 1
    else:
      l = mid + 1
  return ans

def main():
  line = stdin.readline()
  while line != "":
    r1 = list(map(int, stdin.readline().split()))
    r2 = list(map(int, stdin.readline().split()))
    ans = search(r1, r2)
    print(ans)
    line = stdin.readline()


main()