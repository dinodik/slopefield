import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-10, 10, 25)
Y = np.linspace(-10, 10, 25)
mX, mY = np.meshgrid(X, Y)

dydx = -(2*mX+mY+1)/(mX+2*mY+1)
U = 1/np.sqrt(dydx**2 + 1)
V = dydx/np.sqrt(dydx**2 + 1)

fig, ax = plt.subplots()
ax.set_title(r"$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{2x+y=1}{x+2y+1}$ from example 13.5 on p.14")
ax.quiver(mX, mY, U, V, pivot="middle", headaxislength=0, headlength=0)

for c in [4, 50, 100]:
    left = (-1-np.sqrt(2 * (3*c+2)))/3
    right = (-1+np.sqrt(2 * (3*c+2)))/3
    X = np.linspace(left, right, 4000)
    ax.plot(X, -(X+1)/2 + 1/np.sqrt(2) * np.sqrt(c - 2*(X**2+X) + 0.5*(X+1)**2), 'b')
    ax.plot(X, -(X+1)/2 - 1/np.sqrt(2) * np.sqrt(c - 2*(X**2+X) + 0.5*(X+1)**2), 'b')
plt.show()
