from sys import stdin
import heapq

def main():
    n, k = map(int, stdin.readline().split())
    
    while n != 0 and k != 0:
        count = {}  # Diccionario para contar repeticiones
        serials = {}  # Diccionario para guardar el numero de serie más alto

        for i in range(n):
            card, num = stdin.readline().split()
            num = int(num)
            if card in count:
                count[card] += 1
                serials[card] = max(serials[card], num)
            else:
                count[card] = 1
                serials[card] = num

        pq = []
        for card, freq in count.items():
                heapq.heappush(pq, (-freq, -serials[card], card)) 

        selected = []
        i = 0
        while i < k and pq:
            freq, serial, card = heapq.heappop(pq)
            selected.append((card, -freq))  # Restaurar frecuencia original
            i += 1
        selected.sort()
        for card, freq in selected:
            print(card, freq)
        n, k = map(int, stdin.readline().split())

main()
