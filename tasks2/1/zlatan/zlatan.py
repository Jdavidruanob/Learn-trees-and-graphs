""" Jose David Ruano Burbano 8982982 """
from sys import stdin
import heapq

def main():
    n, k = map(int, stdin.readline().split())
    
    while n != 0 and k != 0:
        count = {} 
        serials = {}  

        for i in range(n):
            card, num = stdin.readline().split()
            num = int(num)
            if card in count:
                count[card] += 1
            else:
                count[card] = 1
                serials[card] = num

        pq = []
        for card, freq in count.items():
                heapq.heappush(pq, (-freq, -serials[card], card)) 

        ans = []
        i = 0
        while i < k and pq:
            freq, serial, card = heapq.heappop(pq)
            ans.append((card, -freq)) 
            i += 1
        ans.sort()
        for card, freq in ans:
            print(card, freq)
        n, k = map(int, stdin.readline().split())

main()
