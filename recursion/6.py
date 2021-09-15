# Palindrome
def palindrome(n):
    if len(n) == 0:
        return True
    if n[0] != n[len(n) - 1]:
        return False
    else:
        return palindrome(n[1:-1])


print(palindrome("wooow"))
