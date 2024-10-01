from sympy import *

def f(x):
    return (sinh(x) - 12 * tanh(x) - 0.311).evalf()

#df = lambdify(x, (sinh(x) - 12 * tanh(x) - 0.311).diff(x))
def df(x):
    return (cosh(x) - (12 / cosh(x) ** 2)).evalf()

def ddf(x):
    return ((24 * sinh(x)) / (cosh(x) ** 3) + sinh(x)).evalf()

def phi(x):
    return (asinh(12 * tanh(x) + 0.311)).evalf()

def dphi(x):
    return ((12 * sech(x) ** 2) / (sqrt(144 * (tanh(x) + 0.0259187) ** 2 + 1))).evalf()

def simple_iteration(x0, eps, q):
    x = x0
    i = 0
    while True:
        x_new = phi(x)
        i += 1
        print("Ітерація: ", i, "| xn = ", x_new)
        if (q < 0.5):
            if (abs(x_new - x)) <= (((1 - q) / q) * eps):
                print("Корінь знайдено")
                return x_new, i
        elif abs(x_new - x) <= eps:
            print("Корінь знайдено")
            return x_new, i
        x = x_new

def modified_newton(x0, eps):
    x = x0
    i = 0
    dfx0 = df(x0)
    while True:
        x_new = x - f(x) / dfx0
        i += 1
        print("Ітерація: ", i, "| xn = ", x_new)
        if (abs(x_new - x) <= eps):
            print("Корінь знайдено")
            return x_new, i
        x = x_new

# Знаходимо початковий інтервал
a, b = 3, 4
x0 = 3.5 # Початкове наближення
eps = 1e-4

# Метод простої ітерації
# Перевірка умов збіжності
q = max(abs(dphi(a)), abs(dphi(b)))
print("Метод простої ітерації:")
apriori_simple_iter = ceiling((ln((abs(phi(x0) - x0)) / ((1 - q) * eps))) / (ln(1 / q))) + 1
print("Апріорна оцінка методу простої ітерації:", apriori_simple_iter)
simple_iter_result, aposteriori_simple_iter = simple_iteration(x0, eps, q)
print("Корінь: ", simple_iter_result, "| Апостеріорна оцінка: ", aposteriori_simple_iter)

# Модифікований метод Ньютона
print ("Модифікований метод Ньютона:")
modified_newton_result, aposteriori_modified_newton = modified_newton(x0, eps)
print("Корінь: ", modified_newton_result, "| Апостеріорна оцінка: ", aposteriori_modified_newton)
