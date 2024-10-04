def calcular(n1, n2, op):


    if op == "+":
        soma = X + Y
        return soma
    elif op == "-":
        subtrair = X  Y
        return subtrair
    elif op == "/":
        divisao = X / Y
        return divisao
    elif op == "*":
        multiplicar = X * Y
        return multiplicar

X = int(input())
Y = int(input())
op = input()
print(calcular(X, Y, op))

