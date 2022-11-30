def my_function(*args, **kwargs):
    s = 0

    for param in args:
        if type(param) == int or type(param) == float:
            s += param
    return s

print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))


def f2(n):
    if n == 0:
        return 0, 0, 0

    total, even, odd = f2(n-1)
    total += n

    if n % 2 == 0:
        even += n
    else:
        odd += n

    return total, even, odd

n_total, n_even, n_odd = f2(5)
print('total = ', n_total)
print('even = ', n_even)
print('odd = ', n_odd)

def f3():
    x = input()

    try:
        x = int(x)
    except ValueError:
        x = 0

    return x

print(f3())