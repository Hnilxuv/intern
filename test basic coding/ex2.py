def drawshape(heigt):
    n = heigt
    for i in range(1, n+1):
        for j in range(1, 2*n+1):
            if i+j == n+2 or j-i == n:
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()

    for i in range(1, n+2):
        for j in range(1, 2*n+2):
            if i == j or i+j == n*2+2:
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()

if __name__ == "__main__":
    drawshape(6)