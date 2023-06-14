#python.exe
import numpy as np
from PIL import Image

def mandelbrot(c, maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return 0

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), maxiter) for r in r1] for i in r2]))

def mandelbrot_image(xmin, xmax, ymin, ymax, width=10, height=10, maxiter=256):
    x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter)
    img = Image.new('RGB', (width,height), color='white')
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i,j] = (i % 8 * 32, j % 8 * 32,int(z[j,i]) % 8 * 32)
    return img

img = mandelbrot_image(-2.0,0.5,-1.25,1.25,width=1000,height=1000,maxiter=256)
img.show()
