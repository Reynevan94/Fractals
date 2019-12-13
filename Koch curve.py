import turtle as t
from PIL import Image

import math
def TMseq(n):
    binary = []

    while(n != 0):
        binary.append(n%2)
        n = math.floor(n/2)
    s = sum(binary)
    if(s%2==0):
        return 0
    else:
        return 1

steps = 8400
path = []
for i in range(steps):
    path.append(TMseq(i))

print(path)

t.color('black')
t.speed(0)
t.up()
t.setpos(-300,0)
t.down()
t.left(150)
t.ht()

lineLenght = 1

j = 0
for p in path:
    print(j/steps)
    j = j+1
    if p == 0:
        t.forward(lineLenght)
    else:
        t.left(60)

ts = t.getscreen()
ts.getcanvas().postscript(file="Koch_curve.eps")
t.done()