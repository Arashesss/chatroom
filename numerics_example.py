import numpy
import numpy.linalg as linalg

m1 = numpy.random.randint(1, 100, 10)
print(m1)
print(type(m1))
print(m1.size)
print(m1.shape)
m2 = numpy.linspace(0, 10, 4)
print(m2)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
m3 = numpy.array(l)
m3 = m3.reshape((3, 3))
print(m3)
print(m3[0][0])
print(m3[0, 0])
m4 = numpy.zeros((4,4))
m5 = numpy.ones((4,4))
m6 = numpy.eye(3, 3)

print(m6)
print(m6.T)
# a = numpy.array([2, 4, 4, 8]).reshape((2, 2))
# b = numpy.array([6, 12]).reshape(2, 1)
# print(linalg.solve(a, b))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
m7 = numpy.array(l).reshape(4, 4)
print(m7[::,0::3])
