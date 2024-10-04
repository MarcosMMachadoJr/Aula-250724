def fat(n):
  prod = 1
  for i in range(2, n + 1):
    prod *= i
  return prod

def comb(N, P):
  resultado = fat(N) / (fat(P) * fat(N - P))
  return resultado

print(comb(4, 9))
print(comb(7, 4))
print(comb(12, 4))
print(comb(9, 3))