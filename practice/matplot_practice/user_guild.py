import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x=np.linspace(0,2,100)
    plt.plot(x,x,label='first')
    plt.plot(x,x**2,label='second')
    plt.plot(x,x**3,label='third')
    plt.legend()
    plt.show()
