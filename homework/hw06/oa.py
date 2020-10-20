import math 

# alpha = float(input('your \\alpha'))
# beta = float(input('your \\beta'))
# gamma = float(input('your \\gamma'))
# vgst6 = float(input('your (V_GS6 - V_T6)'))

# the act_1
# alpha = 3 
# beta = 4
# gamma = 3
# vgst6 = 0.2

alpha = 3 
beta = 4
gamma = 3
vgst6 = 0.2

mu = 33e-3

gbw = 50e6
cl = 5e-12

ft = 16 * gbw 

cc = cl / alpha 
cgs6 = cc / beta 
gm6 = ft * 2 * math.pi * cgs6
gm1 = 2 * math.pi * cc * gbw 

l = (3 * mu * vgst6 / (4 * math.pi * ft))**0.5

k = 2e-15/1e-6
w6 = cgs6 / k 
i6 = gm6/2 * vgst6 

i1 = gm1/10 

print('cc ', cc)
print('gm6 ', gm6)
print('gm1 ', gm1)
print('l ', l)
print('w6 ', w6)
print('i6 ', i6)
print('i1 ', i1)
print('i6/i1: ', 16/beta)