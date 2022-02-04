from math import *

def get_sin(theta):
    return round(sin(pi * (theta / 180)), 2)

def get_cos(theta):
    return round(cos(pi * (theta / 180)), 2)

def get_force_X(F, theta):
    return F * get_cos(theta)

def get_force_Y(F, theta):
    return F * get_sin(theta)

def get_a(F, m):
    return F / m;

def get_v(a, t):
    return a * t;

def get_s(v, t):
    return v* t

def get_max_s(F, m, t, g, theta):
    return (2 * pow(F, 2) * pow(t, 2) * get_cos(theta) * get_sin(theta)) / (pow(m, 2) * g)

def get_max_h(F, m, t, g, theta):
    return (pow(F, 2) * pow(t, 2) * pow(get_sin(theta), 2)) / (2 * pow(m, 2) * g)

def h_s_function(F, m, t, g, theta, s):
    if((2 * pow(F, 2) * pow(t, 2) * pow(get_cos(theta), 2)) == 0):
        return 0
    return -(pow(m, 2) * g) / (2 * pow(F, 2) * pow(t, 2) * pow(get_cos(theta), 2)) * s * (s-get_max_s(F, m, t, g ,theta))

def get_F_by_theta(theta, h, s, m, t, g):
    if((2 * pow(t, 2) * get_cos(theta) * (h * get_cos(theta) - s * get_sin(theta))) == 0):
        return None
    innerNumber = -(pow(m, 2 )* g * pow(s, 2)) / (2 * pow(t, 2) * get_cos(theta) * (h * get_cos(theta) - s * get_sin(theta)))
    if(innerNumber < 0):
        return None
    return sqrt(innerNumber)

def get_inclination(F, m, t, g, theta):
    return -(pow(m, 2) * g) / (2 * pow(F, 2) * pow(t, 2) * pow(get_cos(theta), 2))

def get_function(F, m, t, g, theta):
    inclination = get_inclination(F, m, t, g, theta)
    max_s = get_max_s(F, m, t, g , theta)
    return f"h = ({inclination})(s - {max_s})s"