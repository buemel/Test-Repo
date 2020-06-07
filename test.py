# Syntax: Python 3.7
n = int(input('Fakultät von n = '))
f = 1
for i in range(1, n + 1):
    f *= i
print(f'{n}! = {f}')
