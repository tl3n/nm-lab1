from sympy import *
x = Symbol('x')

# наші рівняння та похідні
def f(x):
    return (sinh(x) - 12 * tanh(x) - 0.311).evalf()

df = lambdify(x, (sinh(x) - 12 * tanh(x) - 0.311).diff(x))

def g(x):
    return (asinh(12 * tanh(x) + 0.311)).evalf()

dg = lambdify(x, (asinh(12 * tanh(x) + 0.311)).diff(x))

# знаходження початкового інтервалу
def find_initial_interval():
    a, b = -10, 10
    while f(a) * f(b) > 0:
        a *= 2
        b *= 2
    return a, b

def get_q(a, b):
    return max(abs(dg(a)), abs(dg(b)))

a, b = find_initial_interval()

# перевірка умов збіжності
q = get_q(a, b)
x0 = (a + b) / 2
delta = min(abs(a - x0), abs(b - x0))

if (q >= 1):
    print("умова збіжності 2 не виконується")
elif (abs(g(x0) - x0) > (1 - q * delta)):
    print("умова збіжності 2 не виконується")
else:
    print("збіжність виконується")