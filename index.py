import graph
import values
import physics

minForce = {'theta' : None, 'F' : None}
maxForce = {'theta' : None, 'F' : None}

times = 100

for i in range(0, 90 * times + 1):
    theta = i / times
    F = physics.get_F_by_theta(theta, values.h, values.s, values.m, values.t0, values.g)
    if(F == None):
        continue
    if(minForce['F'] == None ):
        minForce['F'] = F
        minForce['theta'] = theta
        maxForce['F'] = F
        maxForce['theta'] = theta
    if(minForce['F'] > F):
        minForce['F'] = F
        minForce['theta'] = theta
        graph.set_parabolic_motion_graph(theta, F, [0, values.s])
    if(maxForce['F'] < F):
        maxForce['F'] = F
        maxForce['theta'] = theta
        #graph.set_parabolic_motion_graph(theta, F, [0, values.s])
    #graph.set_parabolic_motion_graph(theta, F, [0, values.s])
graph.set_parabolic_motion_graph(minForce['theta'], minForce['F'], [0, values.s])
print()
print(physics.get_function(minForce['F'], values.m, values.t0, values.g, minForce['theta']))

#graph.set_parabolic_motion_graph(maxForce['theta'], maxForce['F'], [0, values.s])
print(f"minForce : {minForce['F']}")
print(f"minTheta : {minForce['theta']}")
print(f"maxForce : {maxForce['F']}")
print(f"maxForce : {maxForce['theta']}")
graph.draw_parabolic_motion_graph()
