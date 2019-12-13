import turtle as t
from PIL import Image

lineLenght = 10
reps = 4

aReplace = ['A', '-', 'B', '-', '-', 'B', '+', 'A', '+', '+', 'A', 'A', '+', 'B', '-']
bReplace = ['+', 'A', '-', 'B', 'B', '-', '-', 'B', '-', 'A', '+', '+', 'A', '+', 'B']

def replace(list):
    newList = []
    for i in list:
        if (i == 'A'):
            for a in aReplace:
                newList.append(a)
        elif (i == 'B'):
            for b in bReplace:
                newList.append(b)
        elif (i == '-'):
            newList.append('-')
        else:
            newList.append('+')
    return(newList)

angle = 60
axiom = 'A'

list = [axiom]

for i in range(reps):
    list = replace(list)

print(list)



t.color('black')
t.speed(0)
t.up()
t.setpos(-300,0)
t.down()
t.left(90)
t.ht()
for move in list:
    if move == 'A':
        t.forward(lineLenght)
    elif move == 'B':
        t.forward(lineLenght)
    elif move == '+':
        t.left(60)
    elif move == '-':
        t.right(60)

ts = t.getscreen()
ts.getcanvas().postscript(file="Gosper_curve.eps")
t.done()