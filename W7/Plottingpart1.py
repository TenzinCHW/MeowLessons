import scipy.constants as c

import numpy as np


def degToRad(deg):
    return round(float(deg) / 180 * c.pi, 5)


def radToDeg(rad):
    return round(float(rad) / c.pi * 180, 5)


# print degToRad(90)

# Problem 3
def sphericalToCartesian(r, theta, phi):  # Quite straightforward, just copy from worksheet
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * -np.cos(phi)
    return round(x, 5), round(y, 5), round(z, 5)


def cartesianToSpherical(x, y, z):
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    if x == 0 and y == 0:  # Handles cases when phi = 0 degrees
        phi = 0
    if x == 0 and y > 0:  # Handle cases when phi = 90 degrees
        phi = np.pi / 2
    if x == 0 and y < 0:  # Handle cases when phi = 270 degrees
        phi = -np.pi / 2
    if x != 0:  # Handle all other cases for phi
        phi = np.arctan(float(y) / x)
    if z == 0:  # Handle cases when theta = 90 degrees
        theta = np.pi / 2
    else:  # Handle all other cases for theta
        theta = np.arctan(np.sqrt(x ** 2 + y ** 2) / float(z))
    return round(r, 5), round(theta, 5), round(phi, 5)


print sphericalToCartesian(3, 0, np.pi)
print sphericalToCartesian(3, np.pi, 0)
print sphericalToCartesian(3, 3.14, 3.14)
print cartesianToSpherical(3, 0, 0)
print cartesianToSpherical(0, 3, 0)
print cartesianToSpherical(0, 0, 3)


# Problem 4
def fact(n):  # We've done this before
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# Problem 5
def p00(theta):
    return 1


def p10(theta):
    return np.cos(theta)


def p11(theta):
    return np.sqrt((np.sin(theta) ** 2))


def p20(theta):
    return 0.5 * (3 * (np.cos(theta) ** 2) - 1)


def p21(theta):
    return -3 * np.cos(theta) * np.sin(theta)


def p22(theta):
    return 3 * np.sin(theta) ** 2


def p30(theta):
    return 0.5 * (5 * np.cos(theta) ** 3 - 3 * np.cos(theta))


def p31(theta):
    return -1.5 * (5 * np.cos(theta) ** 2 - 1) * np.sin(theta)


def p32(theta):
    return 15 * np.cos(theta) * np.sin(theta) ** 2


def p33(theta):
    return -15 * np.sin(theta) ** 3


def p40(theta):
    return 0.125 * (35 * np.cos(theta) ** 4 - 30 * np.cos(theta) ** 2 + 3)


def p41(theta):
    return -2.5 * (7 * np.cos(theta) ** 3 - 3 * np.cos(theta)) * np.sin(theta)


def p42(theta):
    return 7.5 * (7 * np.cos(theta) ** 2 - 1) * np.sin(theta) ** 2


def p43(theta):
    return -105 * np.cos(theta) * np.sin(theta) ** 3


def p44(theta):
    return 105 * np.sin(theta) ** 4


def assocLegendre(m, l):
    if l == 0:
        if m == 0:
            return p00
    elif l == 1:
        if m == 0:
            return p10
        elif m == 1:
            return p11
    elif l == 2:
        if m == 0:
            return p20
        elif m == 1:
            return p21
        elif m == 2:
            return p22
    elif l == 3:
        if m == 0:
            return p30
        elif m == 1:
            return p31
        elif m == 2:
            return p32
        elif m == 3:
            return p33
    elif l == 4:
        if m == 0:
            return p40
        elif m == 1:
            return p41
        elif m == 2:
            return p42
        elif m == 3:
            return p43
        elif m == 4:
            return p44


# f = assocLegendre(0,0)
# print f(1)
# f = assocLegendre(1,1)
# print f(1)
# f = assocLegendre(2,3)
# print f(1)
# f = assocLegendre(2,3)
# print f(0)

# Problem 6
# This is getting quite tiring typing out all the formulae...
def L00(x):
    return 1


def L01(x):
    return 1


def L02(x):
    return 2


def L03(x):
    return 6


def L05(x):
    return 120


def L07(x):
    return 5040


def L10(x):
    return 1 - x


def L11(x):
    return -2 * x + 4


def L12(x):
    return -6 * x + 18


def L13(x):
    return -24 * x + 96


def L15(x):
    return -720 * (x - 6)


def L20(x):
    return x ** 2 - 4 * x + 2


def L21(x):
    return 3 * x ** 2 - 18 * x + 18


def L22(x):
    return 12 * x ** 2 - 96 * x + 144


def L23(x):
    return 60 * x ** 2 - 600 * x + 1200


def L30(x):
    return -x ** 3 + 9 * x ** 2 - 18 * x + 6


def L31(x):
    return -4 * x ** 3 + 48 * x ** 2 - 144 * x + 96


def L32(x):
    return -20 * x ** 3 + 300 * x ** 2 - 1200 * x + 1200


def L33(x):
    return -120 * x ** 3 + 2160 * x ** 2 - 10800 * x + 14400


def L40(x):
    return x ** 4 - 16 * x ** 3 + 72 * x ** 2 - 96 * x +24


def L41(x):
    return 5 * x ** 4 - 100 * x ** 3 + 600 * x ** 2 - 1200 * x + 600


def L42(x):
    return 30 * x ** 4 - 720 * x ** 3 + 5400 * x ** 2 - 14400 * x + 10800


def L43(x):
    return -210 * x ** 4 + 5880 * x ** 3 - 52920 * x ** 2 + 176400 * x - 176400


def L44(x):
    return 1680 * x ** 4 - 53760 * x ** 3 + 564480 * x ** 2 - 2257920 * x + 2822400


def assocLaguerre(p, qmp):
    if qmp == 0:
        if p == 0:
            return L00
        elif p == 1:
            return L01
        elif p == 2:
            return L02
        elif p == 3:
            return L03
        elif p == 5:
            return L05
        elif p == 7:
            return L07
    elif qmp == 1:
        if p == 0:
            return L10
        elif p == 1:
            return L11
        elif p == 2:
            return L12
        elif p == 3:
            return L13
        elif p == 5:
            return L15
    elif qmp == 2:
        if p == 0:
            return L20
        elif p == 1:
            return L21
        elif p == 2:
            return L22
        elif p == 3:
            return L23
    elif qmp == 3:
        if p == 0:
            return L30
        elif p == 1:
            return L31
        elif p == 2:
            return L32
        elif p == 3:
            return L33
    elif qmp == 4:
        if p == 0:
            return L40
        elif p == 1:
            return L41
        elif p == 2:
            return L42
        elif p == 3:
            return L43
        elif p == 4:
            return L44


# f = assocLaguerre(1,0)
# print f(2)
# f = assocLaguerre(1,1)
# print f(1)
# f = assocLaguerre(2,2)
# print f(1)
# f = assocLaguerre(2,2)
# print f(0)

# Problem 7
# THIS IS REALLY GETTING TIRING
def angular_wave_func(m, l, theta, phi):
    pfunc = assocLegendre(m, l)
    y = pfunc(theta)
    top = np.sqrt((2 * l + 1) * fact(l - abs(m)) / ((4 * c.pi) * fact(l + abs(m))))
    bottom = np.e ** (m * 1j * phi)
    ans = ((-1) ** m) * top * bottom * y
    return complex(round(ans.real, 5), round(ans.imag, 5))
    # rounded = round(ans.real, 5) - 0j
    # return rounded
    # return round(ans.real, 5) + round(ans.imag, 5) * 1j


# print angular_wave_func(0, 0, 0, 0)
# print angular_wave_func(0, 1, c.pi, 0)
# print angular_wave_func(1, 1, c.pi / 2, c.pi)
# print angular_wave_func(0, 2, c.pi, 0)

# Problem 8
a = c.physical_constants['Bohr radius'][0]


def radial_wave_func(n, l, r):
    # y1 = (2.0/(n*a))**3
    # y2 = fact(n-l-1)/float(2*n*fact(n+l)**3)
    # ya = np.sqrt(y1*y2)*np.exp(-r/(n*a))
    # yb = (2*r/(n*a))**l
    # lfunc = assocLaguerre(2*l+1,n-l-1)
    # yc = lfunc(2*r/(n*a))
    # return np.round((ya*yb*yc)/(a**(-1.5)),5)
    lfunc = assocLaguerre(2 * l + 1, n - l - 1)
    y = lfunc(2 * float(r) / (n * a))
    # y1 = (2.0 / (a * n)) ** 3
    # y2 = fact(n - l - 1)/(2 * n * fact(n + 1) ** 3)
    ya = np.sqrt((2.0 / (a * n)) ** 3 * fact(n - l - 1) / (2 * n * fact(n + l) ** 3)) * np.e ** (-float(r) / (n * a))
    yb = (2 * float(r) / n / a) ** l
    ans = ya * yb * y / (a ** -1.5)
    return np.round(ans, 5)


# print radial_wave_func(1, 0, a)
# print radial_wave_func(2, 1, a)
# print radial_wave_func(2, 1, 2 * a)
# print radial_wave_func(3, 1, 2 * a)

# Problem 9
def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
    rad = np.vectorize(radial_wave_func)
    ang = np.vectorize(angular_wave_func)
    cartsp = np.vectorize(cartesianToSpherical)
    mypow = np.vectorize(pow)
    myround = np.vectorize(round)
    myfloat = np.vectorize(float)
    matx = np.linspace(-roa, roa, Nx)
    maty = np.linspace(-roa, roa, Ny)
    matz = np.linspace(-roa, roa, Nz)
    xx, yy, zz = myround(np.meshgrid(matx, maty, matz), 5)
    r, theta, phi = cartsp(xx, yy, zz)
    radial = rad(n, l, r * a)
    angular = np.absolute(ang(m, l, theta, phi))
    psysquare = myround(mypow(myfloat(radial * angular), 2), 5)  # I am quite sure the formatting is wrong.
    return xx, yy, zz, psysquare


# Create data files for plotting in 2D
# x, y, z, mag = hydrogen_wave_func(2, 1, 1, 10, 20, 20, 20)
# x.dump('xdata210.dat')
# y.dump('ydata210.dat')
# z.dump('zdata210.dat')
# mag.dump('density210.dat')
x, y, z, mag = hydrogen_wave_func(3, 2, 1, 10, 20, 20, 20)
x.dump('xdata300.dat')
y.dump('ydata300.dat')
z.dump('zdata300.dat')
mag.dump('density300.dat')
print("done")