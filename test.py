import sys
import sympy

n = 0
isprime = False
while True:
    n += 1
    isprime = sympy.isprime(n*n + n + 41)
    if not isprime:
        print("for n = %d NOT PRIME" % (n))
        break
    if n == 1000:
        print("reached %d" % (n))
        break
