import numpy as np
#from sympy.plotting import plot
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
plt.ylabel('Torque [N.m]')
plt.xlabel('Velocidade [rad/s]')


#Dados:
#w = symbols('w')
#tpl = (50*w)/178
#np.arange(0, 310, 10)
w =  np.arange(0, 310, 10) #velocidade
s = np.arange(1, 51, 1)  #escorregamento
x =  np.arange(50, 301, 1)   #alteração
p = 50*w/178 #torque da plaina

print("=================================================================================")
print("Velocidade: ", w)

#ts = 300-(0.0084*(w*w))
t = 316*(2/((1/s)+(s/1)))
tf = 202.24*(2/((25/x)+(x/25)))
print("=================================================================================")
print("Torque de partida valores: ", t)

print("=================================================================================")
print("Torque reduzido valores: ", tf)



l, = plt.plot(w, p, label='Torque of the jointer', lw=2, color='red')
c, = plt.plot(s, t, label='Torque de partida', lw=2, color='black')
m = plt.plot(x, tf, label='Redução', lw=2, color='blue')

plt.axis([0, 300, 0, 300])
plt.legend()






    

plt.show()



