print(''.join(list(reversed('abc'))))
s = 'abc'
print(s[::-1])
def is_palindrome(st):
    rev = ''.join(list(reversed(st)))
    return st == rev
print(is_palindrome('hello world'))
