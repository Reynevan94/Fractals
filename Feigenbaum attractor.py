import matplotlib.pyplot as plt

x = .1
nextx = 0

xfin = []
r = 3.8
tries = 1000

plt.figure()
while(r<4):
    for i in range(tries):
        nextx = r*x*(1-x)
        xfin.append(nextx)
        x = nextx
        if (r >= 3.5) & (i > tries-50):
            plt.scatter(r, x, c='black', s=1)
    if r < 3.5:
        plt.scatter(r, x, c='black', s=1)

    x = .1
    nextx = 0
    xfin = []
    r = r+0.001
    print(r)
plt.show()
