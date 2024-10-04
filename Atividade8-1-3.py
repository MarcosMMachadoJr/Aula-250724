def calcTriangulo(n1, n2, n3):

    triangulo = None
    if n1 == n2 == n3:
        triangulo = "equilatero"
        return triangulo

    elif ((n1 == n2) or (n1 == n3) or (n2 == n3)) and ((n1 > (n2 + n3) or (n2 > (n1 + n3) or (n3 > (n1 + n2))))):
        triangulo = "isoceles"
        return triangulo

    elif ((n1 != n2) or (n1 != n3) or (n2 != n3)) and ((n1 > (n2 + n3) or (n2 > (n1 + n3) or (n3 > (n1 + n2))))):
        triangulo = "escaleno"
        return triangulo

    else:
        triangulo = "nada"
        return triangulo


X = int(input())
Y = int(input())
Z = int(input())

print(calcTriangulo(X, Y, Z))

