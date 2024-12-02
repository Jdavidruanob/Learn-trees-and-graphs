"""
Jose David Ruano Burbano
Tarea 1 - Entropy
Arboles y grafos 2024-2

Análisis de complejidad:
La complejidad temporal de este algoritmo es O(n * m), donde n es el número de palabras en la entrada
y m es el número de palabras unicas. Esto se debe a que en el peor de los casos, el algoritmo
recorre todas las palabras para contarlas y luego recorre todas las palabras únicas para calcular
la entropia
"""

import sys
import re
import math

def main():
    input_data = sys.stdin.read()
    delimiters = r'[,.:;!?"()\n\t\s]+'
    words = re.split(delimiters, input_data)
    word_counter = {}
    total_words = 0
    i = 0
    flag = True

    while i < len(words) and flag:
        # Guardamos la frecuencia de las palabras con ayuda de un diccionario
        word = words[i].lower()
        if word:
            word_counter[word] = word_counter.get(word, 0) + 1
            total_words += 1
        
        if word == '****end_of_text****':
            lambda_value = total_words - 1  
            et = 0
            # Hacemos los calculos 
            for key in word_counter:
                if key != '****end_of_text****':
                    pi = word_counter[key]
                    et += pi * (math.log10(lambda_value) - math.log10(pi))
            et /= lambda_value
            e_max = math.log10(lambda_value)
            e_rel = (et / e_max) * 100

            # Redondeamos para dara la salida correctamente
            et_ans = round(et, 1)
            e_rel_ans = round(e_rel)

            # Imprimimos la salida
            print(f'{lambda_value} {et_ans:.1f} {e_rel_ans}')
            
            # Reseteamos
            word_counter = {}
            total_words = 0
            i += 1 
        elif word == '****end_of_input****':
            flag = False
        else:
            i += 1 

if __name__ == '__main__':
    main()