import math

GBW = 120e6

kn = 280e-6
kp = 70e-6

L = 0.5e-6

CL = 10e-12

VGST1 = 0.2
VGST2 = 0.2
VGST3 = 0.2
VGST4 = 0.2
VGST7 = 0.2


def est(i, norp):
    if norp == 'n':
        return 2 * i / kn * L / (0.2)**2 * 1e6
    if norp == 'p':
        return 2 * i / kp * L / (0.2)**2 * 1e6


gmn = 2 * math.pi * CL * GBW
gmp = gmn

# for PMOS 1

In = gmn / 10
Ip = gmp / 10
Wn = est(In, 'n')
Wp = est(Ip, 'p')
# for NMOS 2

print("L: um: ", L * 1e6)
print('In: uA: ', In * 1e6)
print('Ip: uA: ', Ip * 1e6)
print('W-p: um ', est(Ip, 'p'))
print('IB-p: um ', est(Ip, 'p'))
print('3*IB-p: um ', est(Ip * 3, 'p'))
print('W-n: um ', est(Ip, 'n'))
print('IB-n: um ', est(Ip, 'n'))
print('3*IB-n: um ', est(Ip * 3, 'n'))
