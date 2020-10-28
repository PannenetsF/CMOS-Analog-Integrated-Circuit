import math

GBWDM = 50e6
GBWCM = 100e6 * 1.2

kn = 280e-6
kp = 60e-6

L = 0.5e-6

CL = 5e-12

VGST1 = 0.2
VGST2 = 0.2
VGST3 = 0.2
VGST4 = 0.2
VGST7 = 0.2

gm1 = 2 * math.pi * CL * GBWDM
gm7 = 4 * math.pi * CL * GBWCM

# for PMOS 1

I1 = gm1 / 2 * VGST1
W1 = gm1 * L / kp / VGST1
IB1 = 2 * I1

# for NMOS 2

I2 = I1 * 1.1
W2 = 2 * I2 / kn * L / (VGST2)**2

# for NMOS 3

I3 = I1 * 0.1
W3 = 2 * I3 / kn * L / (VGST3)**2

# for PMOS 4

I4 = I3
W4 = 2 * I4 / kp * L / (VGST4)**2

# for NMOS 7

I7 = gm7 / 2 * VGST7
W7 = gm7 * L / kn / VGST7
IB2 = 2 * I7

print("L: um: ", L * 1e6)
print('IB1: uA: ', IB1 * 1e6)
print('I1: uA: ', I1 * 1e6)
print('gm1: ', gm1)
print('W1: um: ', W1)
print('W2: um: ', W2)
print('W3: um: ', W3)
print('W4: um: ', W4)
print('I7: uA: ', I7 * 1e6)
print('gm7: ', gm7)
print('W7: um: ', W7)
print('IB2: uA: ', IB2 * 1e6)
