from collections import deque
from sys import stdin
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

def ssspBFS(G, s1, s2, s3):
  q = deque()
  d, p = [float("inf") for _ in range(len(G))], [-1 for _ in range(len(G))]
  q.append(s1)
  q.append(s2)
  q.append(s3)
  d[s1] = d[s2] =d[s3]= 0

  while len(q) > 0:
    v = q.popleft()
    for u in G[v]:
      if d[u] == float("inf"):
        q.append(u)
        d[u] = d[v] + 1
        p[u] = v

  return d, p

def main():
    grid = []
    t = int(stdin.readline().strip())
    for i in range(t):
        n = int(stdin.readline().strip())
        for _ in range(n):
            line = stdin.readline().strip()
            grid.append(list(line))
        #print(grid)
        ans = 0
        print(f'case {i+1}: {ans}')      

main()