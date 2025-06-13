def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

# Contoh penggunaan
print(sum_digits(234))   # 2 + 3 + 4 = 9
print(sum_digits(12345)) # 1 + 2 + 3 + 4 + 5 = 15