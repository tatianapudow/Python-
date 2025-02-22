
def find_palindrome(s):
    s_lower=s.lower()
    return s_lower == s_lower[::-1]
print(find_palindrome("Anna"))
print(find_palindrome("Sasha"))
