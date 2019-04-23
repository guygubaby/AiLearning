import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x=np.arange(0,10,0.2)
    y=np.sin(x)

    fig,(ax1,ax2,ax3,ax4)=plt.subplots(2,2)
    ax1.plot(x,y)
    ax2.plot(x,x**2)
    ax3.plot(x,np.cos(x))
    ax4.plot(x,np.tan(x))
    # plt.plot(x,y)
    plt.show()