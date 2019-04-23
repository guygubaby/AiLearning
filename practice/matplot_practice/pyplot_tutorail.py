import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    plt.figure()
    a=np.arange(0,5,0.2)
    plt.plot(a,a,'ro',a,a**2,'b^',a,a**3,'gs',a,np.sin(a),'b--')
    # plt.plot([1,2,3,4],[1,4,9,16],'ro')
    plt.axis([0,5,0,1])
    plt.ylabel('some numbers')
    plt.show()