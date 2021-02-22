from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

g = 9.8
l1 = 1.0
l2 = 1.0
m1 = 1.0
m2 = 1.0

def derivs(state, t):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]
    delta = state[2] - state[0]
    den1 = (m1+m2) * l1 - m2 * l1 * cos(delta) * cos(delta)
    dydx[1] = ((m2 * l1 * state[1] * state[1] * sin(delta) * cos(delta)
                + m2 * g * sin(state[2]) * cos(delta)
                + m2 * l2 * state[3] * state[3] * sin(delta)
                - (m1+m2) * g * sin(state[0]))
               / den1)
    dydx[2] = state[3]

    den2 = (l2/l1) * den1
    dydx[3] = ((- m2 * l2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (m1+m2) * g * sin(state[0]) * cos(delta)
                - (m1+m2) * l1 * state[1] * state[1] * sin(delta)
                - (m1+m2) * g * sin(state[2]))
               / den2)

    return dydx
