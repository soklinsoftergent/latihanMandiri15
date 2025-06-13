def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Contoh penggunaan
print(is_palindrome("katak"))    # True
print(is_palindrome("python"))   # False
print(is_palindrome("kasur rusak")) # True