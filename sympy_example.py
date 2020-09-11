import sympy as sm
from sympy.plotting import plot
x,y = sm.Symbol('x'), sm.Symbol('y')

f = x**2 + 2*x + 1
f2 = (x**2-1) / (x+1)
f3 = (x**2-1) / (x+1) + (x) / (x-1)

# sm.pprint(f2)
print(f2.simplify())
sm.pprint(f3.together().simplify())

print(f3.subs({x:2}))

der = sm.Derivative(f, x, x)
sm.pprint(der)
sm.pprint(der.doit())


lim = sm.Limit(f, x, 0)
sm.pprint(lim)
sm.pprint(lim.doit())

integ = sm.Integral(f, (x, 0, 4))
sm.pprint(integ)
sm.pprint(integ.doit())


summation = sm.Sum(f, (x, 0, 4))
sm.pprint(summation)
sm.pprint(summation.doit())

summation = sm.Product(f, (x, 0, 4))
sm.pprint(summation)
sm.pprint(summation.doit())

plot(f2)