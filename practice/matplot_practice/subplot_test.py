import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    plt.figure()
    x=np.random.randint(0,np.pi,50)
    plt.subplot(221)
    plt.plot(x,np.sin(x),'ro')

    plt.subplot(222)
    plt.plot(x,np.cos(x),'go')

    plt.subplot(223)
    plt.plot(x,np.tan(x),'bo')

    plt.subplot(224)
    plt.plot(x,x**2,'go',marker=(5,2),)

    plt.show()
