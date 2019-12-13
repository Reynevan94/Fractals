from math import *
import matplotlib.pyplot as plt

steps = 10

Xset = []
Yset = []

for i in range(400):
    Xset.append(i*0.01-2)

b = 9
a = 0.7
print(a)
for x in Xset:
    val = 0
    for n in range(steps):
        val = val+a**n*cos(b**n*pi*x)
    Yset.append(val)

plt.figure()
plt.plot(Xset,Yset)
plt.show()