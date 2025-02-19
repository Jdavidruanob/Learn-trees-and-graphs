""" 
Jose David Ruano Burbano 8982982
Tarea 2 - bit
Arboles y grafos 2025-1

Analisis de complejidad:
"""
from sys import stdin
def main():
  line = stdin.readline()
  while line != '#':
    format, rows, cols = map(int, line.split())
    
    line = stdin.readline()

main()