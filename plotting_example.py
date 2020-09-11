from matplotlib import pyplot as plt
import numpy
fig, axes = plt.subplots(2, 1)

x = numpy.linspace(0, 100, 20)
y = x**2
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

axes[0].plot(x, y, marker='s', ls='--', color='r')
axes[0].set_xticks([0, 50, 100])
axes[1].pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
axes[1].axis('equal')
plt.show()