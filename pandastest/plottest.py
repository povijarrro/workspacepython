#!python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from functools import partial

def main():
    ls = np.linspace(-np.pi,np.pi,100)
    sinls = np.sin(ls)
    cosls = np.cos(ls)
    fig, ax = plt.subplots(2,1)
    ax[0].plot(ls,sinls,color = "black",linewidth = 0.5, label = "sin")
    ax[1].plot(ls,cosls, color = "red",linewidth = 0.5, label = "cos")
    ax[0].set_title("sin")
    ax[1].set_title("cos")
    ax[0].set_aspect("equal")
    ax[1].set_aspect("equal")
    fig.suptitle("Some goniometric functions")
    ax[0].legend()
    ax[1].legend()
    plt.show()

if __name__ == "__main__":
     main()