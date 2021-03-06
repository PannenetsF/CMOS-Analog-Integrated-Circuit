import math 

kn = 280e-6
kp = 60e-6

alpha = 6
beta = 3
gamma = 6
vgst6 = 0.2
vgst1 = 0.2
vgst3 = 0.2

mu = 33e-3

gbw = 50e6
cl = 5e-12

ft = alpha * gamma * (1 + beta) * gbw 

cc = cl / alpha 
cgs6 = cc / beta 
gm6 = ft * 2 * math.pi * cgs6
gm1 = 2 * math.pi * cc * gbw 

l = (3 * mu * vgst6 / (4 * math.pi * ft))**0.5

k = 2e-15/1e-6
w6 = cgs6 / k 
i6 = gm6/2 * vgst6 

i1 = gm1/10 

w1 = 2 * i1 * l / kp / vgst1**2
w3 = 2 * i1 * l / kn / vgst3**2

print('l:u ', l*1e6)
print('w6:u ', w6*1e6)
print('w1:u ', w1*1e6)
print('w3:u ', w3*1e6)
print('cc ', cc)
print('gm6 ', gm6)
print('gm1 ', gm1)
print('i6:u ', i6*1e6)
print('i1:u ', i1*1e6)
print('i6/i1: ', i6/i1)