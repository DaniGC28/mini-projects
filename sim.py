import numpy as np
import pygame
from pygame.locals import *

simulation_time = 10**3
eps = 10**(-3)

fps = 60
speed = 10

g = 9.81
l = 150
m = 1

def dda(a, b, da, db):

    term1 = np.sin(a-b)*(da**2 * np.cos(a-b) + db**2)
    term2 = g/l * (2*np.sin(a) - np.cos(a-b)*np.sin(b))

    return (term1 + term2)/(np.cos(a-b)**2 - 2)

def ddb(a, b, da, db, dda_numval):

    term1 = -dda_numval*np.cos(a-b)
    term2 = da**2*np.sin(a-b)
    term3 = -g/l * np.sin(b)

    return term1 + term2 + term3


a  = -np.pi/2
b  = 0
da = 0
db = 0

a_hist = [a]
b_hist = [b]

t = 0

t_hist = [t]

while t <= simulation_time:

    temp_da = da
    temp_db = db

    dda_numval = dda(a, b, temp_da, temp_db)

    da = temp_da + eps * dda_numval
    db = temp_db + eps * ddb(a, b, temp_da, temp_db, dda_numval)

    a += eps * temp_da
    b += eps * temp_db

    a_hist.append(a)
    b_hist.append(b)

    t += eps
    t_hist.append(t)
    


print("sim done")

pygame.init()

window = pygame.display.set_mode((600, 600))


radius = 10
ball1 = pygame.Surface((radius*2, radius*2))
pygame.draw.circle(ball1, "white", (radius, radius), radius)


clock = pygame.time.Clock()


i = 0
n = 0

while n < len(t_hist):

    clock.tick(fps)

    n = int(i * (1/fps) / eps * speed)

    x1 = l * np.sin(a_hist[n])
    y1 = l * np.cos(a_hist[n])

    x2 = x1 + l*np.sin(b_hist[n])
    y2 = y1 + l*np.cos(b_hist[n])

    pygame.draw.line(
        window,
        "grey",
        (300, 200),
        (x1 + 300, y1 + 200),
        3
    )

    pygame.draw.line(
        window,
        "grey",
        (x1 + 300, y1 + 200),
        (x2 + 300, y2 + 200),
        3
    )

    window.blit(ball1, (x1 + 300 - radius, y1 + 200 - radius))
    window.blit(ball1, (x2 + 300 - radius, y2 + 200 - radius))

    pygame.display.update()

    window.fill((0, 0, 0))

    i += 1

    