import numpy as np
from numpy import loadtxt
from matplotlib import pyplot as plt
import re

if __name__ == '__main__':

    array2 = np.zeros((200,200))
    x = np.zeros((200,200))
    y = np.zeros((200, 200))

    for j in range(0,199):
        source = 'output' + str(j) + '.txt'
        f = open(source, 'r')
        data = f.read()
        data = data[1:-15]
        line = f.readline()
        array = np.array(data.split(), dtype=float)

        for i in range(0,199):
           # print(array[i])
            array2[j][i] = array[i]
            x[j][i] = i
            y[j][i] = j

    print(array2)
    print(array2[100][2])
    print(array2.shape)

    fig = plt.scatter(y,x,c=array2,cmap='jet')
    plt.colorbar()
    plt.show()
