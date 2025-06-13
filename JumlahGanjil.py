def sum_odd_series(n):
    if n == 1:
        return 1
    if n % 2 == 0:  # Jika genap, cari bilangan ganjil sebelumnya
        return sum_odd_series(n - 1)
    return n + sum_odd_series(n - 2)

# Contoh penggunaan
print(sum_odd_series(7))  # 1 + 3 + 5 + 7 = 16
print(sum_odd_series(10)) # 1 + 3 + 5 + 7 + 9 = 25