def is_prime(n, divisor=None):
    if divisor is None:
        if n <= 1:
            return False
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

# Contoh penggunaan
print(is_prime(7))  # True
print(is_prime(10)) # False