import sys, fractions, operator, functools

print (list(filter(lambda x : fractions.gcd(functools.reduce(operator.mul, list(range(2, x-1))) if x > 3 else 1, x)== 1, list(range(2, int(sys.argv[1]))))))
