import matplotlib.pyplot as plt

bar = [0, 1]

bars = [bar]
nextBars = [bar]
nextBars2 = []
steps = 4  # more steps lacks resolution

for i in range(steps):
    for b in nextBars:
        newBar1 = [b[0], b[0] + (b[1] - b[0]) / 3]
        newBar2 = [b[1] - (b[1] - b[0]) / 3, b[1]]

        nextBars2.append(newBar1)
        nextBars2.append(newBar2)

    nextBars = nextBars2
    for new in nextBars:
        bars.append(new)
    nextBars2 = []

i = 1
j = 0
plt.figure()

for b in bars:
    plt.plot(b, [-j, -j], c="black")

    if i % (2 ** j) == 0:
        j = j + 1
        i = 0
    i = i + 1
plt.axis('off')
plt.show()
