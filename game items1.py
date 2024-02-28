def v1(x):
    if x > 3:
        print('========error========')
        print('only up to level 3')
        return None
    p, q, k, d = 2*x, 2, 2, 2
    if x in [2, 3]:
        multiplier = 3 if x == 2 else 6
        q *= multiplier
        k *= multiplier
        d *= multiplier
    return p, q, k, d

print('1,2,3')
x = int(input('selected level : '))
result = v1(x)
if result is not None:
    print(f'level selected: {x}')
    p, q, k, d = result
    print(f'swiss knife: {p}, tulip scope: {q}, nikop: {k}, pss: {d}')