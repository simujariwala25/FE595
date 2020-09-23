#import required libraries
import numpy as np
import matplotlib.pyplot as plt

def func1():
    x = np.arange(0, 2*np.pi, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z)
    plt.xlabel('x values')
    plt.ylabel('sin(x) & cos(x)')
    plt.title('Plot of sine & cosine')
    plt.legend(['sin(x)', 'cos(x)'])
    plt.show()

if __name__ == "__main__":
    func1()