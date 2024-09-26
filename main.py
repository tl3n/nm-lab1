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

def bisection(f, a, b, eps):
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def get_q(a, b):
    return max(abs(dg(a)), abs(dg(b)))

def is_convergent(q, x0, delta):
    if (q >= 1):
        print("умова збіжності 1 не виконується")
        return false
    elif (abs(g(x0) - x0) > (1 - q * delta)):
        print("умова збіжності 2 не виконується")
        return false

    print("збіжність виконується")
    return true

def simple_iteration(g, x0, eps, q, max_iter = 1000):
    roots = []
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if (q < 0.5):
            if (abs(x_new - x)) <= (((1 - q) / q) * eps):
                return x_new, i
                #roots.append([x_new, i])
        elif (abs(x_new - x) <= eps):
            return x_new, i
            #roots.append([x_new, i])
        x = x_new
    #return max(roots[0])

eps = 1e-4
a, b = find_initial_interval()
x0 = bisection(f, a, b, eps)

# перевірка умов збіжності
q = get_q(a, b)
delta = min(abs(a - x0), abs(b - x0))
is_convergent = is_convergent(q, x0, delta)

# апріорна оцінка
apriori_iter = ceiling((ln((abs(g(x0) - x0)) / ((1 - q) * eps))) / (ln(1 / q))) + 1

print(apriori_iter)
print(simple_iteration(g, x0, eps, q))