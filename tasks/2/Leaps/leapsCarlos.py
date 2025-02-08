import sys
import math

n, eps = int(), 1e-8
d, h = [0 for _ in range(105)], [0 for _ in range(105)]

def isValid(theta, v):
    vx, vy, dx = v * math.cos(theta), v * math.sin(theta), 0
    i, flag = 0, True
    while flag and i < n: 
        t = dx / vx
        ht = vy * t - 9.8 * (t ** 2) / 2
        if ht < h[i] - eps: flag = False
        else:
            dx += d[i]
            t = dx / vx
            ht = vy * t - 9.8 * (t ** 2) / 2
            if ht < h[i] - eps: flag = False
        i += 1
    return flag

def main():
    global n, h, d
    line = sys.stdin.readline()
    while line != "":
        n, xmax = int(line), 0
        for i in range(n):
            h[i], d[i] = list(map(float, sys.stdin.readline().split()))
            xmax += d[i]
        l, r = 0, math.pi / 2
        while abs(r - l) > eps:
            mid = (l + r) / 2
            v = math.sqrt(xmax * 9.8  / math.sin(2 * mid))
            if isValid(mid, v): r = mid 
            else: l = mid
        
        print("%.2f %.2f" % (mid * 180 / math.pi, v) )
        line = sys.stdin.readline()
    

main()