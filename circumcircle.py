# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:22:29 2020

@author: joniel
"""

from PIL import Image
from random import random
import numpy as np

img = Image.new( 'RGB' , (400,400) , (0,0,0) )

x1, y1 = random(), random()
x2, y2 = random(), random()
x3, y3 = random(), random()

def i(x, xmin = 0.0, xmax = 1.0, vmin = 0, vmax = 400):
    return int(vmin + (x - xmin) * (vmax - vmin) / (xmax - xmin))
   
def bresenham(px1, py1, px2, py2): #my working implementation
    if(px1 < px2 and py1 < py2):
        y = py1
        ay = py1
        dx = px2 - px1
        dy = py2 - py1
        slope = dy/dx
        if(slope<1):
            for x in range(px1, px2+1):
                if(abs(y-(ay+slope)) < abs((y+1)-(ay+slope))):
                    img.putpixel((x,y),(255, 0, 255))
                else:
                    y += 1
                    img.putpixel((x,y),(255, 0, 255))
                ay += slope
        else:
            x = px1
            ax = px1
            dx = px2 - px1
            dy = py2 - py1
            slope = dx/dy
            for y in range(py1, py2+1):
                if(abs(x-(ax+slope)) < abs((x+1)-(ax+slope))):
                    img.putpixel((x,y),(255, 0, 255))
                else:
                    x += 1
                    img.putpixel((x,y),(255, 0, 255))
                ax += slope
            
            
    elif(px1 > px2 and py1 > py2):
        px1, px2 = px2, px1
        py1, py2 = py2, py1
        y = py1
        ay = py1
        dx = px2 - px1
        dy = py2 - py1
        slope = dy/dx
        if(slope<1):
            for x in range(px1, px2+1):
                if(abs(y-(ay+slope)) < abs((y+1)-(ay+slope))):
                    img.putpixel((x,y),(255, 0, 255))
                else:
                    y += 1
                    img.putpixel((x,y),(255, 0, 255))
                ay += slope
        else:
            x = px1
            ax = px1
            dx = px2 - px1
            dy = py2 - py1
            slope = dx/dy
            for y in range(py1, py2+1):
                if(abs(x-(ax+slope)) < abs((x+1)-(ax+slope))):
                    img.putpixel((x,y),(255, 0, 255))
                else:
                    x += 1
                    img.putpixel((x,y),(255, 0, 255))
                ax += slope
    elif(px1 < px2 and py1 > py2):
        y = py1
        ay = py1
        dx = px2 - px1
        dy = py2 - py1
        slope = dy/dx
        slope = abs(slope)
        if(slope<1):
            for x in range(px1, px2+1):
                if(abs(y-(ay-slope)) < abs((y-1)-(ay-slope))):
                    img.putpixel((x,y),(255, 0, 255))
                else:
                    y -= 1
                    img.putpixel((x,y),(255, 0, 255))
                ay -= slope
        else:
            x = px2
            ax = px2
            dx = px2 - px1
            dy = py2 - py1
            slope = dx/dy
            slope = abs(slope)
            for y in range(py2, py1+1):
                if(abs(x-(ax-slope)) < abs((x-1)-(ax-slope))):
                    img.putpixel((x,y),(255, 0, 255))
                else:
                    x -= 1
                    img.putpixel((x,y),(255, 0, 255))
                ax -= slope
    else:
        px1, px2 = px2, px1
        py1, py2 = py2, py1
        y = py1
        ay = py1
        dx = px2 - px1
        dy = py2 - py1
        slope = dy/dx
        slope = abs(slope)
        if(slope<1):
            for x in range(px1, px2+1):
                if(abs(y-(ay-slope)) < abs((y-1)-(ay-slope))):
                    img.putpixel((x,y),(255, 0, 255))
                else:
                    y -= 1
                    img.putpixel((x,y),(255, 0, 255))
                ay -= slope
        else:
            x = px2
            ax = px2
            dx = px2 - px1
            dy = py2 - py1
            slope = dx/dy
            slope = abs(slope)
            for y in range(py2, py1+1):
                if(abs(x-(ax-slope)) < abs((x-1)-(ax-slope))):
                    img.putpixel((x,y),(255, 0, 255))
                else:
                    x -= 1
                    img.putpixel((x,y),(255, 0, 255))
                ax -= slope

def circumcenter(px1, py1, px2, py2, px3, py3):
    ma = ([px1, py1, 1], [px2, py2, 1], [px3, py3, 1])   
    mbx = ([px1**2 + py1**2, py1, 1], [px2**2 + py2**2, py2, 1], [px3**2+py3**2, py3, 1])
    mby = ([px1**2 + py1**2, px1, 1], [px2**2 + py2**2, px2, 1], [px3**2+py3**2, px3, 1])
    a = np.linalg.det(ma) * 2
    bx = np.linalg.det(mbx) * -1
    by = np.linalg.det(mby)
    return ((bx/a) * -1), ((by/a) * -1)

def circumradius(px1, py1, px2, py2, px3, py3):
    ma = ([px1, py1, 1], [px2, py2, 1], [px3, py3, 1])   
    mbx = ([px1**2 + py1**2, py1, 1], [px2**2 + py2**2, py2, 1], [px3**2+py3**2, py3, 1])
    mby = ([px1**2 + py1**2, px1, 1], [px2**2 + py2**2, px2, 1], [px3**2+py3**2, px3, 1])
    mc = ([px1**2 + py1**2, px1, py1], [px2**2 + py2**2, px2, py2], [px3**2+py3**2, px3, py3])
    a = np.linalg.det(ma)
    c = np.linalg.det(mc) * -1
    bx = np.linalg.det(mbx) * -1
    by = np.linalg.det(mby)
    return (pow(bx**2 + by**2 - 4 * a * c, 1/2) / (2 * abs(a)))

def int_radius(x, r): 
    return i(x+r) - i(x)

def r_err(x, y, r):
    return abs(pow(x,2)+pow(y,2)-pow(r,2)) 
     
def circle(x, y, r):
    xi = x + r
    yi = y
    dx = r
    dy = 0
    rerr = 0
    for yi in range(yi, y+int(3*r/4)):
        yerr = 2 * dy + 1
        xerr = -2 * dx + 1
        if(2*(rerr + yerr) + xerr > 0):
            xi -= 1
            dx = xi - x
            rerr += xerr
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(255, 255, 0))
        else:
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(255, 255, 0))
        dy = yi - y
        rerr += yerr
    xi = x
    yi = y + r
    dx = 0
    dy = r
    rerr = 0
    for xi in range(xi, x+int(3*r/4)):
        yerr = 2 * dy + 1
        xerr = -2 * dx + 1
        if(2*(rerr + yerr) + xerr < 0):
            yi -= 1
            dy = yi - y
            rerr += yerr
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(255, 255, 0))
        else:
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(255, 255, 0))
        dx = xi - x
        rerr += xerr
    xi = x - r
    yi = y
    dx = -r
    dy = 0
    rerr = 0
    for yi in range(yi, y+int(3*r/4)):
        yerr = 2 * dy + 1
        xerr = 2 * dx + 1
        if(2*(rerr + yerr) + xerr > 0):
            xi += 1
            dx = xi - x
            rerr += xerr
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(0, 200, 255))
        else:
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(0, 200, 255))
        dy = yi - y
        rerr += yerr
    xi = x
    yi = y + r
    dx = 0
    dy = r
    rerr = 0
    for xi in range(xi, x-int(3*r/4), -1):
        yerr = 2 * dy + 1
        xerr = 2 * dx + 1
        if(2*(rerr + yerr) + xerr < 0):
            yi -= 1
            dy = yi - y
            rerr += yerr
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(0, 200, 255))
        else:
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(0, 200, 255))
        dx = xi - x
        rerr += xerr
    xi = x - r
    yi = y
    dx = -r
    dy = 0
    rerr = 0
    for yi in range(yi, y-int(3*r/4), -1):
        yerr = -2 * dy + 1
        xerr = 2 * dx + 1
        if(2*(rerr + yerr) + xerr > 0):
            xi += 1
            dx = xi - x
            rerr += xerr
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(255, 0, 0))
        else:
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(255, 0, 0))
        dy = yi - y
        rerr += yerr
    xi = x
    yi = y - r
    dx = 0
    dy = r
    rerr = 0
    for xi in range(xi, x-int(3*r/4), -1):
        yerr = -2 * dy + 1
        xerr = 2 * dx + 1
        if(2*(rerr + yerr) + xerr < 0):
            yi += 1
            dy = yi - y
            rerr += yerr
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(255, 0, 0))
        else:
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(255, 0, 0))
        dx = xi - x
        rerr += xerr
    xi = x + r
    yi = y
    dx = -r
    dy = 0
    rerr = 0
    for yi in range(yi, y-int(3*r/4), -1):
        yerr = -2 * dy + 1
        xerr = -2 * dx + 1
        if(2*(rerr + yerr) + xerr > 0):
            xi -= 1
            dx = xi - x
            rerr += xerr
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(0, 255, 0))
        else:
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(0, 255, 0))
        dy = yi - y
        rerr += yerr
    xi = x
    yi = y - r
    dx = 0
    dy = r
    rerr = 0
    for xi in range(xi, x+int(3*r/4)):
        yerr = -2 * dy + 1
        xerr = -2 * dx + 1
        if(2*(rerr + yerr) + xerr < 0):
            yi += 1
            dy = yi - y
            rerr += yerr
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(0, 255, 0))
        else:
            if(xi>=0 and xi<400 and yi>=0 and yi<400):
                img.putpixel((xi,yi),(0, 255, 0))
        dx = xi - x
        rerr += xerr
    

                    
bresenham(i(x1), i(y1), i(x2), i(y2))
bresenham(i(x2), i(y2), i(x3), i(y3))
bresenham(i(x3), i(y3), i(x1), i(y1))
x0, y0 = circumcenter(x1, y1, x2, y2, x3, y3)
r = circumradius(x1, y1, x2, y2, x3, y3)
r = int_radius(x0, r)
circle(i(x0), i(y0), r)

# bresenham(250, 300, 300, 155)
# bresenham(300, 155, 20, 200)
# bresenham(20, 200, 250, 300)
# x0, y0 = circumcenter(250, 300, 300, 155, 20, 200)
# r = circumradius(250, 300, 300, 155, 20, 200)
# r = int(r)
# circle(int(x0), int(y0), r)

img.save( 'circle.png' )
print( 'done' )
