import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    plt.figure()
    x=np.random.randint(0,50,50)
    plt.subplot(221)
    plt.plot(x,np.sin(x))

    plt.subplot(222)
    plt.plot(x,np.cos(x))

    plt.subplot(223)
    plt.plot(x,np.tan(x))

    plt.subplot(224)
    plt.plot(x,x**2,marker=(5,2))

    plt.show()
