
x = float(input())

xx = x * x + 7

y = xx

while (y * y - xx > 0.0000001):
    y  =  0.5 * (y + xx / y)

print(y)