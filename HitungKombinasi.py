def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combination(n, k):
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n - k))

def combination_recursive(n, k):
    if k == 0 or k == n:
        return 1
    return combination_recursive(n - 1, k - 1) + combination_recursive(n - 1, k)

# Contoh penggunaan
print(combination(5, 2))          # 10
print(combination_recursive(5, 2)) # 10
print(combination(10, 3))         # 120