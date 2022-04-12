def S(x,n):
    t = 1
    s = 0
    for i in range(1, n+1):
        t = t * x
        s = s + t
    return s

if __name__ == "__main__":
    print(S(3,3))