import matplotlib.pyplot as plt

x = .1  # normalized initial population (in 0-1 range)


xfin = []
r = 3  # initial r parameter
rEnd = 3.5  # final r value; 4 makes sense because of mathematical and practical properties of attractor
step = 0.01
tries = 100


nextx = 0
plt.figure()
while(r<rEnd):
    for i in range(tries):
        nextx = r*x*(1-x)
        xfin.append(nextx)
        x = nextx
        if (r<3.5) & (i > 31) & (i <= 64):
            # because in these region x oscilates between some values,
            # we display 32 of them (if there are less than 32, points will cover each other
            plt.scatter(r, x, c='black', s=1)
        elif (r >= 3.5) & (i > tries-50):  # for r above 3.5 attractor is chaotic, so last 50 results are plotted
            plt.scatter(r, x, c='black', s=1)

    if r < 3:  # for low r values last x value is plotted
        plt.scatter(r, x, c='black', s=1)


    x = .1
    nextx = 0
    r = r+step
    print(r)
plt.show()
