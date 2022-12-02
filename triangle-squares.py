import time


line = int(input("Üçgen kenar uzunluğu: "))


def createTriangle(line):
    square = "#"
    triangle = ""
    n = 0

    for i in range(1, line+1):
        n += 1
        triangle += " " * (line - n)
        for j in range(0, n):
            triangle += square
            triangle += " "
        triangle += "\n"
    return triangle


triangle = createTriangle(line)

START_TIME = time.time()
print(triangle)
END_TIME = time.time() - START_TIME

print("--- %s seconds ---" % (END_TIME))
