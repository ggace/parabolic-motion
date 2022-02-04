from matplotlib import pyplot as plt

import physics
import values

times = 100

def set_parabolic_motion_graph(theta, F=values.F, xlimit = None):
    
    
    if(xlimit == None):
        xlimit = [0, round(physics.get_max_s(F, values.m, values.t0, values.g, theta), 2)]
    
    xs = []
    ys = []

    for i in range(xlimit[0], int(xlimit[1] * times) + 1):
        x = i / times
        xs.append(x)
        ys.append(physics.h_s_function(F, values.m, values.t0, values.g, theta, x))

    print(f"max height \t:{physics.get_max_h(F, values.m, values.t0, values.g, theta)}")
    print(f"max distance \t:{physics.get_max_s(F, values.m, values.t0, values.g, theta)}")
    print(f"F \t\t:{F}")
    print(f"theta \t\t:{theta}")
    plt.plot(xs,ys)
    
    
def draw_parabolic_motion_graph(F=values.F):
    plt.title(f"parabolic motion graph")
    plt.xlabel('distance(m)')
    plt.ylabel('height(m)')
    plt.show()